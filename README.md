## Service API

- Search Swimmer name, team
    1. `/search?q={:term}`

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

1.  Update time standards.
     - update `data/*.csv` based on most recent timestandards
     - cd to root folder
     - run `python -m data.extract_agc_time_pdf` and save the results to times.py > times_map

2.  Update Age Group Championship qualifying time.
     - cd to root folder
     - run `python -m data.extract_national_time_pdf` and save the results to times.py > national_timemap

3.  Add swimmers to .py file which feeds into the drop down list.
     - cd to root folder
     - run `python -m data.crawl_swimmer_py and save the results to `swimmers.py`

4.  Add swimmer profile to .csv file and database.
    - cd to root folder
    - run `python -m data.crawl_swimmer_csv` to update `swimmer-profile-top1000-per-group.csv`
    - run `python -m data.build_swimmer_profile_db` to update `swimmer-profile.db`

