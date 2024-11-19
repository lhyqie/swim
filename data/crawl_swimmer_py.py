from utils import SwimStandardsCrawler

crawler = SwimStandardsCrawler()

urls = [
  # Male
  'https://swimstandards.com/rankings/25fr-scy-8-male-pc_alto?page=1',
  'https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?page=1',
  'https://swimstandards.com/rankings/50fr-scy-9-10-male-pc_alto?page=2',
  'https://swimstandards.com/rankings/50fr-scy-11-12-male-pc_alto?page=1',
  'https://swimstandards.com/rankings/50fr-scy-11-12-male-pc_alto?page=2',
  
  # Female
  'https://swimstandards.com/rankings/25fr-scy-8-female-pc_alto?page=1',
  'https://swimstandards.com/rankings/50fr-scy-9-10-female-pc_alto?page=1',
  'https://swimstandards.com/rankings/50fr-scy-9-10-female-pc_alto?page=2',
  'https://swimstandards.com/rankings/50fr-scy-11-12-female-pc_alto?page=1',
  'https://swimstandards.com/rankings/50fr-scy-11-12-female-pc_alto?page=2',
]

swimmers = []
for url in urls:
  swimmers += crawler.crawl_swimmers(url)

for swimmer in sorted(set(swimmers)):  
  print(f"'{swimmer}',")
