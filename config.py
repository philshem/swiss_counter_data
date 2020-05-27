


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
# Use the following table to find status and availability of open places

The python3 script `parse_endpoints.py`:

+ generates list of valid endpoints, saved to {0}

+ writes this file ({1}) with table of links

---
## Results table

{2}

All things unofficial. Data is owned by the owners. YMMV.

'''


#MARKDOWN_TEMPLATE = MARKDOWN_TEMPLATE.format()