## Service API

- Search Swimmer name, team 
    - `/search?q={:term}`

- Query One Qualifying Time + National Time + Multiple Swimmers

    - `/board?id=swimmer1,swimmer2&ts=JO-10-MALE`
    where swimmer1,swimmer2 are IDs from https://swimstandards.com/
    and JO-10-MALE is defined from times.py \
        example: /board?id=carlos-li,ian-sun&ts=FW_11_12_MALE

- Query One Swimmer + National Time + Multiple Qualifying Times

    - `/card?id=swimmer1&nt=10-MALE`
    where swimmer1 is an ID from https://swimstandards.com/
    and JO-10-MALE is defined from times.py \
        example: /card?id=carlos-li&nt=10-MALE

      

## Data Maintenance 

1.  Update time standards.
     - cd to root folder
     - run `uv run python -m data.timestandards.extract_national_time_pdf` and save the results to times.py > national_timemap

2.  Update Age Group Championship qualifying time.
     - cd to root folder
     - run `uv run python -m data.timestandards.extract_agc_time_pdf` and save the results to times.py > times_map

3.  Update Far Western Championship qualifying time.
     - cd to root folder
     - run `uv run python -m data.timestandards.extract_fw_time_pdf` and save the results to times.py > times_map

