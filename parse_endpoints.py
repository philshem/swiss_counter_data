
import json
import requests
import pandas as pd

# internal params
import config

'''
1. collect list of endpoints for open places' counters
2. write markdown table of clickable links (csv, json too)
'''

def parse_endpoints():

	if config.GET_ENDPOINTS:
		get_endpoints()

	full_list = []

	with open(config.METADATA_FILE,'r') as fp:
		data = json.load(fp)

	for x in data:
		y = x.get('data', False).get('response', False).get('data', False)#.get('slug', False)
		if y:

			slug = y.get('slug',None).strip()
			name = y.get('name',None).strip()
			index = y.get('id',None)

			# so that there are no empty cells in table
			if len(name) == 0:
				name = slug

			# can expand columns here
			#slug_badi_info = y.get('slug_badi_info',None)

			url_dashboard = config.URL_DASH.format(slug)
			url_data = config.URL_DATA.format(index)
			full_list.append({'index': index, 'name' : name, 'slug': slug, 'url_dashboard' : url_dashboard, 'url_data' : url_data})

	df = pd.DataFrame(full_list).set_index('index')
	
	# dump to csv, if param set to True
	if config.CSV_PATH:
		df.to_csv(config.CSV_PATH)

	if config.JSON_PATH:
		df.reset_index().to_json(config.JSON_PATH, orient='records', indent=True)

	# prepare to process for markdown
	df['url_dashboard'] = df.apply(lambda x: wrap_md(x.url_dashboard), axis=1)
	df['url_data'] = df.apply(lambda x: wrap_md(x.url_data), axis=1)

	#del df['slug']
	#del df['url']
	
	md = df.to_markdown()

	# dump to markdown file in repo
	with open(config.MARKDOWN_TABLE,'w') as fp:
		fp.write(md)


#	print(md)

def get_endpoints():

	url_base = config.URL_METADATA

	s = requests.Session()

	good_list = []

	for x in range(config.RNG[0], config.RNG[1]+1):
		url = url_base.format(str(x))
		r = s.get(url)
		data = r.json()
		if data.get('response',False).get('data',False):
			print(url)
			tmp = {'url' : url, 'data' : data}
			good_list.append(tmp)


	# dump to file, path stored in config.py
	with open(config.METADATA_FILE,'w') as fp:
		json.dump(good_list, fp, indent = True)

def wrap_md(link):

	return '[{0}]({0})'.format(link)


if __name__ == '__main__':
	parse_endpoints()

