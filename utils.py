import json
import requests
from bs4 import BeautifulSoup
from times import times_map

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
  def __init__(self):
    self.event_name = ''
    self.time = ''
    self.age = ''
    self.swim_meet = ''
    self.date = ''

  def __str__(self):
    # return f'{self.event_name:12s} ({self.age}) | {self.time:7s} | {self.date} | {self.swim_meet}'
    # return f'{self.event_name:12s} ({self.age}) | {self.time:7s}'
    return f'{self.event_name:12s} | {self.time:7s}'


def crawl_all_events(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  jobj = json.loads(soup.select('script')[-1].string)
  data = jobj['props']['pageProps']['swimmer']['records']['data']

  events = []
  for elem in data:
    event = Event(elem)
    events.append(event)
  return events


def crawl_fastest_time(url):
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
  column_names = ['Event', 'Time', 'Standards', 'Points', 'Age', 'Meet', 'Meet Date']
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
def crawl_swimmers(team_url):
  response = requests.get(team_url)
  soup = BeautifulSoup(response.content, 'html.parser')
  table = soup.select('table[id=all-results-table]')
  subtabs = []
  result = table[0].tbody.select('a')
  if len(result) > 0:
    for a in result:
      swimmer = a['href'].split('/')[-1]
      yield swimmer


# events = crawl_all_events('https://swimstandards.com/swimmer/carlos-li')
# for event in events:
#   print(event)
# events = crawl_fastest_time('https://swimstandards.com/swimmer/carlos-li')
# for event in events:
#   print(event)

class ScoreBoard:
  def __init__(self, time_standard) -> None:
    self.board = []
    self.swimmers = []
    self.time_standard = time_standard

  def add_time_standards(self):
    self.board.append(times_map[self.time_standard])
    self.swimmers.append(self.time_standard)

  def add_swimmer(self, swimmer_id):
    column = {}
    events = crawl_fastest_time('https://swimstandards.com/swimmer/' + swimmer_id)
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
