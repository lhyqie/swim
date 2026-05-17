# -------------------- Test Crawler --------------------------
from data.swimmer_data_provider import SwimStandardsCrawler
from utils import to_fastest
crawler = SwimStandardsCrawler()

# for event in crawler.crawl_fastest_time('https://swimstandards.com/swimmer/abby-chan'):
#   print(event)
all_events, gender, age = crawler.crawl_all_events('https://swimstandards.com/swimmer/abby-chan')
print('gender is:', gender, ' age is: ', age)
for event in all_events:
  print(event)
print('----------------------------------------------------')
for event in to_fastest(all_events):
  print(event)

# -------------------- Test DataProvider --------------------------
# from data.swimmer_data_provider import SwimStandardsDataProvider
# data_provider = SwimStandardsDataProvider()
# events, gender, age, swimmer_display_name = data_provider.swimmer_fastest_time('abby-chan')
# print(gender, age)
# for event in events:
#   print(event)

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

# from datetime import datetime
# date = datetime.strptime('2024-03-10 08:20:20','%Y-%m-%d %H:%M:%S')
# print(date)

# from datetime import datetime
# date2 = datetime.now()

# print(type(date2 - date))
# print((date2 - date))
