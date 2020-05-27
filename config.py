
'''
params for running parse_endpoints.py
'''


# scanning endpoints
GET_ENDPOINTS = False
METADATA_FILE = 'endpoints.json'
URL_METADATA = 'https://www.startupuniverse.ch/api/1.0/de/counters/get/{0}'
RNG = (1,200) # seems to be between 10 and 150

# dashboard url constructing
URL_DASH = 'https://www.countee.ch/app/de/counter/{0}'
URL_DATA = 'https://www.startupuniverse.ch/api/1.0/de/counters/get/{0}'

# output generation
CSV_PATH = 'results.csv'
JSON_PATH = 'results.json'

MARKDOWN_TABLE = 'RESULTS.md'


#MARKDOWN_TEMPLATE = MARKDOWN_TEMPLATE.format()