


# scanning endpoints
GET_ENDPOINTS = True
METADATA_FILE = 'endpoints.json'
URL_METADATA = 'https://www.startupuniverse.ch/api/1.0/de/counters/get/{0}'
RNG = (1,200) # seems to be between 10 and 150

# dashboard url constructing
URL_DATA = 'https://www.countee.ch/app/de/counter/{0}'

# output generation
WRITE_CSV = True
CSV_PATH = 'results.csv'

MARKDOWN_FILE = 'README.md'
MARKDOWN_TEMPLATE = '''
⚠️ This file is generated automatically. Please make edits to the markdown in [`config.py`](https://github.com/philshem/swiss_counter_data/blob/master/config.py).

# Use the following table as a list of entry-counter status, and availability of open places

I made this list so as some swimming pools open, I'd like an easy index for checking how crowded they are, or if they are no longer allowing entries.

The dashboards for each place are publicly available (see screenshot)
![example screenshot](https://raw.githubusercontent.com/philshem/swiss_counter_data/master/screenshot.png)

But as far as I know, are not yet indexed.

---

The python3 script [`parse_endpoints.py`](https://github.com/philshem/swiss_counter_data/blob/master/parse_endpoints.py):

+ generates list of valid endpoints, saved to [`endpoints.json`](https://github.com/philshem/swiss_counter_data/blob/master/endpoints.json)

+ writes list as CSV, saved to [`results.json`](https://github.com/philshem/swiss_counter_data/blob/master/results.json)

+ writes this file ([`README.md`](https://github.com/philshem/swiss_counter_data/blob/master/README.md)) with table of links

---
## Results table

{0}

All things unofficial. Data is owned by the owners. YMMV.

'''


#MARKDOWN_TEMPLATE = MARKDOWN_TEMPLATE.format()