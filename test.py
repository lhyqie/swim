# -------------------- Test Crawler --------------------------
from utils import SwimStandardsCrawler, to_fastest
crawler = SwimStandardsCrawler()

# for event in crawler.crawl_fastest_time('https://swimstandards.com/swimmer/abby-chan'):
#   print(event)
all_events = crawler.crawl_all_events('https://swimstandards.com/swimmer/abby-chan')
for event in all_events:
  print(event)
print('----------------------------------------------------')
for event in to_fastest(all_events):
  print(event)

# swimmers = []
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/25fr-scy-8-male-pc_alto?target=2&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?target=12&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?target=12&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-male-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-male-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/25fr-scy-8-female-pc_alto?target=2&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-female-pc_alto?target=3&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-female-pc_alto?target=3&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-female-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawler.crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-female-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# for swimmer in sorted(set(swimmers)):  
#   print(f"'{swimmer}',")

# -------------------- Test EventStore --------------------------
# from utils import EventStore
# event_store = EventStore(sqldb_file='swimmers_test.db')
# for row in event_store.swimmer_fastest_time_from_db('abby-chan'):
#   print(row['id'], row['fastest_time'])
# print(event_store.swimmer_fastest_time_from_db('unknown-swimmer'))
# print()
# for event in event_store.swimmer_fastest_time('abby-chan', use_cache=True):
#   print(event)
# print()
# for event in event_store.swimmer_fastest_time('abby-chan', use_cache=False):
#   print(event)
# // Test update swimmer fastest times to db.
# events = event_store.swimmer_fastest_time('abby-chan', use_cache=False)
# for event in events:
#   print(event)
# event_store.swimmer_fastest_time_to_db('abby-chan', events)

# -------------------- Test ScoreBoard --------------------------
# from utils import ScoreBoard
# sb = ScoreBoard(time_standard='JO-10-MALE', national_time='10-MALE')
# sb.add_time_standards()
# sb.add_swimmer('abby-chan')
# records, rownames, colnames = sb.gen_report(format="records+nationaltime")
# print('rownames:', rownames)
# print('colnames:', colnames)
# print('records:', records)

# records, rownames, colnames = sb.gen_report(format="records")
# print('rownames:', rownames)
# print('colnames:', colnames)
# print('records:', records)

# df = sb.gen_report(format="dataframe")
# print(df)
# print(df.index.values)
# print(df.columns.values)
# for k, v in enumerate(df.to_dict('records')):
#   print(k, v)


# -------------------- Print Packages Version --------------------------
# import numpy
# print(numpy.__version__)

# import pandas
# print(pandas.__version__)

# import requests
# print(requests.__version__)

# import sys
# print(sys.version)

# import requests
# print(requests.__version__)

# import flask
# print(flask.__version__)

# import flask_wtf
# print(flask_wtf.__version__)

# import wtforms
# print(wtforms.__version__)

# import sqlite3
# print(sqlite3.version)

# from datetime import datetime
# date = datetime.strptime('2024-03-10 08:20:20','%Y-%m-%d %H:%M:%S')
# print(date)

# from datetime import datetime
# date2 = datetime.now()

# print(type(date2 - date))
# print((date2 - date))
