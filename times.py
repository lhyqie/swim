# From https://www.pacswim.org/userfiles/cms/documents/809/agc-time-std.-scy-2023-2024-rev-9.18.23.pdf
# and https://www.pacswim.org/userfiles/cms/documents/859/fw-time-std.---spring-2024-rev-8.25.23.pdf
times_name_pair = [
  ("JO-10-MALE",        "Men\u00A0\u00A0 10 & Under\u00A0\u00A0Age Group Championship"), 
  ("FW-10-MALE",        "Men\u00A0\u00A0 10 & Under\u00A0\u00A0Far Western"),
  ("JO-11-MALE",        "Men\u00A0\u00A0 11 \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0Age Group Championship"), 
  ("FW-11-12-MALE",     "Men\u00A0\u00A0 11-12\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0Far Western"),
  ("JO-10-FEMALE",      "Women 10 & Under \u00A0Age Group Championship"),
  ("FW-10-FEMALE",      "Women 10 & Under \u00A0Far Western"),
  ("JO-11-FEMALE",      "Women 11 \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0Age Group Championship"), 
  ("FW-11-12-FEMALE",   "Women 11-12 \u00A0\u00A0\u00A0\u00A0\u00A0 Far Western"),
]

times_map = {
  'JO-10-MALE' : {
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
  'JO-10-FEMALE' : {
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
  'JO-11-MALE' : {
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
  'JO-11-FEMALE' : {
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
  'FW-10-MALE' : {
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
  'FW-10-FEMALE' : {
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
  'FW-11-12-MALE' : {
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
  'FW-11-12-FEMALE' : {
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

national_times_name_pair = [
  ("10-MALE",       "Boys\u00A0 10 & Under"), 
  ("11-12-MALE",    "Boys\u00A0 11-12"), 
  ("10-FEMALE",     "Girls 10 & Under"), 
  ("11-12-FEMALE",  "Girls 11-12"), 
]

# exported from data/export.py
# using data from https://www.pacswim.org/userfiles/cms/documents/801/2021-2024-national-age-group-motivational-times.pdf
national_timemap = {'10-MALE': {'AAAA': {'25 Y Free': '', '50 Y Free': '27.39', '100 Y Free': '1:00.59', '200 Y Free': '2:10.69', '500 Y Free': '5:47.69', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '31.69', '100 Y Back': '1:08.39', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '35.49', '100 Y Breast': '1:18.29', '25 Y Fly': '', '50 Y Fly': '30.29', '100 Y Fly': '1:08.49', '200 Y Fly': '', '100 Y IM': '1:09.09', '200 Y IM': '2:28.69', '400 Y IM': '', '50 M Free': '31.39', '100 M Free': '1:09.49', '200 M Free': '2:29.49', '400 M Free': '5:14.59', '800 M Free': '', '1500 M Free': '', '50 M Back': '36.89', '100 M Back': '1:18.89', '200 M Back': '', '50 M Breast': '40.59', '100 M Breast': '1:29.29', '200 M Breat': '', '50 M Fly': '34.39', '100 M Fly': '1:18.09', '200 M Fly': '', '200 M IM': '2:49.89', '400 M IM': ''}, 'AAA': {'25 Y Free': '', '50 Y Free': '28.59', '100 Y Free': '1:03.69', '200 Y Free': '2:16.89', '500 Y Free': '6:04.19', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '33.49', '100 Y Back': '1:11.89', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '37.29', '100 Y Breast': '1:22.19', '25 Y Fly': '', '50 Y Fly': '31.99', '100 Y Fly': '1:13.19', '200 Y Fly': '', '100 Y IM': '1:12.39', '200 Y IM': '2:36.19', '400 Y IM': '', '50 M Free': '32.79', '100 M Free': '1:12.89', '200 M Free': '2:36.59', '400 M Free': '5:29.59', '800 M Free': '', '1500 M Free': '', '50 M Back': '38.89', '100 M Back': '1:22.89', '200 M Back': '', '50 M Breast': '42.69', '100 M Breast': '1:33.79', '200 M Breat': '', '50 M Fly': '36.29', '100 M Fly': '1:23.59', '200 M Fly': '', '200 M IM': '2:58.39', '400 M IM': ''}, 'AA': {'25 Y Free': '', '50 Y Free': '29.79', '100 Y Free': '1:06.69', '200 Y Free': '2:23.09', '500 Y Free': '6:20.79', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '35.19', '100 Y Back': '1:15.39', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '39.19', '100 Y Breast': '1:26.09', '25 Y Fly': '', '50 Y Fly': '33.69', '100 Y Fly': '1:17.99', '200 Y Fly': '', '100 Y IM': '1:15.69', '200 Y IM': '2:43.59', '400 Y IM': '', '50 M Free': '34.09', '100 M Free': '1:16.39', '200 M Free': '2:43.69', '400 M Free': '5:44.49', '800 M Free': '', '1500 M Free': '', '50 M Back': '40.99', '100 M Back': '1:26.99', '200 M Back': '', '50 M Breast': '44.89', '100 M Breast': '1:38.19', '200 M Breat': '', '50 M Fly': '38.19', '100 M Fly': '1:28.99', '200 M Fly': '', '200 M IM': '3:06.89', '400 M IM': ''}, 'A': {'25 Y Free': '', '50 Y Free': '30.99', '100 Y Free': '1:09.69', '200 Y Free': '2:29.39', '500 Y Free': '6:37.39', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '36.99', '100 Y Back': '1:18.79', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '40.99', '100 Y Breast': '1:29.99', '25 Y Fly': '', '50 Y Fly': '35.39', '100 Y Fly': '1:22.79', '200 Y Fly': '', '100 Y IM': '1:18.99', '200 Y IM': '2:50.99', '400 Y IM': '', '50 M Free': '35.49', '100 M Free': '1:19.79', '200 M Free': '2:50.79', '400 M Free': '5:59.49', '800 M Free': '', '1500 M Free': '', '50 M Back': '42.99', '100 M Back': '1:30.99', '200 M Back': '', '50 M Breast': '46.99', '100 M Breast': '1:42.69', '200 M Breat': '', '50 M Fly': '40.19', '100 M Fly': '1:34.49', '200 M Fly': '', '200 M IM': '3:15.39', '400 M IM': ''}, 'BB': {'25 Y Free': '', '50 Y Free': '34.49', '100 Y Free': '1:18.79', '200 Y Free': '2:47.99', '500 Y Free': '7:26.99', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '42.29', '100 Y Back': '1:29.29', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '46.59', '100 Y Breast': '1:41.69', '25 Y Fly': '', '50 Y Fly': '40.49', '100 Y Fly': '1:37.09', '200 Y Fly': '', '100 Y IM': '1:28.89', '200 Y IM': '3:13.19', '400 Y IM': '', '50 M Free': '39.49', '100 M Free': '1:30.19', '200 M Free': '3:12.09', '400 M Free': '6:44.49', '800 M Free': '', '1500 M Free': '', '50 M Back': '49.19', '100 M Back': '1:43.09', '200 M Back': '', '50 M Breast': '53.29', '100 M Breast': '1:55.99', '200 M Breat': '', '50 M Fly': '45.99', '100 M Fly': '1:50.79', '200 M Fly': '', '200 M IM': '3:40.79', '400 M IM': ''}, 'B': {'25 Y Free': '', '50 Y Free': '38.09', '100 Y Free': '1:27.79', '200 Y Free': '3:06.69', '500 Y Free': '8:16.69', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '47.49', '100 Y Back': '1:39.79', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '52.09', '100 Y Breast': '1:53.39', '25 Y Fly': '', '50 Y Fly': '45.69', '100 Y Fly': '1:51.39', '200 Y Fly': '', '100 Y IM': '1:38.79', '200 Y IM': '3:35.49', '400 Y IM': '', '50 M Free': '43.59', '100 M Free': '1:40.59', '200 M Free': '3:33.49', '400 M Free': '7:29.39', '800 M Free': '', '1500 M Free': '', '50 M Back': '55.29', '100 M Back': '1:55.09', '200 M Back': '', '50 M Breast': '59.69', '100 M Breast': '2:09.39', '200 M Breat': '', '50 M Fly': '51.79', '100 M Fly': '2:07.09', '200 M Fly': '', '200 M IM': '4:06.19', '400 M IM': ''}, '25 Y Free': {}, '50 Y Free': {}, '100 Y Free': {}, '200 Y Free': {}, '500 Y Free': {}, '1000 Y Free': {}, '1650 Y Free': {}, '25 Y Back': {}, '50 Y Back': {}, '100 Y Back': {}, '200 Y Back': {}, '25 Y Breast': {}, '50 Y Breast': {}, '100 Y Breast': {}, '200 Y Breast': {}, '25 Y Fly': {}, '50 Y Fly': {}, '100 Y Fly': {}, '200 Y Fly': {}, '100 Y IM': {}, '200 Y IM': {}, '400 Y IM': {}, '50 M Free': {}, '100 M Free': {}, '200 M Free': {}, '400 M Free': {}, '800 M Free': {}, '1500 M Free': {}, '50 M Back': {}, '100 M Back': {}, '200 M Back': {}, '50 M Breast': {}, '100 M Breast': {}, '200 M Breat': {}, '50 M Fly': {}, '100 M Fly': {}, '200 M Fly': {}, '200 M IM': {}, '400 M IM': {}}, '10-FEMALE': {'AAAA': {'25 Y Free': '', '50 Y Free': '27.69', '100 Y Free': '1:00.99', '200 Y Free': '2:13.59', '500 Y Free': '5:53.79', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '31.59', '100 Y Back': '1:07.99', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '35.99', '100 Y Breast': '1:18.79', '25 Y Fly': '', '50 Y Fly': '30.59', '100 Y Fly': '1:09.19', '200 Y Fly': '', '100 Y IM': '1:09.79', '200 Y IM': '2:29.79', '400 Y IM': '', '50 M Free': '31.39', '100 M Free': '1:09.39', '200 M Free': '2:31.59', '400 M Free': '5:19.79', '800 M Free': '', '1500 M Free': '', '50 M Back': '36.89', '100 M Back': '1:19.49', '200 M Back': '', '50 M Breast': '40.89', '100 M Breast': '1:29.89', '200 M Breat': '', '50 M Fly': '34.49', '100 M Fly': '1:18.89', '200 M Fly': '', '200 M IM': '2:50.89', '400 M IM': ''}, 'AAA': {'25 Y Free': '', '50 Y Free': '28.89', '100 Y Free': '1:04.19', '200 Y Free': '2:20.89', '500 Y Free': '6:10.59', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '33.29', '100 Y Back': '1:11.79', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '37.89', '100 Y Breast': '1:23.09', '25 Y Fly': '', '50 Y Fly': '32.49', '100 Y Fly': '1:14.19', '200 Y Fly': '', '100 Y IM': '1:13.49', '200 Y IM': '2:37.39', '400 Y IM': '', '50 M Free': '32.79', '100 M Free': '1:13.09', '200 M Free': '2:39.79', '400 M Free': '5:34.99', '800 M Free': '', '1500 M Free': '', '50 M Back': '38.89', '100 M Back': '1:23.89', '200 M Back': '', '50 M Breast': '43.09', '100 M Breast': '1:34.89', '200 M Breat': '', '50 M Fly': '36.59', '100 M Fly': '1:24.59', '200 M Fly': '', '200 M IM': '2:59.59', '400 M IM': ''}, 'AA': {'25 Y Free': '', '50 Y Free': '30.19', '100 Y Free': '1:07.29', '200 Y Free': '2:28.19', '500 Y Free': '6:27.49', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '34.99', '100 Y Back': '1:15.59', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '39.79', '100 Y Breast': '1:27.49', '25 Y Fly': '', '50 Y Fly': '34.39', '100 Y Fly': '1:19.19', '200 Y Fly': '', '100 Y IM': '1:17.09', '200 Y IM': '2:45.09', '400 Y IM': '', '50 M Free': '34.19', '100 M Free': '1:16.69', '200 M Free': '2:48.09', '400 M Free': '5:50.19', '800 M Free': '', '1500 M Free': '', '50 M Back': '40.89', '100 M Back': '1:28.29', '200 M Back': '', '50 M Breast': '45.29', '100 M Breast': '1:39.89', '200 M Breat': '', '50 M Fly': '38.69', '100 M Fly': '1:30.29', '200 M Fly': '', '200 M IM': '3:08.29', '400 M IM': ''}, 'A': {'25 Y Free': '', '50 Y Free': '31.39', '100 Y Free': '1:10.49', '200 Y Free': '2:35.39', '500 Y Free': '6:44.29', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '36.69', '100 Y Back': '1:19.29', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '41.69', '100 Y Breast': '1:31.89', '25 Y Fly': '', '50 Y Fly': '36.19', '100 Y Fly': '1:24.09', '200 Y Fly': '', '100 Y IM': '1:20.79', '200 Y IM': '2:52.69', '400 Y IM': '', '50 M Free': '35.59', '100 M Free': '1:20.29', '200 M Free': '2:56.29', '400 M Free': '6:05.39', '800 M Free': '', '1500 M Free': '', '50 M Back': '42.89', '100 M Back': '1:32.69', '200 M Back': '', '50 M Breast': '47.49', '100 M Breast': '1:44.89', '200 M Breat': '', '50 M Fly': '40.79', '100 M Fly': '1:35.99', '200 M Fly': '', '200 M IM': '3:17.09', '400 M IM': ''}, 'BB': {'25 Y Free': '', '50 Y Free': '35.19', '100 Y Free': '1:19.99', '200 Y Free': '2:57.19', '500 Y Free': '7:34.89', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '41.89', '100 Y Back': '1:30.69', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '47.49', '100 Y Breast': '1:44.99', '25 Y Fly': '', '50 Y Fly': '41.79', '100 Y Fly': '1:39.09', '200 Y Fly': '', '100 Y IM': '1:31.69', '200 Y IM': '3:15.59', '400 Y IM': '', '50 M Free': '39.89', '100 M Free': '1:31.19', '200 M Free': '3:20.99', '400 M Free': '6:51.09', '800 M Free': '', '1500 M Free': '', '50 M Back': '48.89', '100 M Back': '1:45.99', '200 M Back': '', '50 M Breast': '53.99', '100 M Breast': '1:59.79', '200 M Breat': '', '50 M Fly': '47.09', '100 M Fly': '1:52.99', '200 M Fly': '', '200 M IM': '3:43.19', '400 M IM': ''}, 'B': {'25 Y Free': '', '50 Y Free': '38.89', '100 Y Free': '1:29.59', '200 Y Free': '3:18.99', '500 Y Free': '8:25.39', '1000 Y Free': '', '1650 Y Free': '', '25 Y Back': '', '50 Y Back': '46.99', '100 Y Back': '1:41.99', '200 Y Back': '', '25 Y Breast': '', '50 Y Breast': '53.19', '100 Y Breast': '1:58.09', '25 Y Fly': '', '50 Y Fly': '47.39', '100 Y Fly': '1:53.99', '200 Y Fly': '', '100 Y IM': '1:42.59', '200 Y IM': '3:38.49', '400 Y IM': '', '50 M Free': '44.09', '100 M Free': '1:41.99', '200 M Free': '3:45.79', '400 M Free': '7:36.79', '800 M Free': '', '1500 M Free': '', '50 M Back': '54.89', '100 M Back': '1:59.19', '200 M Back': '', '50 M Breast': '1:00.49', '100 M Breast': '2:14.79', '200 M Breat': '', '50 M Fly': '53.39', '100 M Fly': '2:09.99', '200 M Fly': '', '200 M IM': '4:09.39', '400 M IM': ''}, '25 Y Free': {}, '50 Y Free': {}, '100 Y Free': {}, '200 Y Free': {}, '500 Y Free': {}, '': {}, '1000 Y Free': {}, '1650 Y Free': {}, '25 Y Back': {}, '50 Y Back': {}, '100 Y Back': {}, '200 Y Back': {}, '25 Y Breast': {}, '50 Y Breast': {}, '100 Y Breast': {}, '200 Y Breast': {}, '25 Y Fly': {}, '50 Y Fly': {}, '100 Y Fly': {}, '200 Y Fly': {}, '100 Y IM': {}, '200 Y IM': {}, '400 Y IM': {}, '50 M Free': {}, '100 M Free': {}, '200 M Free': {}, '400 M Free': {}, '800 M Free': {}, '1500 M Free': {}, '50 M Back': {}, '100 M Back': {}, '200 M Back': {}, '50 M Breast': {}, '100 M Breast': {}, '200 M Breat': {}, '50 M Fly': {}, '100 M Fly': {}, '200 M Fly': {}, '200 M IM': {}, '400 M IM': {}}, '11-12-MALE': {'AAAA': {'25 Y Free': '', '50 Y Free': '24.49', '100 Y Free': '53.29', '200 Y Free': '1:55.89', '500 Y Free': '5:12.99', '1000 Y Free': '10:54.39', '1650 Y Free': '18:16.39', '25 Y Back': '', '50 Y Back': '27.79', '100 Y Back': '59.49', '200 Y Back': '2:08.99', '25 Y Breast': '', '50 Y Breast': '31.09', '100 Y Breast': '1:06.99', '200 Y Breast': '2:25.59', '25 Y Fly': '', '50 Y Fly': '26.79', '100 Y Fly': '58.99', '200 Y Fly': '2:09.89', '100 Y IM': '1:00.29', '200 Y IM': '2:10.69', '400 Y IM': '4:39.79', '50 M Free': '27.99', '100 M Free': '1:00.99', '200 M Free': '2:13.19', '400 M Free': '4:41.59', '800 M Free': '9:53.79', '1500 M Free': '18:55.19', '50 M Back': '31.99', '100 M Back': '1:09.19', '200 M Back': '2:29.59', '50 M Breast': '35.49', '100 M Breast': '1:18.09', '200 M Breast': '2:48.49', '50 M Fly': '30.19', '100 M Fly': '1:06.99', '200 M Fly': '2:30.39', '200 M IM': '2:30.19', '400 M IM': '5:22.39'}, 'AAA': {'25 Y Free': '', '50 Y Free': '25.59', '100 Y Free': '55.79', '200 Y Free': '2:01.39', '500 Y Free': '5:27.89', '1000 Y Free': '11:25.59', '1650 Y Free': '19:08.59', '25 Y Back': '', '50 Y Back': '29.29', '100 Y Back': '1:02.79', '200 Y Back': '2:15.19', '25 Y Breast': '', '50 Y Breast': '32.69', '100 Y Breast': '1:10.49', '200 Y Breast': '2:32.49', '25 Y Fly': '', '50 Y Fly': '28.19', '100 Y Fly': '1:02.39', '200 Y Fly': '2:16.09', '100 Y IM': '1:03.29', '200 Y IM': '2:17.29', '400 Y IM': '4:53.19', '50 M Free': '29.29', '100 M Free': '1:03.89', '200 M Free': '2:19.49', '400 M Free': '4:55.09', '800 M Free': '10:22.09', '1500 M Free': '19:49.19', '50 M Back': '33.69', '100 M Back': '1:12.99', '200 M Back': '2:36.69', '50 M Breast': '37.49', '100 M Breast': '1:22.19', '200 M Breast': '2:56.59', '50 M Fly': '31.89', '100 M Fly': '1:10.89', '200 M Fly': '2:37.49', '200 M IM': '2:37.79', '400 M IM': '5:37.79'}, 'AA': {'25 Y Free': '', '50 Y Free': '26.79', '100 Y Free': '58.29', '200 Y Free': '2:06.99', '500 Y Free': '5:42.79', '1000 Y Free': '11:56.79', '1650 Y Free': '20:00.79', '25 Y Back': '', '50 Y Back': '30.69', '100 Y Back': '1:05.99', '200 Y Back': '2:21.29', '25 Y Breast': '', '50 Y Breast': '34.39', '100 Y Breast': '1:13.99', '200 Y Breast': '2:39.39', '25 Y Fly': '', '50 Y Fly': '29.69', '100 Y Fly': '1:05.89', '200 Y Fly': '2:22.19', '100 Y IM': '1:06.19', '200 Y IM': '2:23.99', '400 Y IM': '5:06.49', '50 M Free': '30.69', '100 M Free': '1:06.79', '200 M Free': '2:25.79', '400 M Free': '5:08.49', '800 M Free': '10:50.39', '1500 M Free': '20:43.29', '50 M Back': '35.39', '100 M Back': '1:16.69', '200 M Back': '2:43.79', '50 M Breast': '39.39', '100 M Breast': '1:26.19', '200 M Breast': '3:04.59', '50 M Fly': '33.59', '100 M Fly': '1:14.69', '200 M Fly': '2:44.69', '200 M IM': '2:45.49', '400 M IM': '5:53.09'}, 'A': {'25 Y Free': '', '50 Y Free': '27.89', '100 Y Free': '1:00.89', '200 Y Free': '2:12.49', '500 Y Free': '5:57.69', '1000 Y Free': '12:27.89', '1650 Y Free': '20:52.99', '25 Y Back': '', '50 Y Back': '32.09', '100 Y Back': '1:09.19', '200 Y Back': '2:27.39', '25 Y Breast': '', '50 Y Breast': '36.09', '100 Y Breast': '1:17.49', '200 Y Breast': '2:46.39', '25 Y Fly': '', '50 Y Fly': '31.19', '100 Y Fly': '1:09.29', '200 Y Fly': '2:28.39', '100 Y IM': '1:09.09', '200 Y IM': '2:30.69', '400 Y IM': '5:19.79', '50 M Free': '31.99', '100 M Free': '1:09.69', '200 M Free': '2:32.19', '400 M Free': '5:21.89', '800 M Free': '11:18.59', '1500 M Free': '21:37.39', '50 M Back': '36.99', '100 M Back': '1:20.49', '200 M Back': '2:50.99', '50 M Breast': '41.29', '100 M Breast': '1:30.29', '200 M Breast': '3:12.59', '50 M Fly': '35.19', '100 M Fly': '1:18.59', '200 M Fly': '2:51.89', '200 M IM': '2:53.19', '400 M IM': '6:08.49'}, 'BB': {'25 Y Free': '', '50 Y Free': '30.29', '100 Y Free': '1:05.89', '200 Y Free': '2:23.49', '500 Y Free': '6:27.49', '1000 Y Free': '13:30.19', '1650 Y Free': '22:37.49', '25 Y Back': '', '50 Y Back': '34.99', '100 Y Back': '1:15.69', '200 Y Back': '2:39.69', '25 Y Breast': '', '50 Y Breast': '39.49', '100 Y Breast': '1:24.49', '200 Y Breast': '3:00.19', '25 Y Fly': '', '50 Y Fly': '34.19', '100 Y Fly': '1:16.09', '200 Y Fly': '2:40.79', '100 Y IM': '1:14.99', '200 Y IM': '2:43.99', '400 Y IM': '5:46.39', '50 M Free': '34.69', '100 M Free': '1:15.49', '200 M Free': '2:44.89', '400 M Free': '5:48.69', '800 M Free': '12:15.19', '1500 M Free': '23:25.49', '50 M Back': '40.39', '100 M Back': '1:27.99', '200 M Back': '3:05.19', '50 M Breast': '45.19', '100 M Breast': '1:38.39', '200 M Breast': '3:28.69', '50 M Fly': '38.59', '100 M Fly': '1:26.29', '200 M Fly': '3:06.19', '200 M IM': '3:08.49', '400 M IM': '6:39.19'}, 'B': {'25 Y Free': '', '50 Y Free': '32.59', '100 Y Free': '1:10.99', '200 Y Free': '2:34.59', '500 Y Free': '6:57.29', '1000 Y Free': '14:32.59', '1650 Y Free': '24:21.89', '25 Y Back': '', '50 Y Back': '37.89', '100 Y Back': '1:22.19', '200 Y Back': '2:51.99', '25 Y Breast': '', '50 Y Breast': '42.89', '100 Y Breast': '1:31.39', '200 Y Breast': '3:14.09', '25 Y Fly': '', '50 Y Fly': '37.09', '100 Y Fly': '1:22.89', '200 Y Fly': '2:53.19', '100 Y IM': '1:20.89', '200 Y IM': '2:57.29', '400 Y IM': '6:13.09', '50 M Free': '37.29', '100 M Free': '1:21.29', '200 M Free': '2:57.49', '400 M Free': '6:15.49', '800 M Free': '13:11.69', '1500 M Free': '25:13.59', '50 M Back': '43.69', '100 M Back': '1:35.49', '200 M Back': '3:19.49', '50 M Breast': '48.99', '100 M Breast': '1:46.59', '200 M Breast': '3:44.69', '50 M Fly': '41.89', '100 M Fly': '1:33.99', '200 M Fly': '3:20.49', '200 M IM': '3:23.79', '400 M IM': '7:09.89'}, '25 Y Free': {}, '50 Y Free': {}, '100 Y Free': {}, '200 Y Free': {}, '500 Y Free': {}, '1000 Y Free': {}, '1650 Y Free': {}, '25 Y Back': {}, '50 Y Back': {}, '100 Y Back': {}, '200 Y Back': {}, '25 Y Breast': {}, '50 Y Breast': {}, '100 Y Breast': {}, '200 Y Breast': {}, '25 Y Fly': {}, '50 Y Fly': {}, '100 Y Fly': {}, '200 Y Fly': {}, '100 Y IM': {}, '200 Y IM': {}, '400 Y IM': {}, '50 M Free': {}, '100 M Free': {}, '200 M Free': {}, '400 M Free': {}, '800 M Free': {}, '1500 M Free': {}, '50 M Back': {}, '100 M Back': {}, '200 M Back': {}, '50 M Breast': {}, '100 M Breast': {}, '200 M Breast': {}, '50 M Fly': {}, '100 M Fly': {}, '200 M Fly': {}, '200 M IM': {}, '400 M IM': {}}, '11-12-FEMALE': {'AAAA': {'25 Y Free': '', '50 Y Free': '25.49', '100 Y Free': '55.19', '200 Y Free': '2:00.29', '500 Y Free': '5:21.59', '1000 Y Free': '11:06.09', '1650 Y Free': '18:40.49', '25 Y Back': '', '50 Y Back': '28.59', '100 Y Back': '1:01.39', '200 Y Back': '2:12.49', '25 Y Breast': '', '50 Y Breast': '32.29', '100 Y Breast': '1:09.79', '200 Y Breast': '2:30.69', '25 Y Fly': '', '50 Y Fly': '27.39', '100 Y Fly': '1:00.79', '200 Y Fly': '2:14.99', '100 Y IM': '1:03.09', '200 Y IM': '2:15.19', '400 Y IM': '4:48.19', '50 M Free': '29.09', '100 M Free': '1:03.09', '200 M Free': '2:16.69', '400 M Free': '4:47.99', '800 M Free': '10:03.09', '1500 M Free': '19:19.39', '50 M Back': '32.99', '100 M Back': '1:11.49', '200 M Back': '2:33.39', '50 M Breast': '36.69', '100 M Breast': '1:20.79', '200 M Breast': '2:54.49', '50 M Fly': '30.99', '100 M Fly': '1:09.29', '200 M Fly': '2:33.69', '200 M IM': '2:34.59', '400 M IM': '5:29.79'}, 'AAA': {'25 Y Free': '', '50 Y Free': '26.59', '100 Y Free': '57.79', '200 Y Free': '2:05.99', '500 Y Free': '5:36.89', '1000 Y Free': '11:37.79', '1650 Y Free': '19:33.89', '25 Y Back': '', '50 Y Back': '29.99', '100 Y Back': '1:04.69', '200 Y Back': '2:18.79', '25 Y Breast': '', '50 Y Breast': '33.79', '100 Y Breast': '1:13.19', '200 Y Breast': '2:37.89', '25 Y Fly': '', '50 Y Fly': '28.69', '100 Y Fly': '1:04.19', '200 Y Fly': '2:21.39', '100 Y IM': '1:06.09', '200 Y IM': '2:21.59', '400 Y IM': '5:01.89', '50 M Free': '30.39', '100 M Free': '1:06.09', '200 M Free': '2:23.19', '400 M Free': '5:01.69', '800 M Free': '10:31.79', '1500 M Free': '20:14.59', '50 M Back': '34.49', '100 M Back': '1:15.39', '200 M Back': '2:40.69', '50 M Breast': '38.49', '100 M Breast': '1:24.79', '200 M Breast': '3:02.79', '50 M Fly': '32.39', '100 M Fly': '1:13.09', '200 M Fly': '2:40.99', '200 M IM': '2:41.89', '400 M IM': '5:45.49'}, 'AA': {'25 Y Free': '', '50 Y Free': '27.79', '100 Y Free': '1:00.49', '200 Y Free': '2:11.79', '500 Y Free': '5:52.19', '1000 Y Free': '12:09.49', '1650 Y Free': '20:27.19', '25 Y Back': '', '50 Y Back': '31.29', '100 Y Back': '1:08.09', '200 Y Back': '2:25.09', '25 Y Breast': '', '50 Y Breast': '35.39', '100 Y Breast': '1:16.69', '200 Y Breast': '2:45.09', '25 Y Fly': '', '50 Y Fly': '29.99', '100 Y Fly': '1:07.49', '200 Y Fly': '2:27.89', '100 Y IM': '1:09.09', '200 Y IM': '2:27.99', '400 Y IM': '5:15.59', '50 M Free': '31.69', '100 M Free': '1:09.09', '200 M Free': '2:29.69', '400 M Free': '5:15.39', '800 M Free': '11:00.59', '1500 M Free': '21:09.79', '50 M Back': '36.09', '100 M Back': '1:19.29', '200 M Back': '2:47.99', '50 M Breast': '40.19', '100 M Breast': '1:28.79', '200 M Breast': '3:11.09', '50 M Fly': '33.89', '100 M Fly': '1:16.99', '200 M Fly': '2:48.29', '200 M IM': '2:49.29', '400 M IM': '6:01.19'}, 'A': {'25 Y Free': '', '50 Y Free': '28.99', '100 Y Free': '1:03.09', '200 Y Free': '2:17.49', '500 Y Free': '6:07.59', '1000 Y Free': '12:41.19', '1650 Y Free': '21:20.59', '25 Y Back': '', '50 Y Back': '32.69', '100 Y Back': '1:11.39', '200 Y Back': '2:31.39', '25 Y Breast': '', '50 Y Breast': '36.89', '100 Y Breast': '1:20.19', '200 Y Breast': '2:52.19', '25 Y Fly': '', '50 Y Fly': '31.29', '100 Y Fly': '1:10.89', '200 Y Fly': '2:34.29', '100 Y IM': '1:12.09', '200 Y IM': '2:34.49', '400 Y IM': '5:29.29', '50 M Free': '32.99', '100 M Free': '1:12.09', '200 M Free': '2:36.19', '400 M Free': '5:29.09', '800 M Free': '11:29.29', '1500 M Free': '22:04.99', '50 M Back': '37.69', '100 M Back': '1:23.19', '200 M Back': '2:55.29', '50 M Breast': '41.99', '100 M Breast': '1:32.79', '200 M Breast': '3:19.39', '50 M Fly': '35.39', '100 M Fly': '1:20.79', '200 M Fly': '2:55.59', '200 M IM': '2:56.59', '400 M IM': '6:16.89'}, 'BB': {'25 Y Free': '', '50 Y Free': '31.29', '100 Y Free': '1:08.29', '200 Y Free': '2:28.99', '500 Y Free': '6:38.19', '1000 Y Free': '13:44.69', '1650 Y Free': '23:07.29', '25 Y Back': '', '50 Y Back': '35.39', '100 Y Back': '1:18.09', '200 Y Back': '2:43.99', '25 Y Breast': '', '50 Y Breast': '39.99', '100 Y Breast': '1:27.19', '200 Y Breast': '3:06.59', '25 Y Fly': '', '50 Y Fly': '33.89', '100 Y Fly': '1:17.59', '200 Y Fly': '2:47.19', '100 Y IM': '1:18.09', '200 Y IM': '2:47.29', '400 Y IM': '5:56.79', '50 M Free': '35.69', '100 M Free': '1:18.09', '200 M Free': '2:49.19', '400 M Free': '5:56.49', '800 M Free': '12:26.69', '1500 M Free': '23:55.39', '50 M Back': '40.79', '100 M Back': '1:30.99', '200 M Back': '3:09.89', '50 M Breast': '45.49', '100 M Breast': '1:40.89', '200 M Breast': '3:35.99', '50 M Fly': '38.29', '100 M Fly': '1:28.49', '200 M Fly': '3:10.19', '200 M IM': '3:11.39', '400 M IM': '6:48.29'}, 'B': {'25 Y Free': '', '50 Y Free': '33.59', '100 Y Free': '1:13.59', '200 Y Free': '2:40.39', '500 Y Free': '7:08.79', '1000 Y Free': '14:48.09', '1650 Y Free': '24:53.99', '25 Y Back': '', '50 Y Back': '38.09', '100 Y Back': '1:24.79', '200 Y Back': '2:56.59', '25 Y Breast': '', '50 Y Breast': '42.99', '100 Y Breast': '1:34.09', '200 Y Breast': '3:20.89', '25 Y Fly': '', '50 Y Fly': '36.49', '100 Y Fly': '1:24.39', '200 Y Fly': '2:59.99', '100 Y IM': '1:24.09', '200 Y IM': '3:00.19', '400 Y IM': '6:24.19', '50 M Free': '38.39', '100 M Free': '1:24.09', '200 M Free': '3:02.29', '400 M Free': '6:23.89', '800 M Free': '13:24.09', '1500 M Free': '25:45.79', '50 M Back': '43.99', '100 M Back': '1:38.69', '200 M Back': '3:24.49', '50 M Breast': '48.99', '100 M Breast': '1:48.89', '200 M Breast': '3:52.59', '50 M Fly': '41.29', '100 M Fly': '1:36.19', '200 M Fly': '3:24.89', '200 M IM': '3:26.09', '400 M IM': '7:19.69'}, '25 Y Free': {}, '50 Y Free': {}, '100 Y Free': {}, '200 Y Free': {}, '500 Y Free': {}, '1000 Y Free': {}, '1650 Y Free': {}, '25 Y Back': {}, '50 Y Back': {}, '100 Y Back': {}, '200 Y Back': {}, '25 Y Breast': {}, '50 Y Breast': {}, '100 Y Breast': {}, '200 Y Breast': {}, '25 Y Fly': {}, '50 Y Fly': {}, '100 Y Fly': {}, '200 Y Fly': {}, '100 Y IM': {}, '200 Y IM': {}, '400 Y IM': {}, '50 M Free': {}, '100 M Free': {}, '200 M Free': {}, '400 M Free': {}, '800 M Free': {}, '1500 M Free': {}, '50 M Back': {}, '100 M Back': {}, '200 M Back': {}, '50 M Breast': {}, '100 M Breast': {}, '200 M Breast': {}, '50 M Fly': {}, '100 M Fly': {}, '200 M Fly': {}, '200 M IM': {}, '400 M IM': {}}}