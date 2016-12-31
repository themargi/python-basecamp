import urllib
import json
googleapiurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

fileHandle = open('PplNplaces.txt')
map = dict()
for line in fileHandle:
	items = line.strip().split(',')
	map[items[0]]=items[1]

for name, place in map.items():
	url = googleapiurl + urllib.urlencode({'sensor': 'false', 'address': place})
	#print url
	placeData = urllib.urlopen(url).read()
	js = json.loads(str(placeData))
	#print json.dumps(js, indent=4)
	print name, 'lives in', js['results'][0]['formatted_address']