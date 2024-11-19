# Note:
#
#   1. Inspect Web page https://swimstandards.com/rankings, we can find the API endpoint `get-rankings` under the `Network` tab.
#      example:  https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_8_Female.json
# 
#   2. in https://swimstandards.com/, type a query in the search box and inspect similarly and find API endpoint for swimmer search 
#      example for search swimmer name and team:  https://api.swimstandards.com/swimmers?$search=Alto%20Swim%20Club&lsc=&$limit=20&$skip=0
#      example for search meet name:  https://api.swimstandards.com/meets?$search=Alto%20Swim%20Club&$limit=20&$skip=0
#      example for search time-standards:  https://api.swimstandards.com/time-standards/?$search=age&$limit=20&$skip=0

# Crawl top 1000 swimmers from 50Y FR

import csv
import requests
import json

from data.schema import SwimmerProfile

urls = [
  # Female
  'https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_8_Female.json',
  'https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_9-10_Female.json',
  'https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_11-12_Female.json',
  
  # Male
  'https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_8_Male.json',
  'https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_9-10_Male.json',
  'https://swimstandards.com/api/get-rankings?folder=bigranks2425&filename=usa_50FR_SCY_11-12_Male.json',
]

def craw_one_page(url):
  swimmers = []
  
  response = requests.get(url)
  entries = json.loads(response.content)['data']
  for entry in entries:
    id = entry['slug']
    name = entry['name'].strip().replace(',', '')  # remove `,` in some team names
    name_tokens = name.split()
    firstname = name_tokens[0]
    lastname = ''.join(name_tokens[1:])
    team = entry['swimTeam'].strip().replace(',', '').replace('|', '')  # remove `,` and `|` in some team names
    age = entry['age']
    gender = entry['sex']
    swimmer = SwimmerProfile(id=id, firstname=firstname, lastname=lastname, team=team, age=age, gender=gender)
    swimmers.append(swimmer)
  return swimmers


def write_to_csv(swimmers, csv_file):
  with open(csv_file, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      writer.writerow(['id', 'firstname', 'lastname', 'team', 'age', 'gender'])
      for s in swimmers:
        writer.writerow([s.id, s.firstname, s.lastname, s.team, s.age, s.gender])


def dedup(swimmers):
  # Sometime same swimmer has entries of two ages due to age-up.
  id2age= {}
  dedup_swimmers = []
  swimmers.sort(key=lambda x: -int(x.age))  # sort by age DESC
  for swimmer in swimmers:
    if swimmer.id not in id2age:
      id2age[swimmer.id] = int(swimmer.age)
      dedup_swimmers.append(swimmer)
  return dedup_swimmers


def crawl_top_1000():
  swimmers = []
  for url in urls:
    # 200 results per page
    for start in [0, 200, 400, 600, 800]:
      url_with_offset = url+f'&start={start}'
      print('crawling', url_with_offset)
      swimmers += craw_one_page(url_with_offset)
      print('crawled', len(swimmers), 'swimmers')
  print(f'total swimmers: {len(swimmers)}')
  print('remove duplicated swimmers who aged up (keep older age)')
  swimmers = dedup(swimmers)
  print(f'total swimmers: {len(swimmers)}')
  write_to_csv(swimmers=swimmers,csv_file='data/swimmer-profile-top1000-per-group.csv')


def crawl_alto():
  # TODO: crawl alto swimmers and save to `swimmer-profile-alto.csv`
  pass

if __name__ == '__main__':
  crawl_top_1000()
  crawl_alto()
