import json
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from flask import session
from times import national_timemap,times_map,times_name_pair,time_name_fits_age_gender
from typing import List


class Event:
  def __init__(self, entry):
    self.swimmer_name = entry['name']
    self.sex = entry['sex']
    self.event_name = entry['event']
    self.type = entry['type']
    self.date = entry['date']
    self.age = entry['age']
    self.time = entry['time']
    self.standard = entry['standard']
    self.power_points = entry['powerPoints']
    self.swim_meet = entry['swimMeet']

  def __str__(self):
    return f'{self.date} | {self.swimmer_name} ({self.age}) | {self.event_name:8s} {self.type} | {self.time:7s} ({self.standard:2s}) | {self.swim_meet}'


class FastestEvent:
  def __init__(self, event_name='', time=''):
    self.event_name = event_name
    self.time = time
    # self.age = ''
    # self.swim_meet = ''
    # self.date = ''

  def __str__(self):
    # return f'{self.event_name:12s} ({self.age}) | {self.time:7s} | {self.date} | {self.swim_meet}'
    # return f'{self.event_name:12s} ({self.age}) | {self.time:7s}'
    return f'{self.event_name:12s} | {self.time:7s}'


def national_time_standard(event:str, timestr:str, national_timemap) -> str:
    def _toSeconds(timestr):
      seconds = 0
      tokens = timestr.split('.')
      if len(tokens) == 2:
        seconds += int(tokens[1]) / 100
      parts = tokens[0].split(':')
      if len(parts) == 2:
        seconds += (int(parts[0]) if parts[0] else 0) * 60 + (int(parts[1]) if parts[1] else 0)
      else:
        seconds += int(parts[0]) if parts[0] else 0
      return seconds;

    res = "<B"
    for standard in ['B', 'BB', 'A', 'AA', 'AAA', 'AAAA']:
      standard_timestr = national_timemap[standard].get(event,'')
      if not standard_timestr or not timestr: return ''
      if _toSeconds(timestr) <= _toSeconds(standard_timestr):
        res = standard
      else:
        break
    return res


def to_fastest(events: List[Event]) -> List[FastestEvent]:
  from collections import defaultdict
  from functools import cmp_to_key
  def compare_time(time1: str, time2: str) -> int:
      if time1 == '' or time2 == '': return False
      try:
        timeint1 = int(time1.replace(':','').replace('.',''))
        timeint2 = int(time2.replace(':','').replace('.',''))
      except ValueError:
        return False
      return timeint1 - timeint2
  
  def compare_event_name(e1: FastestEvent, e2: FastestEvent) -> int:
    # find the first non-numeric character
    p = 0
    en1 = e1.event_name
    en2 = e2.event_name
    for i, ch in enumerate(en1):
      if not ch.isnumeric():
        p = i
        break
    length1 = en1[:p]
    type1, style1 = en1[p:].split()
    for i, ch in enumerate(en2):
      if not ch.isnumeric():
        p = i
        break
    length2 = en2[:p]
    type2, style2 = en2[p:].split()
    
    if type1 != type2:
      return ord(type2) - ord(type1) # 'Y' first, 'M' later
    if style1 == style2:
      return (int)(length1) - (int)(length2)
    else:
      orderMap = {
        'Free' : 0,
        'Back' : 1,
        'Breast' : 2,
        'Fly' : 3,
        'IM' : 4,
      }
      return orderMap[style1] - orderMap[style2]

  # For example: convert "100FL" + "SCY" to "100 Y Fly"
  def convert_event_name_type(event_name, event_type) -> str:
    # find the first non-numeric character
    p = 0
    for i, ch in enumerate(event_name):
      if not ch.isnumeric():
        p = i
        break
    chunk1 = event_name[:p]
    chunk2 = event_name[p:]
    nameMap = {
      'FR': 'Free',
      'FL': 'Fly',
      'IM': 'IM',
      'BK': 'Back',
      'BR': 'Breast'
    }
    typeMap = {
      'SCY' : 'Y',
      'LCM' : 'M',
    }
    if chunk1 == "400500" and event_type == "SCY":
      chunk1 = "500"
    elif chunk1 == "400500" and event_type == "LCM":
      chunk1 = "400"
    elif chunk1 == "8001000" and event_type == "SCY":
      chunk1 = "1000"
    elif chunk1 == "8001000" and event_type == "LCM":
      chunk1 = "800"
    elif chunk1 == "15001650" and event_type == "SCY":
      chunk1 = "1650"
    elif chunk1 == "15001650" and event_type == "LCM":
      chunk1 = "1500"
    elif int(chunk1) > 400:
      print(chunk1)
      raise Exception(f"unknown event name {chunk1} for {event_type}")

    return f"{chunk1} {typeMap[event_type]} {nameMap[chunk2]}"
    
  e2t = defaultdict(list)
  for event in events:
    # remove time that is invalid: "00.00"
    if event.time == "00.00":
      continue
    try:
      e2t[convert_event_name_type(event.event_name, event.type)].append(event.time)
    except Exception:
      print(event)
    
  fastest_events = []
  for event_name, events in e2t.items():
    events.sort(key=cmp_to_key(compare_time))
    fastest_events.append(FastestEvent(event_name, events[0]))
  fastest_events.sort(key=cmp_to_key(compare_event_name))
  return fastest_events

class SwimStandardsCrawler:
  def __init__(self):
    pass

  # for example swimmer url: https://swimstandards.com/swimmer/abby-chan
  def crawl_all_events(self, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobj = json.loads(soup.select('script')[-1].string)
    swimmer_data = jobj['props']['pageProps']['swimmer']
    gender = swimmer_data['sex']
    age = swimmer_data['age']
    events = []
    for elem in swimmer_data['records']['data']:
      event = Event(elem)
      events.append(event)
    return events, gender, age

  # for example swimmer url: https://swimstandards.com/swimmer/abby-chan
  def crawl_fastest_time(self, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tabs = soup.select('div[class=swimmer-tabs]')
    subtabs = []
    for tab in tabs:
      subtabs.extend(tab.select('div[class~=active]'))

    data = []
    for tab in subtabs:
      rows = tab.table.tbody.find_all('tr') if tab.table else []
      for row in rows:
        tds = row.find_all('td')
        data_row = []
        for ele in tds:
          cell = ele.get_text('|').strip()
          data_row.append(cell)
        data.append(data_row)
      break

    events = []
    column_names = ['Event', 'Time', 'Standard', 'Points', 'Age', 'Meet', 'Meet Date']
    for row in data:
      event = FastestEvent()
      for i, cell in enumerate(row):
        if column_names[i] in ['Event', 'Time', 'Age', 'Meet', 'Meet Date']:
          cell = (cell.rstrip('|').lstrip(column_names[i]+'|'))
          if column_names[i] == 'Event':
            event.event_name = cell
          elif column_names[i] == 'Time':
            event.time = cell
          elif column_names[i] == 'Age':
            event.age = cell
          elif column_names[i] == 'Meet':
            event.swim_meet = cell
          elif column_names[i] == 'Meet Date':
            event.date = cell
      events.append(event)
    return events

  # for example team url:
  # https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?target=12&u_season=2324&u_season_start=2023&u_season_end=2024
  def crawl_swimmers(self, team_url):
    response = requests.get(team_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.select('table[id=all-results-table]')
    subtabs = []
    result = table[0].tbody.select('a')
    if len(result) > 0:
      for a in result:
        swimmer = a['href'].split('/')[-1]
        yield swimmer

class EventStore:
  def __init__(self, sqldb_file):
    self.crawler = SwimStandardsCrawler()
    self.sqldb_file = sqldb_file
    self.db_cache_expiry = timedelta(hours=6)
    self.event_delim = '|'
    self.event_time_delim = '-'

  def swimmer_fastest_time(self, swimmer_id, use_cache=True):
    gender = 'Male'
    age = '10'
    from_db = self.swimmer_fastest_time_from_db(swimmer_id)
    if use_cache and len(from_db) > 0: 
      cache_datetime = datetime.strptime(from_db[0]['crawl_date'], '%Y-%m-%d %H:%M:%S')
      if (datetime.now() - cache_datetime) < self.db_cache_expiry:
        events = []
        for elem in from_db[0]['fastest_time'].strip().split(self.event_delim):
          event = FastestEvent()
          tokens = elem.split(self.event_time_delim)
          event.event_name = tokens[0].strip()
          event.time = tokens[1].strip()
          events.append(event)
        return events, gender, age

    # events = self.crawler.crawl_fastest_time('https://swimstandards.com/swimmer/' + swimmer_id)
    try:
      events, gender, age = self.crawler.crawl_all_events('https://swimstandards.com/swimmer/' + swimmer_id)
      events = to_fastest(events)
    except KeyError:
      return []
    # use live fetched stats to database.
    self.swimmer_fastest_time_to_db(swimmer_id, events)
    return events, gender, age

  def swimmer_fastest_time_from_db(self, swimmer_id):
    conn = self._get_db_connection()
    swimmers = conn.execute(f'SELECT * FROM swimmers WHERE id="{swimmer_id}"').fetchall()
    conn.close()
    return swimmers
  
  def swimmer_fastest_time_to_db(self, swimmer_id, events):
    event_str = self.event_delim.join([f'{event.event_name}{self.event_time_delim}{event.time}' for event in events])
    if not event_str: return
    conn = self._get_db_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM swimmers WHERE id='{swimmer_id}'")
    cur.execute(f"INSERT INTO swimmers (id, fastest_time) VALUES ('{swimmer_id}', '{event_str}')")
    conn.commit()
    conn.close()

  def _get_db_connection(self):
    conn = sqlite3.connect(self.sqldb_file)
    conn.row_factory = sqlite3.Row
    return conn

# A score board is to represent one timestand and optional national time and muliple swimmers.
class ScoreBoard:
  def __init__(self, time_standard, national_time) -> None:
    self.board = []
    self.swimmers = []
    self.time_standard = time_standard
    self.national_time = national_time
    self.event_store = EventStore('swimmers.db')

  def add_time_standards(self):
    self.board.append(times_map[self.time_standard])
    self.swimmers.append(self.time_standard)

  def add_swimmer(self, swimmer_id):
    column = {}
    events, gender, age = self.event_store.swimmer_fastest_time(swimmer_id, use_cache=False)
    for event in events:
      column[event.event_name] = event.time
    self.board.append(column)
    self.swimmers.append(swimmer_id)

  def gen_report(self, format='dataframe'):
    if format == 'dataframe':
      import numpy as np
      import pandas as pd
      df = pd.DataFrame.from_dict(self.board).T
      df.columns = self.swimmers
      return df.replace(np.nan, '')
    elif format == 'records':
      rownames = [k for k, _ in self.board[0].items()]
      colnames = self.swimmers
      records = []
      for rowname in rownames:
        time_map = {}  # for each row (event), record the fastest time per swimmer
        for i, swimmer in enumerate(self.swimmers):
          time_map[swimmer] = self.board[i].get(rowname,'')
        records.append(time_map)
      return (records, rownames, colnames)
    elif format == 'records+nationaltime':
      rownames = [k for k, _ in self.board[0].items()]
      colnames = []
      for i, swimmer in enumerate(self.swimmers):
        colnames.append(swimmer)
        if i > 0: colnames.append(swimmer+'@nt')
      records = []
      for rowname in rownames:
        time_map = {}  # for each row (event), record the fastest time per swimmer
        for i, swimmer in enumerate(self.swimmers):
          time_map[swimmer] = self.board[i].get(rowname,'')
          if i > 0: time_map[swimmer+'@nt'] = national_time_standard(
            event=rowname, timestr=time_map[swimmer], national_timemap=national_timemap[self.national_time])
        records.append(time_map)
      return (records, rownames, colnames)
    elif format == 'json':
      from json2html import convert
      jobj = {}
      for swimmer_id, events in zip(self.swimmers, self.board):
        jobj[swimmer_id] = events
      # return json.dumps(jobj)
      return convert(json=jobj)
    elif format == 'dict':
      jobj = {}
      for swimmer_id, events in zip(self.swimmers, self.board):
        jobj[swimmer_id] = events
      return jobj
    else:
      return f'format {format} is not supported'

  
# A score card is to represent one swimmer, his/her national time and all timestandards.
class ScoreCard:
  def __init__(self, swimmer, nationaltime) -> None:
    self.board = []
    self.swimmer = swimmer
    self.swimmers = []
    self.national_time = nationaltime
    self.event_store = EventStore('swimmers.db')
    self.gender = 'Male'
    self.age = '10'
    # the first column is swimmmer, the next columns are time standards.
    self._add_swimmer_to_board()    
    self._add_all_time_standards_to_board()

  def _add_swimmer_to_board(self):
    if not self.swimmer: return
    self.swimmers.append(self.swimmer)
    column = {}
    events, gender, age = self.event_store.swimmer_fastest_time(self.swimmer, use_cache=False)
    self.gender = gender
    self.age = age
    for event in events:
      column[event.event_name] = event.time
    self.board.append(column)

  def _add_all_time_standards_to_board(self):
    # filter times by gender
    for times_name, _ in times_name_pair:
      if times_name.endswith(f'-{self.gender.upper()}'):
        self.board.append(times_map[times_name])
        self.swimmers.append(times_name)

  def gen_report(self, filter_column_by_age_gender=True, filter_25y_by_age=True):    
    if not self.swimmer: return [], [], []
    # if national time not specified, infer it from swimmer's age and gender.
    if self.national_time == '':
      if self.age <= 10:
        self.national_time += "10-" + self.gender.upper()
      elif 11<= self.age <= 12:
        self.national_time += "11-12-" + self.gender.upper()
      elif 13<= self.age <= 14:
        self.national_time += "13-14-" + self.gender.upper()
      else:
        self.national_time = '10-MALE'
    rownames = [k for k, _ in self.board[1].items()]
    # remove 25 Y when swimmer is more than 8 year old.
    if filter_25y_by_age and self.age > 8:
      rownames = [rowname for rowname in rownames if not rowname.startswith('25 Y')]
    colnames = []
    for i, swimmer in enumerate(self.swimmers):
      if (i == 0 or  # real swimer id column
          not filter_column_by_age_gender or 
          time_name_fits_age_gender(time_name=swimmer, age=self.age, gender=self.gender)
      ):
        colnames.append(swimmer)
      if i == 0: colnames.append(swimmer+'@nt')
    records = []
    for rowname in rownames:
      time_map = {}  # for each row (event), record the fastest time per swimmer
      for i, swimmer in enumerate(self.swimmers):
        time_map[swimmer] = self.board[i].get(rowname,'')
        if i == 0 and self.national_time: 
          time_map[swimmer+'@nt'] = national_time_standard(
          event=rowname, timestr=time_map[swimmer], national_timemap=national_timemap[self.national_time])
        
      records.append(time_map)
    return (records, rownames, colnames)
