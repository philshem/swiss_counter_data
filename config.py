


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

MARKDOWN_FILE = 'RESULTS.md'
MARKDOWN_TEMPLATE = '''

## Results table

{0}

'''


#MARKDOWN_TEMPLATE = MARKDOWN_TEMPLATE.format()