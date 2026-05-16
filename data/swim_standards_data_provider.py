from abc import ABC, abstractmethod
from dataclasses import dataclass

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
      SwimmerProfile(
        slug=entry.get("slug", ""),
        name=entry.get("name", ""),
        sex=entry.get("sex", ""),
        age=entry.get("age", 0),
        team=entry.get("team") or entry.get("swimTeam", ""),
      )
      for entry in response.json().get("data", [])
    ]
