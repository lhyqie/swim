# From https://websitedevsa.blob.core.windows.net/sitefinity/docs/default-source/timesdocuments/time-standards/2025/2028-motivational-standards-age-group.pdf

import json
import pdfplumber

from data.common import full_event_list


event_map = {
  '50 FR SCY'  : '50 Y Free',
  '100 FR SCY' : '100 Y Free',
  '200 FR SCY' : '200 Y Free',
  '500 FR SCY' : '500 Y Free',
  '1000 FR SCY': '1000 Y Free',
  '1650 FR SCY': '1650 Y Free',
  '50 BK SCY'  : '50 Y Back',
  '100 BK SCY' : '100 Y Back',
  '200 BK SCY' : '200 Y Back',
  '50 BR SCY'  : '50 Y Breast',
  '100 BR SCY' : '100 Y Breast',
  '200 BR SCY' : '200 Y Breast',
  '50 FL SCY'  : '50 Y Fly',
  '100 FL SCY' : '100 Y Fly',
  '200 FL SCY' : '200 Y Fly',
  '100 IM SCY' : '100 Y IM',
  '200 IM SCY' : '200 Y IM',
  '400 IM SCY' : '400 Y IM',
  '50 FR LCM'  : '50 M Free',
  '100 FR LCM' : '100 M Free',
  '200 FR LCM' : '200 M Free',
  '400 FR LCM' : '400 M Free',
  '800 FR LCM' : '800 M Free',
  '1500 FR LCM': '1500 M Free',
  '50 BK LCM'  : '50 M Back',
  '100 BK LCM' : '100 M Back',
  '200 BK LCM' : '200 M Back',
  '50 BR LCM'  : '50 M Breast',
  '100 BR LCM' : '100 M Breast',
  '200 BR LCM' : '200 M Breast',
  '50 FL LCM'  : '50 M Fly',
  '100 FL LCM' : '100 M Fly',
  '200 FL LCM' : '200 M Fly',
  '200 IM LCM' : '200 M IM',
  '400 IM LCM' : '400 M IM',
}
 
   
def extract_national(pdf_path):
  def _read_pdf(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        all_pages = []

        # Iterate through each page
        for page_num, page in enumerate(pdf.pages):
            print(f"Processing page {page_num + 1}...")

            lines = page.extract_text()
            all_pages.append(lines)
    return all_pages


  def _process_lines(jobj, lines, age, mode='scy'):
    standards = ['AAAA', 'AAA', 'AA', 'A', 'BB', 'B']
    boy = { s:{} for s in standards }
    girl = { s:{} for s in standards }
    
    for line in lines:
      # print(repr(line))
      tokens = line.replace('*', '').split()
      tokens = [token.strip() for token in tokens if token.strip()]
      # print(tokens)
      
      # Girls B, BB, A, AA, AAA, AAAA from offset [0, 6)
      tokens_girl = tokens[0:6]
      tokens_girl = tokens_girl[::-1]  # reverse it so the order is from AAAA to B
      # Boys AAA, AA, A, BB, B from offset reverse of [9, ... )
      tokens_boy = tokens[9:]
      
      # middle token is tokens[6:9] cotains event name as Boys AAAA
      middle_tokens = ' '.join(tokens[6:9]).replace('-', ' ').split()
      event = (' '.join(middle_tokens[:3]))
      if event.endswith(" R"):
        continue  # relay time skipped
      
      # print(event)
      # print(tokens_girl)
      # print(tokens_boy)
      event = event_map[event]
      
      for i, s in enumerate(standards):
        girl[s][event] = tokens_girl[i]
        boy[s][event] = tokens_boy[i]
    
    # use `girl`, `boy` to construct `jobj``
    # print(girl)
    # print(boy)

    
    for s in standards:
      jobj[age + '-MALE'].setdefault(s, {})
      jobj[age + '-FEMALE'].setdefault(s, {})
      for event in full_event_list:
        if mode == 'scy':
          if not ' Y ' in event:
            continue
        elif mode == 'lcm':
          if not ' M ' in event:
            continue
        jobj[age + '-FEMALE'][s][event] = girl[s].get(event, "")
        jobj[age + '-MALE'][s][event] = boy[s].get(event, "")


  all_pages = _read_pdf(pdf_path)
  jobj = {}

  # Handle SCY
  age2lines_scy = {
    '10': {
      'page': 0,
      'start': 4,
      'end': 18,
    },
    '11-12': {
      'page': 0,
      'start': 20,
      'end': 44,
    },
    '13-14': {
      'page': 1,
      'start': 4,
      'end': 28,
    }
  }
  # Handle LCM
  age2lines_lcm = {
    '10': {
      'page': 5,
      'start': 26,
      'end': 39,
    },
    '11-12': {
     'page': 6,
     'start': 4,
     'end': 27,
    },
    '13-14': {
      'page': 7,
      'start': 4,
      'end': 27,
    }
  }

  for age in age2lines_scy:
    jobj[age + '-FEMALE'] = {}
    jobj[age + '-MALE'] = {}
    # handle SCY
    page = all_pages[age2lines_scy[age]['page']]
    lines = page.split('\n')[age2lines_scy[age]['start']:age2lines_scy[age]['end']]
    lines = [line for line in lines if len(line) > 10] # some short lines are caused by overflowing event names
    _process_lines(jobj, lines, age, mode='scy')
    # handle LCM
    page = all_pages[age2lines_lcm[age]['page']]
    lines = page.split('\n')[age2lines_lcm[age]['start']:age2lines_lcm[age]['end']]
    lines = [line for line in lines if len(line) > 10] # some short lines are caused by overflowing event names
    _process_lines(jobj, lines, age, mode='lcm')


  return jobj

if __name__ == '__main__':
  jobj = extract_national("data/download-national-time.pdf")
  print(json.dumps(jobj, indent=2))
