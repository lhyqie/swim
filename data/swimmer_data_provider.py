from abc import ABC, abstractmethod
import base64
from dataclasses import dataclass
import re
import time
from urllib.parse import quote

import requests


@dataclass(frozen=True)
class SwimmerProfile:
  slug: str
  name: str
  sex: str
  age: int
  team: str


class SwimmerSearchDataProvider(ABC):
  @abstractmethod
  def search_swimmers(self, query, limit=20, skip=0) -> list[SwimmerProfile]:
    pass


def _normalize_sex(sex):
  if sex in (1, "1"):
    return "Male"
  if sex in (-1, "-1"):
    return "Female"
  return str(sex or "")


def _normalize_age(age):
  try:
    return int(age or 0)
  except (TypeError, ValueError):
    return 0


def _swimmer_entries_from_payload(payload):
  if isinstance(payload, list):
    return payload
  if not isinstance(payload, dict):
    return []

  for key in ("data", "results", "swimmers", "items"):
    entries = payload.get(key)
    if isinstance(entries, list):
      return entries
  return []


def _swimmer_profile_from_entry(entry):
  return SwimmerProfile(
    slug=str(entry.get("slug") or entry.get("id") or entry.get("pkey") or ""),
    name=str(entry.get("name") or entry.get("Name") or entry.get("fullName") or ""),
    sex=_normalize_sex(entry.get("sex") or entry.get("gender")),
    age=_normalize_age(entry.get("age")),
    team=str(entry.get("team") or entry.get("swimTeam") or entry.get("clubName") or ""),
  )


class AjzxHubDataProvider(SwimmerSearchDataProvider):
  BASE_URL = "https://swim.ajzxhub.net"
  SEARCH_URL = "https://swim.ajzxhub.net/#search/{query}"
  PROXY_URL = "https://swim.ajzxhub.net/q?url={url}"
  SECURITY_INFO_URL = "https://securityapi.usaswimming.org/security/Auth/GetSecurityInfoForToken"
  DATAHUB_TOKEN_URL = "https://securityapi.usaswimming.org/security/DataHubAuth/GetSisenseAuthToken"
  SISENSE_URL = "https://usaswimming.sisense.com/api/datasources/{database}/jaql"
  IP_URLS = ("https://api.ipify.org", "https://ipv4.icanhazip.com")
  TOKEN_TTL_SECONDS = 50 * 60
  TIMEOUT_SECONDS = 20
  USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
  )
  DATASOURCES = {
    "swimmer": {
      "database": "Public Person Search",
      "dimensions": {
        "pkey": "Persons.PersonKey",
        "name": "Persons.FullName",
        "firstName": "Persons.FirstAndPreferredName",
        "lastName": "Persons.LastName",
        "age": "Persons.Age",
        "clubName": "Persons.ClubName",
        "lsc": "Persons.LscCode",
      },
    },
    "event": {
      "database": "USA Swimming Times Elasticube",
      "dimensions": {
        "pkey": "UsasSwimTime.PersonKey",
        "gender": "UsasSwimTime.EventCompetitionCategoryKey",
      },
    },
  }

  def __init__(self, session=None):
    self.session = session or requests.Session()
    self._access_token = None
    self._access_token_expires_at = 0
    if hasattr(self.session, "headers"):
      self.session.headers.update({"User-Agent": self.USER_AGENT})

  def search_swimmers(self, query, limit=20, skip=0) -> list[SwimmerProfile]:
    query = (query or "").strip()
    if not query:
      return []

    normalized_query, include_adults = self._normalize_query(query)
    if not normalized_query:
      return []

    entries = self._search_by_name(normalized_query, include_adults)
    if not entries:
      entries = self._search_by_club(normalized_query, include_adults)
    if entries:
      entries = self._filter_swimmers_with_events(entries)

    return [
      _swimmer_profile_from_entry(entry)
      for entry in entries[skip:skip + limit]
    ]

  def _normalize_query(self, query):
    include_adults = query.endswith("~19O")
    if include_adults:
      query = query[:-4]
    comma_index = query.find(",")
    if comma_index > 0:
      query = query[comma_index + 1:] + " " + query[:comma_index]
    return re.sub(r"\s+", " ", query.strip().lower()), include_adults

  def _search_by_name(self, query, include_adults):
    entries = self._query_swimmers(
      query,
      include_adults,
      {
        "name": [{"contains": term} for term in query.split()],
      },
    )
    return self._filter_entries(entries, query, "name")

  def _search_by_club(self, query, include_adults):
    entries = self._query_swimmers(
      query,
      include_adults,
      {
        "clubName": [{"contains": term} for term in query.split()],
      },
    )
    return self._filter_entries(entries, query, "clubName")

  def _query_swimmers(self, query, include_adults, filters):
    filters = {
      **filters,
      "age": {"from": 19} if include_adults else {"to": 18},
    }
    return self._query_datasource(
      "swimmer",
      5000 if "clubName" in filters else 1000,
      ["name", "age+", "clubName", "lsc", "pkey"],
      filters,
      query,
    )

  def _filter_entries(self, entries, query, field):
    terms = query.split()
    return [
      entry
      for entry in entries
      if self._matches_terms_in_order(terms, entry.get(field, ""))
    ]

  def _matches_terms_in_order(self, terms, value):
    value = " " + str(value or "").lower()
    start = 0
    for term in terms:
      start = value.find(" " + term, start)
      if start < 0:
        return False
      start += len(term) + 1
    return True

  def _filter_swimmers_with_events(self, entries):
    pkeys = [entry["pkey"] for entry in entries if entry.get("pkey") is not None]
    if not pkeys:
      return entries

    event_entries = self._query_datasource(
      "event",
      len(pkeys),
      ["pkey", "gender"],
      {"pkey": {"members": pkeys}},
    )
    if not event_entries:
      return entries

    active_pkeys = {entry.get("pkey") for entry in event_entries}
    sex_by_pkey = {
      entry.get("pkey"): self._sex_from_event_gender(entry.get("gender"))
      for entry in event_entries
    }
    return [
      {
        **entry,
        "sex": sex_by_pkey.get(entry.get("pkey"), ""),
      }
      for entry in entries
      if entry.get("pkey") in active_pkeys
    ]

  def _sex_from_event_gender(self, gender):
    if gender == 1:
      return "Female"
    if gender == 2:
      return "Male"
    return ""

  def _query_datasource(self, datasource_name, count, fields, filters, query=""):
    datasource = self.DATASOURCES[datasource_name]
    body = self._build_query(datasource_name, count, fields, filters)
    target_url = self.SISENSE_URL.format(database=datasource["database"])

    for attempt in range(2):
      access_token = self._get_access_token(query, force=attempt > 0)
      response = self._post_proxy(
        target_url,
        body,
        headers={"Authorization": f"Bearer {access_token}"},
      )
      if getattr(response, "status_code", None) == 401 and attempt == 0:
        self._clear_access_token()
        continue
      response.raise_for_status()
      payload = response.json()
      if payload.get("error") or "values" not in payload:
        return []
      return [
        dict(zip(payload.get("headers", []), row))
        for row in payload.get("values", [])
      ]
    return []

  def _build_query(self, datasource_name, count, fields, filters):
    datasource = self.DATASOURCES[datasource_name]
    metadata = []
    for field in fields:
      panel = None
      if field.startswith("_"):
        panel = "scope"
        field = field[1:]

      sort = None
      if field.endswith("-"):
        sort = "desc"
        field = field[:-1]
      elif field.endswith("+"):
        sort = "asc"
        field = field[:-1]

      item = {
        "dim": f"[{datasource['dimensions'][field]}]",
      }
      if panel:
        item["panel"] = panel
      else:
        item["title"] = field
      if sort:
        item["sort"] = sort

      field_filter = filters.get(field)
      if field_filter is None:
        metadata.append(item)
        continue

      field_filters = field_filter if isinstance(field_filter, list) else [field_filter]
      for index, filter_item in enumerate(field_filters):
        scoped_item = dict(item)
        if index > 0:
          scoped_item["panel"] = "scope"
          scoped_item.pop("title", None)
        scoped_item["filter"] = filter_item
        metadata.append(scoped_item)
    return {"metadata": metadata, "count": count}

  def _get_access_token(self, query="", force=False):
    if (
      not force
      and self._access_token
      and time.time() < self._access_token_expires_at
    ):
      return self._access_token

    ip_address = self._get_public_ip()
    host_id = base64.b64encode(
      str(self._ip_to_u32(ip_address)).encode("utf-8")
    ).decode("ascii")
    device_id = self._murmur_hash(
      ip_address
      + self.SEARCH_URL.format(query=quote(query, safe=""))
      + self.USER_AGENT
    )

    security_info = self._post_proxy_json(
      self.SECURITY_INFO_URL,
      {
        "toxonomies": [],
        "appName": "Data",
        "deviceId": device_id,
        "uIProjectName": "times-microsite-ui",
        "hostId": host_id,
        "bustCache": False,
        "scope": "Project",
      },
    )
    token_payload = self._post_proxy_json(
      self.DATAHUB_TOKEN_URL,
      {
        "sessionId": int(security_info["requestId"]) * 13,
        "deviceId": device_id,
        "hostId": host_id,
        "requestUrl": "/datahub",
      },
    )
    self._access_token = token_payload["accessToken"]
    self._access_token_expires_at = time.time() + self.TOKEN_TTL_SECONDS
    return self._access_token

  def _clear_access_token(self):
    self._access_token = None
    self._access_token_expires_at = 0

  def _get_public_ip(self):
    for url in self.IP_URLS:
      try:
        response = self.session.get(url, timeout=10)
        if response.ok:
          return response.text.strip()
      except requests.RequestException:
        pass
    return "169.254.130.1"

  def _post_proxy_json(self, target_url, payload, headers=None):
    response = self._post_proxy(target_url, payload, headers=headers)
    response.raise_for_status()
    return response.json()

  def _post_proxy(self, target_url, payload, headers=None):
    request_headers = {
      "Content-Type": "application/json",
      "X-Cache-TTL": "10",
    }
    if headers:
      request_headers.update(headers)
    return self.session.post(
      self.PROXY_URL.format(url=quote(target_url, safe="")),
      json=payload,
      headers=request_headers,
      timeout=self.TIMEOUT_SECONDS,
    )

  def _ip_to_u32(self, ip_address):
    value = 0
    for part in ip_address.split("."):
      value = ((value << 8) + int(part)) & 0xffffffff
    return value

  def _murmur_hash(self, value):
    value = str(value)
    remainder = len(value) & 3
    end = len(value) - remainder
    hash_value = 0
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    index = 0

    while index < end:
      key = (
        (ord(value[index]) & 0xff)
        | ((ord(value[index + 1]) & 0xff) << 8)
        | ((ord(value[index + 2]) & 0xff) << 16)
        | ((ord(value[index + 3]) & 0xff) << 24)
      )
      index += 4
      key = self._uint32_multiply(key, c1)
      key = ((key << 15) | (key >> 17)) & 0xffffffff
      key = self._uint32_multiply(key, c2)
      hash_value ^= key
      hash_value = ((hash_value << 13) | (hash_value >> 19)) & 0xffffffff
      mixed = self._uint32_multiply(hash_value, 5)
      hash_value = (
        (mixed & 0xffff)
        + 0x6b64
        + ((((mixed >> 16) + 0xe654) & 0xffff) << 16)
      ) & 0xffffffff

    key = 0
    tail = end
    if remainder == 3:
      key ^= (ord(value[tail + 2]) & 0xff) << 16
    if remainder >= 2:
      key ^= (ord(value[tail + 1]) & 0xff) << 8
    if remainder >= 1:
      key ^= ord(value[tail]) & 0xff
      key = self._uint32_multiply(key, c1)
      key = ((key << 15) | (key >> 17)) & 0xffffffff
      key = self._uint32_multiply(key, c2)
      hash_value ^= key

    hash_value ^= len(value)
    hash_value ^= hash_value >> 16
    hash_value = self._uint32_multiply(hash_value, 0x85ebca6b)
    hash_value ^= hash_value >> 13
    hash_value = self._uint32_multiply(hash_value, 0xc2b2ae35)
    hash_value ^= hash_value >> 16
    return hash_value & 0xffffffff

  def _uint32_multiply(self, value, multiplier):
    return (
      (value & 0xffff) * multiplier
      + ((((value >> 16) * multiplier) & 0xffff) << 16)
    ) & 0xffffffff


class SwimStandardsDataProvider(SwimmerSearchDataProvider):
  SWIMMERS_URL = "https://swimstandards.com/dnxapi/swimmers"
  HEADERS = {
    "User-Agent": (
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
  }

  def __init__(self, session=None):
    self.session = session or requests

  def search_swimmers(self, query, limit=20, skip=0) -> list[SwimmerProfile]:
    query = (query or "").strip()
    if not query:
      return []

    response = self.session.get(
      self.SWIMMERS_URL,
      params={
        "$search": query,
        "lsc": "",
        "$limit": limit,
        "$skip": skip,
      },
      headers=self.HEADERS,
    )
    response.raise_for_status()
    return [
      _swimmer_profile_from_entry(entry)
      for entry in _swimmer_entries_from_payload(response.json())
    ]
