# From https://www.pacswim.org/userfiles/cms/documents/809/agc-time-std.-scy-2024-2025-rev-8.27.24.pdf
# NOTE: JO-14-MALE data has some noise. 
# Run this script and manually fix '50 Y Free' for JO-14-MALE

import json
import pdfplumber
import os
import requests

from data.common import ages2agcevents


def extract_agc(pdf_path):
    def _read_pdf(pdf_path):
      # Open the PDF file
      with pdfplumber.open(pdf_path) as pdf:
          all_tables = []

          # Iterate through each page
          for page_num, page in enumerate(pdf.pages):
              # print(f"Processing page {page_num + 1}...")

              # Extract tables from the page
              tables = page.extract_tables()
              # print(f"Total {len(tables)} tables")
              
              # If tables are found, add them to the list
              if tables:
                  for table in tables:
                      if table:
                          all_tables.extend(table)
      # content only extracted to all_tables[0][0]
      return all_tables[0][0]


    def _process_lines(lines):
      rows = []
      for line in lines:
        row = []
        tokens = line.split()
        event = tokens[0] + ' ' +tokens[1]
        # print(event)
        row.append(event)
        row.extend(tokens[2:])
        
        if event in ['800/1000 FR', '1500/1650 FR', '200 BK', '200 BR', '200 FL', '400 IM']:
          # Those event not in 10 & U
          row = [event] + [''] * 3 + row[1:]
        elif event in ['50 BK', '50 BR', '50 FL']:
          # Those event not in 13 and 14
          row.extend([''] * 6)
        elif event in ['100 IM']:
          row.insert(2, '')
          row.insert(5, '')
          row.insert(8, '')
          row.extend([''] * 6)

        rows.append(row)
      return rows


    def _to_json(lines, gender):
      jobj = {}
      
      # event mapped to row in pdf.
      # -1 means do not exist.
      event2rowId = {
          '25 Y Free':    -1,
          '50 Y Free':     0,
          '100 Y Free':    1,
          '200 Y Free':    2,
          '500 Y Free':    3,
          '1000 Y Free':   4,
          '1650 Y Free':   5,
          '25 Y Back':    -1,
          '50 Y Back':     6,
          '100 Y Back':    7,
          '200 Y Back':    8,
          '25 Y Breast':  -1,
          '50 Y Breast':   9,
          '100 Y Breast': 10,
          '200 Y Breast': 11,
          '25 Y Fly':     -1,
          '50 Y Fly':     12,
          '100 Y Fly':    13,
          '200 Y Fly':    14,
          '100 Y IM':     15,
          '200 Y IM':     16,
          '400 Y IM':     17,
          '50 M Free':     0,
          '100 M Free':    1,
          '200 M Free':    2,
          '400 M Free':    3,
          '800 M Free':    4,
          '1500 M Free':   5,
          '50 M Back':     6,
          '100 M Back':    7,
          '200 M Back':    8,
          '50 M Breast':   9,
          '100 M Breast': 10,
          '200 M Breast': 11,
          '50 M Fly':     12,
          '100 M Fly':    13,
          '200 M Fly':    14,
          '200 M IM':     16,
          '400 M IM':     17,
      }
      # for line in lines:
      #   print(line)
      for age in ages2agcevents:
        key = 'JO-' + age + '-' + gender
        jobj[key] = {}
        for event in event2rowId:
          if event in ages2agcevents[age]:
            # column offset = 1 + (age - 10) * 3 + o
            # o is 0 if SCY else 1
            offset = 1
            offset += (int(age) - 10) * 3
            if ' Y ' in event:
              offset += 0
            elif ' M ' in event:
              offset += 1
            else:
              raise Exception('Event is either yard or meter!')
            jobj[key][event] = lines[event2rowId[event]][offset]
          else:
            jobj[key][event] = ''
      return jobj
      

    table = _read_pdf(pdf_path)
    lines = table.split('\n')    
    # girls section from line 4 to line 21
    girlslines = lines[4:22]
    # boys section from line 25 to last
    boyslines = lines[25:]
    # print(girlslines)
    # print(boyslines)

    girlslines = _process_lines(girlslines)
    boyslines = _process_lines(boyslines)
    
    import json
    girls = _to_json(girlslines, gender='FEMALE')
    boys = _to_json(boyslines, gender='MALE')
    return {**girls, **boys}


if __name__ == '__main__':
  jobj = extract_agc(pdf_path='data/download-agc-time.pdf')
  print(json.dumps(jobj, indent=2))