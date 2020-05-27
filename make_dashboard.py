
import json
import config

keep_list = ('sport','schwim','freibad','hallenbad','fitness','kletter')

with open(config.JSON_PATH,'r') as fp:
	data = json.load(fp)


html_head = '''<html class="no-js">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
      <div class="wrapper">

'''
html_tail = '''</div>
    </body>
</html>
'''

# <iframe src="..." style="position: relative; left: -100px; top: -100px">
template = '''
       <iframe src="{0}" width="300" height="250" noresize=yes frameborder=0 marginheight=0 marginwidth=0 scrolling="no"/></iframe>
       '''
			  

html = ''
html += html_head

#print (sorted(data, key = lambda i: i['index']))
#print(data)

for x in data:

	name_list = x.get('name').lower()#.split()
	if any([y for y in keep_list if y in name_list]):
		#tmp = '<div style="width: 500px; height: 500px; overflow: hidden">'
		html += template.format(x.get('url_dashboard')) 
		#html + '</div>'+ '\n'

html += html_tail

with open('html/index.html','w') as fp:
	fp.write(html)

		#print (x.get('name'))
		#print (x.get('url_dashboard'))
