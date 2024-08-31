# TSV files in data/ are extracted using OCR from
# https://websitedevsa.blob.core.windows.net/sitefinity/docs/default-source/timesdocuments/time-standards/2025/2028-motivational-standards-age-group.pdf
def load_national_times(tsv_file):
  with open(tsv_file) as f:
    lines = f.readlines()
    headers = lines[0].split('\t')
    standards = [header.strip() for header in headers[1:]]
    timemap = {}
    for standard in standards:
      timemap[standard] = {}
    
    for line in lines[1:]:
      tokens = line.split('\t')
      event = tokens[0].strip()
      timemap[event] = {}
      for j in range(1, len(tokens)):
        timemap[headers[j].strip()][event] = tokens[j].strip()
  return timemap

national_timemap = {}
national_timemap['10-MALE'] = load_national_times('data/national_times_10_boys.tsv')
national_timemap['10-FEMALE'] = load_national_times('data/national_times_10_girls.tsv')
national_timemap['11-12-MALE'] = load_national_times('data/national_times_11_12_boys.tsv')
national_timemap['11-12-FEMALE'] = load_national_times('data/national_times_11_12_girls.tsv')
print(national_timemap)  # copy the output to times.py and format