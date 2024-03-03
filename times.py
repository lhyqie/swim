# From https://www.pacswim.org/userfiles/cms/documents/809/agc-time-std.-scy-2023-2024-rev-9.18.23.pdf
# and https://www.pacswim.org/userfiles/cms/documents/859/fw-time-std.---spring-2024-rev-8.25.23.pdf

times_name_pair = [
  ("JO_10_MALE",     "Age Group Championship (Junior Olympics) 10 and Under Men"), 
  ("JO_10_FEMALE",   "Age Group Championship (Junior Olympics) 10 and Under Women"),
  ("JO_11_MALE",     "Age Group Championship (Junior Olympics) 11 Men"), 
  ("JO_11_FEMALE",   "Age Group Championship (Junior Olympics) 11 Women"), 
  ("FW_10_MALE",     "Far Western 10 and Under Men"),
  ("FW_10_FEMALE",   "Far Western 10 and Under Women"),
  ("FW_11_12_MALE",  "Far Western 11-12 Men"),
  ("FW_11_12_FEMALE",  "Far Western 11-12 Women"),
]

times_map = {
  'JO_10_MALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "30.99",
    '100 Y Free'    : "1:09.69",
    '200 Y Free'    : "2:29.39",
    '500 Y Free'    : "6:37.09",
    '1000 Y Free'   : "",
    '1650 Y Free'   : "",
    '25 Y Back'     : "",
    '50 Y Back'     : "36.99",
    '100 Y Back'    : "1:18.89",
    '200 Y Back'    : "",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "40.99",
    '100 Y Breast'  : "1:28.99",
    '200 Y Breast'  : "",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "35.39",
    '100 Y Fly'     : "1:22.69",
    '200 Y Fly'     : "",
    '100 Y IM'      : "1:18.89",
    '200 Y IM'      : "2:50.99",
    '400 Y IM'      : "",

    '50 M Free'     : "35.49",
    '100 M Free'    : "1:19.49",
    '200 M Free'    : "2:49.89",
    '400 M Free'    : "5:59.49",
    '800 M Free'    : "",
    '1500 M Free'   : "",
    '50 M Back'     : "42.99",
    '100 M Back'    : "1:30.89",
    '200 M Back'    : "",
    '50 M Breast'   : "46.99",
    '100 M Breast'  : "1:42.69",
    '200 M Breast'  : "",
    '50 M Fly'      : "40.19",
    '100 M Fly'     : "1:34.49",
    '200 M Fly'     : "",
    '200 M IM'      : "3:14.29",
    '400 M IM'      : "",
  },
  'JO_10_FEMALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "31.39",
    '100 Y Free'    : "1:10.49",
    '200 Y Free'    : "2:35.59",
    '500 Y Free'    : "6:43.99",
    '1000 Y Free'   : "",
    '1650 Y Free'   : "",
    '25 Y Back'     : "",
    '50 Y Back'     : "36.69",
    '100 Y Back'    : "1.19.29",
    '200 Y Back'    : "",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "41.69",
    '100 Y Breast'  : "1:31.89",
    '200 Y Breast'  : "",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "36.19",
    '100 Y Fly'     : "1:24.09",
    '200 Y Fly'     : "",
    '100 Y IM'      : "1:20.09",
    '200 Y IM'      : "2:52.39",
    '400 Y IM'      : "",

    '50 M Free'     : "35.59",
    '100 M Free'    : "1:20.19",
    '200 M Free'    : "2:55.59",
    '400 M Free'    : "6:04.29",
    '800 M Free'    : "",
    '1500 M Free'   : "",
    '50 M Back'     : "42.89",
    '100 M Back'    : "1:32.69",
    '200 M Back'    : "",
    '50 M Breast'   : "47.49",
    '100 M Breast'  : "1:44.89",
    '200 M Breast'  : "",
    '50 M Fly'      : "40.79",
    '100 M Fly'     : "1:35.39",
    '200 M Fly'     : "",
    '200 M IM'      : "3:17.09",
    '400 M IM'      : "",
  },
  'JO_11_MALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "29.79",
    '100 Y Free'    : "1:05.19",
    '200 Y Free'    : "2:21.39",
    '500 Y Free'    : "6:14.69",
    '1000 Y Free'   : "13:11.69",
    '1650 Y Free'   : "22:14.79",
    '25 Y Back'     : "",
    '50 Y Back'     : "34.69",
    '100 Y Back'    : "1:14.29",
    '200 Y Back'    : "2:38.69",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "38.99",
    '100 Y Breast'  : "1:23.59",
    '200 Y Breast'  : "2:59.39",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "33.39",
    '100 Y Fly'     : "1:14.59",
    '200 Y Fly'     : "2:49.39",
    '100 Y IM'      : "1:14.69",
    '200 Y IM'      : "2:40.89",
    '400 Y IM'      : "5:42.09",

    '50 M Free'     : "34.19",
    '100 M Free'    : "1:14.59",
    '200 M Free'    : "2:41.79",
    '400 M Free'    : "5:40.39",
    '800 M Free'    : "11:57.69",
    '1500 M Free'   : "23:05.09",
    '50 M Back'     : "39.99",
    '100 M Back'    : "1:26.89",
    '200 M Back'    : "3:03.39",
    '50 M Breast'   : "44.69",
    '100 M Breast'  : "1:37.69",
    '200 M Breast'  : "3:28.19",
    '50 M Fly'      : "37.59",
    '100 M Fly'     : "1:25.19",
    '200 M Fly'     : "3:10.69",
    '200 M IM'      : "3:05.49",
    '400 M IM'      : "6:33.39",
  },
  'JO_11_FEMALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "30.09",
    '100 Y Free'    : "1:05.49",
    '200 Y Free'    : "2:22.09",
    '500 Y Free'    : "6:24.09",
    '1000 Y Free'   : "13:17.69",
    '1650 Y Free'   : "22:25.99",
    '25 Y Back'     : "",
    '50 Y Back'     : "33.99",
    '100 Y Back'    : "1:14.09",
    '200 Y Back'    : "2:38.39",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "38.49",
    '100 Y Breast'  : "1:23.99",
    '200 Y Breast'  : "3:01.39",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "32.59",
    '100 Y Fly'     : "1:14.59",
    '200 Y Fly'     : "2:49.39",
    '100 Y IM'      : "1:14.59",
    '200 Y IM'      : "2:39.99",
    '400 Y IM'      : "5:41.79",

    '50 M Free'     : "34.19",
    '100 M Free'    : "1:14.69",
    '200 M Free'    : "2:43.09",
    '400 M Free'    : "5:43.09",
    '800 M Free'    : "12:06.49",
    '1500 M Free'   : "23:23.59",
    '50 M Back'     : "39.39",
    '100 M Back'    : "1:27.19",
    '200 M Back'    : "3:04.39",
    '50 M Breast'   : "44.09",
    '100 M Breast'  : "1:37.59",
    '200 M Breast'  : "3:29.79",
    '50 M Fly'      : "36.89",
    '100 M Fly'     : "1:24.89",
    '200 M Fly'     : "3:10.69",
    '200 M IM'      : "3:04.39",
    '400 M IM'      : "6:34.19",
  },
  'FW_10_MALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "30.19",
    '100 Y Free'    : "1:07.59",
    '200 Y Free'    : "2:26.99",
    '500 Y Free'    : "6:26.79",
    '1000 Y Free'   : "",
    '1650 Y Free'   : "",
    '25 Y Back'     : "",
    '50 Y Back'     : "35.79",
    '100 Y Back'    : "1:17.09",
    '200 Y Back'    : "",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "39.99",
    '100 Y Breast'  : "1:26.99",
    '200 Y Breast'  : "",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "33.99",
    '100 Y Fly'     : "1:20.49",
    '200 Y Fly'     : "",
    '100 Y IM'      : "1:16.89",
    '200 Y IM'      : "2:47.99",
    '400 Y IM'      : "",

    '50 M Free'     : "34.39",
    '100 M Free'    : "1:17.09",
    '200 M Free'    : "2:46.39",
    '400 M Free'    : "5:45.69",
    '800 M Free'    : "",
    '1500 M Free'   : "",
    '50 M Back'     : "40.79",
    '100 M Back'    : "1:26.79",
    '200 M Back'    : "",
    '50 M Breast'   : "45.59",
    '100 M Breast'  : "1:39.19",
    '200 M Breast'  : "",
    '50 M Fly'      : "38.49",
    '100 M Fly'     : "1:30.29",
    '200 M Fly'     : "",
    '200 M IM'      : "3:09.69",
    '400 M IM'      : "",
  },
  'FW_10_FEMALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "30.19",
    '100 Y Free'    : "1:08.09",
    '200 Y Free'    : "2:29.49",
    '500 Y Free'    : "6:25.69",
    '1000 Y Free'   : "",
    '1650 Y Free'   : "",
    '25 Y Back'     : "",
    '50 Y Back'     : "35.49",
    '100 Y Back'    : "1:17.09",
    '200 Y Back'    : "",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "40.29",
    '100 Y Breast'  : "1:28.99",
    '200 Y Breast'  : "",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "33.99",
    '100 Y Fly'     : "1:20.49",
    '200 Y Fly'     : "",
    '100 Y IM'      : "1:17.09",
    '200 Y IM'      : "2:47.99",
    '400 Y IM'      : "",

    '50 M Free'     : "34.79",
    '100 M Free'    : "1:17.59",
    '200 M Free'    : "2:52.79",
    '400 M Free'    : "5:44.59",
    '800 M Free'    : "",
    '1500 M Free'   : "",
    '50 M Back'     : "40.49",
    '100 M Back'    : "1:26.79",
    '200 M Back'    : "",
    '50 M Breast'   : "45.89",
    '100 M Breast'  : "1:41.19",
    '200 M Breast'  : "",
    '50 M Fly'      : "38.49",
    '100 M Fly'     : "1:30.29",
    '200 M Fly'     : "",
    '200 M IM'      : "3:09.69",
    '400 M IM'      : "",
  },
  'FW_11_12_MALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "26.19",
    '100 Y Free'    : "57.29",
    '200 Y Free'    : "2:06.69",
    '500 Y Free'    : "5:36.69",
    '1000 Y Free'   : "11:39.09",
    '1650 Y Free'   : "19:30.69",
    '25 Y Back'     : "",
    '50 Y Back'     : "30.59",
    '100 Y Back'    : "1:05.89",
    '200 Y Back'    : "2:20.79",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "34.09",
    '100 Y Breast'  : "1:14.29",
    '200 Y Breast'  : "2:39.89",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "28.89",
    '100 Y Fly'     : "1:04.99",
    '200 Y Fly'     : "2:25.09",
    '100 Y IM'      : "1:06.09",
    '200 Y IM'      : "2:24.09",
    '400 Y IM'      : "5:03.39",

    '50 M Free'     : "30.39",
    '100 M Free'    : "1:06.19",
    '200 M Free'    : "2:23.89",
    '400 M Free'    : "5:00.49",
    '800 M Free'    : "10:27.69",
    '1500 M Free'   : "20:10.89",
    '50 M Back'     : "34.59",
    '100 M Back'    : "1:16.59",
    '200 M Back'    : "2:41.19",
    '50 M Breast'   : "38.89",
    '100 M Breast'  : "1:24.49",
    '200 M Breast'  : "3:04.59",
    '50 M Fly'      : "32.99",
    '100 M Fly'     : "1:14.39",
    '200 M Fly'     : "2:42.29",
    '200 M IM'      : "2:46.19",
    '400 M IM'      : "5:43.19",
  },
  'FW_11_12_FEMALE' : {
    '25 Y Free'     : "",
    '50 Y Free'     : "26.79",
    '100 Y Free'    : "59.09",
    '200 Y Free'    : "2:08.49",
    '500 Y Free'    : "5:41.89",
    '1000 Y Free'   : "11:42.69",
    '1650 Y Free'   : "20:14.59",
    '25 Y Back'     : "",
    '50 Y Back'     : "31.09",
    '100 Y Back'    : "1:07.49",
    '200 Y Back'    : "2:26.79",
    '25 Y Breast'   : "",
    '50 Y Breast'   : "34.99",
    '100 Y Breast'  : "1:15.89",
    '200 Y Breast'  : "2:45.89",
    '25 Y Fly'      : "",
    '50 Y Fly'      : "29.49",
    '100 Y Fly'     : "1:05.89",
    '200 Y Fly'     : "2:28.09",
    '100 Y IM'      : "1:07.59",
    '200 Y IM'      : "2:25.09",
    '400 Y IM'      : "5:10.29",

    '50 M Free'     : "30.99",
    '100 M Free'    : "1:08.59",
    '200 M Free'    : "2:27.59",
    '400 M Free'    : "5:05.79",
    '800 M Free'    : "10:38.89",
    '1500 M Free'   : "20:38.89",
    '50 M Back'     : "35.49",
    '100 M Back'    : "1:17.09",
    '200 M Back'    : "2:46.19",
    '50 M Breast'   : "39.49",
    '100 M Breast'  : "1:27.39",
    '200 M Breast'  : "3:08.99",
    '50 M Fly'      : "33.69",
    '100 M Fly'     : "1:16.09",
    '200 M Fly'     : "2:49.59",
    '200 M IM'      : "2:48.79",
    '400 M IM'      : "5:56.69",
  },
}
