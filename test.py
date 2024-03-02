from utils import ScoreBoard

sb = ScoreBoard()
sb.add_time_standards()
sb.add_swimmer('carlos-li')#
# records, rownames, colnames = sb.gen_report(format="records")
# print(rownames)
# print(colnames)
# print()
# print(records)

df = sb.gen_report(format="dataframe")
print(df)
print(df.index.values)
print(df.columns.values)
print('-----\n')
for k, v in enumerate(df.to_dict('records')):
  print(k, v)

# import numpy
# print(numpy.__version__)

# import pandas
# print(pandas.__version__)

import requests
print(requests.__version__)

# import sys
# print(sys.version)
  
