
# An index of entry-counter status, and availability of open places

I made this list so as some swimming pools open, I'd like an easy index for checking how crowded they are, or if they are no longer allowing entries.

The dashboards for each place are publicly available ([live dashboard](https://www.countee.ch/app/de/counter/c5eb19118e5824)),
![example screenshot](https://raw.githubusercontent.com/philshem/swiss_counter_data/master/screenshot.png)

And the endpoints for the data are available as JSON ([for example](https://www.startupuniverse.ch/api/1.0/de/counters/get/71)).

But as far as I know, are not yet indexed.

The python3 script [`parse_endpoints.py`](https://github.com/philshem/swiss_counter_data/blob/master/parse_endpoints.py):

+ generates list of valid endpoints, saved to [`endpoints.json`](https://raw.githubusercontent.com/philshem/swiss_counter_data/master/endpoints.json)

---

Result files:

## [Markdown Table](https://github.com/philshem/swiss_counter_data/blob/master/RESULTS.md)

## [CSV](https://raw.githubusercontent.com/philshem/swiss_counter_data/master/results.csv)

## [JSON](https://raw.githubusercontent.com/philshem/swiss_counter_data/master/results.json)


All things unofficial. Data is owned by the owners. YMMV.

