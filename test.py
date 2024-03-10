# from utils import crawl_swimmers
# swimmers = []

# swimmers += crawl_swimmers('https://swimstandards.com/rankings/25fr-scy-8-male-pc_alto?target=2&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?target=12&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?target=12&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-male-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-male-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/25fr-scy-8-female-pc_alto?target=2&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-female-pc_alto?target=3&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-9-10-female-pc_alto?target=3&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-female-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=1')
# swimmers += crawl_swimmers('https://swimstandards.com/rankings/50fr-scy-11-12-female-pc_alto?target=5&u_season=2324&u_season_start=2023&u_season_end=2024&page=2')
# for swimmer in sorted(set(swimmers)):  
#   print(f"'{swimmer}',")

# from utils import ScoreBoard
# sb = ScoreBoard()
# sb.add_time_standards()
# sb.add_swimmer('carlos-li')#
# # records, rownames, colnames = sb.gen_report(format="records")
# # print(rownames)
# # print(colnames)
# # print()
# # print(records)

# df = sb.gen_report(format="dataframe")
# print(df)
# print(df.index.values)
# print(df.columns.values)
# print('-----\n')
# for k, v in enumerate(df.to_dict('records')):
#   print(k, v)



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

import flask
print(flask.__version__)

import flask_wtf
print(flask_wtf.__version__)

import wtforms
print(wtforms.__version__)
