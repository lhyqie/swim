## Service API

- Query One Qualifying Time + National Time + Multiple Swimmers

    1. `/board?id=swimmer1,swimmer2&ts=JO-10-MALE`
    where swimmer1,swimmer2 are IDs from https://swimstandards.com/
    and JO-10-MALE is defined from times.py
    
        example: /board?id=carlos-li,ian-sun&ts=FW_11_12_MALE

    2. `/compare` pick swimmer and enter more free-text swimmers and pick time standards from form.

        example: /compare


- Query One Swimmer + National Time + Multiple Qualifying Times

    1. `/card?id=swimmer1&nt=10-MALE`
    where swimmer1 is an ID from https://swimstandards.com/
    and JO-10-MALE is defined from times.py

        example: /card?id=carlos-li&nt=10-MALE

    2. `/swim` pick one swimmer and National Time from form.

        example: /swim
      

## Data Maintenance 

1.  Add swimmers in drop down list.

     - run `swimmers_crawl.py` and save the results to `swimmers.py`


2.  Update time standards.

     - update `data/*.csv` based on most recent timestandards
     - run `data/export.py` and save the results to times.py