import pdfplumber

def extract_agc(pdf_path):

    def _read_pdf(pdf_path):
      # Open the PDF file
      with pdfplumber.open(pdf_path) as pdf:
          all_tables = []

          # Iterate through each page
          for page_num, page in enumerate(pdf.pages):
              print(f"Processing page {page_num + 1}...")

              # Extract tables from the page
              tables = page.extract_tables()
              print(f"Total {len(tables)} tables")
              
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
          row = [event] + ['-'] * 3 + row[1:]
        elif event in ['50 BK', '50 BR', '50 FL']:
          # Those event not in 13 and 14
          row.extend(['-'] * 6)
        elif event in ['100 IM']:
          row.insert(2, '-')
          row.insert(5, '-')
          row.insert(8, '-')
          row.extend(['-'] * 6)

        rows.append(row)
      return rows


    def _to_json(lines, gender):
      jobj = {}
      ages2events = {
        'JO-10':  [
                    '50 Y Free', 
                    '100 Y Free',
                    '200 Y Free',
                    '500 Y Free'
                    '50 Y Back',
                    '100 Y Back',
                    '50 Y Breast',
                    '100 Y Breast',
                    '200 Y Breast',
                    '50 Y Fly',
                    '100 Y Fly',
                    '100 Y IM',
                    '200 Y IM',
                    '50 M Free',
                    '100 M Free',
                    '200 M Free',
                    '400 M Free',
                    '50 M Back',
                    '100 M Back',
                    '50 M Breast',
                    '100 M Breast',
                    '50 M Fly',
                    '100 M Fly',
                    '200 M IM',
                  ],
        'JO-11':  [
                    '50 Y Free',
                    '100 Y Free',
                    '200 Y Free',
                    '500 Y Free',
                    '1000 Y Free',
                    '1650 Y Free',
                    '50 Y Back',
                    '100 Y Back', 
                    '200 Y Back' ,
                    '50 Y Breast',
                    '100 Y Breast',
                    '200 Y Breast',
                    '50 Y Fly',
                    '100 Y Fly',  
                    '200 Y Fly', 
                    '100 Y IM', 
                    '200 Y IM',  
                    '400 Y IM',
                    '50 M Free',
                    '100 M Free',
                    '200 M Free',
                    '400 M Free',
                    '800 M Free',
                    '1500 M Free',
                    '50 M Back',
                    '100 M Back',
                    '200 M Back',
                    '50 M Breast',
                    '100 M Breast',
                    '200 M Breast',
                    '50 M Fly',
                    '100 M Fly',
                    '200 M Fly',
                    '200 M IM',
                    '400 M IM',
                  ],
        'JO-12':  [
                    '50 Y Free',
                    '100 Y Free',
                    '200 Y Free',
                    '500 Y Free',
                    '1000 Y Free',
                    '1650 Y Free',
                    '50 Y Back',
                    '100 Y Back', 
                    '200 Y Back' ,
                    '50 Y Breast',
                    '100 Y Breast',
                    '200 Y Breast',
                    '50 Y Fly',
                    '100 Y Fly',  
                    '200 Y Fly', 
                    '100 Y IM', 
                    '200 Y IM',  
                    '400 Y IM',
                    '50 M Free',
                    '100 M Free',
                    '200 M Free',
                    '400 M Free',
                    '800 M Free',
                    '1500 M Free',
                    '50 M Back',
                    '100 M Back',
                    '200 M Back',
                    '50 M Breast',
                    '100 M Breast',
                    '200 M Breast',
                    '50 M Fly',
                    '100 M Fly',
                    '200 M Fly',
                    '200 M IM',
                    '400 M IM',
                  ],
        'JO-13':  [
                    '50 Y Free',
                    '100 Y Free',
                    '200 Y Free',
                    '500 Y Free',
                    '1000 Y Free',
                    '1650 Y Free',
                    '100 Y Back', 
                    '200 Y Back' ,
                    '100 Y Breast',
                    '200 Y Breast',
                    '100 Y Fly',  
                    '200 Y Fly', 
                    '200 Y IM',  
                    '400 Y IM',
                    '50 M Free',
                    '100 M Free',
                    '200 M Free',
                    '400 M Free',
                    '800 M Free',
                    '1500 M Free',
                    '100 M Back',
                    '200 M Back',
                    '100 M Breast',
                    '200 M Breast',
                    '100 M Fly',
                    '200 M Fly',
                    '200 M IM',
                    '400 M IM',
                  ],
        'JO-14':  [
                    '50 Y Free',
                    '100 Y Free',
                    '200 Y Free',
                    '500 Y Free',
                    '1000 Y Free',
                    '1650 Y Free',
                    '100 Y Back', 
                    '200 Y Back' ,
                    '100 Y Breast',
                    '200 Y Breast',
                    '100 Y Fly',  
                    '200 Y Fly', 
                    '200 Y IM',  
                    '400 Y IM',
                    '50 M Free',
                    '100 M Free',
                    '200 M Free',
                    '400 M Free',
                    '800 M Free',
                    '1500 M Free',
                    '100 M Back',
                    '200 M Back',
                    '100 M Breast',
                    '200 M Breast',
                    '100 M Fly',
                    '200 M Fly',
                    '200 M IM',
                    '400 M IM',
                  ]
      }
      
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
          '100 M IM':     -1,
          '200 M IM':     16,
          '400 M IM':     17,
      }
      for line in lines:
        print(line)
      for age in ages2events:
        key = age + '-' + gender
        jobj[key] = {}
        for event in event2rowId:
          if event in ages2events[age]:
            # column offset = 1 + (age - 10) * 3 + o
            # o is 0 if SCY else 1
            offset = 1
            offset += (int(age[3:]) - 10) * 3
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

    boyslines = _process_lines(boyslines)
    girlslines = _process_lines(girlslines)
    
    import json
    print(json.dumps(_to_json(girlslines, gender='MALE'), indent=4))


if __name__ == '__main__':
  extract_agc(pdf_path="agc-time.pdf")