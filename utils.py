from data.swimmer_data_provider import Event, FastestEvent
from times import national_timemap,times_map,times_name_pair,time_name_fits_age_gender
from typing import List


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

# A score board is to represent one timestand and optional national time and muliple swimmers.
class ScoreBoard:
  def __init__(self, time_standard, national_time, data_provider=None) -> None:
    self.board = []
    self.swimmers = []
    self.swimmer_ids = []
    self.colids = []
    self.time_standard = time_standard
    self.national_time = national_time
    self.data_provider = data_provider

  def add_time_standards(self):
    self.board.append(times_map[self.time_standard])
    self.swimmers.append(self.time_standard)
    self.swimmer_ids.append(self.time_standard)

  def add_swimmer(self, swimmer_id):
    column = {}
    events, gender, age, swimmer_display_name = self.data_provider.swimmer_fastest_time(swimmer_id)
    for event in events:
      column[event.event_name] = event.time
    self.board.append(column)
    self.swimmers.append(self._swimmer_label(swimmer_id, swimmer_display_name))
    self.swimmer_ids.append(swimmer_id)

  def _swimmer_label(self, swimmer_id, swimmer_display_name):
    label = swimmer_display_name or swimmer_id
    if label in self.swimmers:
      return f"{label} ({swimmer_id})"
    return label

  def gen_report(self, format='dataframe'):
    if format == 'dataframe':
      import numpy as np
      import pandas as pd
      df = pd.DataFrame.from_dict(self.board).T
      df.columns = self.swimmers
      self.colids = list(self.swimmer_ids)
      return df.replace(np.nan, '')
    elif format == 'records':
      rownames = [k for k, _ in self.board[0].items()]
      colnames = self.swimmers
      self.colids = list(self.swimmer_ids)
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
      self.colids = []
      for i, swimmer in enumerate(self.swimmers):
        colnames.append(swimmer)
        self.colids.append(self.swimmer_ids[i])
        if i > 0:
          colnames.append(swimmer+'@nt')
          self.colids.append('')
      records = []
      for rowname in rownames:
        time_map = {}  # for each row (event), record the fastest time per swimmer
        for i, swimmer in enumerate(self.swimmers):
          time_map[swimmer] = self.board[i].get(rowname,'')
          if i > 0: time_map[swimmer+'@nt'] = national_time_standard(
            event=rowname, timestr=time_map[swimmer], national_timemap=national_timemap[self.national_time])
        records.append(time_map)
      return (records, rownames, colnames)
    elif format == 'dict':
      jobj = {}
      for swimmer_id, events in zip(self.swimmers, self.board):
        jobj[swimmer_id] = events
      return jobj
    else:
      return f'format {format} is not supported'

  
# A score card is to represent one swimmer, his/her national time and all timestandards.
class ScoreCard:
  def __init__(self, swimmer, nationaltime, data_provider=None) -> None:
    self.board = []
    self.swimmer = swimmer
    self.swimmers = []
    self.national_time = nationaltime
    self.data_provider = data_provider
    self.gender = 'Male'
    self.age = 10
    # the first column is swimmmer, the next columns are time standards.
    self._add_swimmer_to_board()    
    self._add_all_time_standards_to_board()

  def _add_swimmer_to_board(self):
    if not self.swimmer: return
    column = {}
    events, gender, age, swimmer_display_name = self.data_provider.swimmer_fastest_time(self.swimmer)
    self.swimmers.append(swimmer_display_name or self.swimmer)
    if gender is not None:
      self.gender = gender
    if age is not None:
      self.age = int(age)
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
