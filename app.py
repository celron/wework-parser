import urllib2
import json

def readGeoGroupings():
    response = urllib2.urlopen('https://api-proxy.wework.com/locations/api/v1/geogroupings')
    a = response.read()
    return json.loads(a)


a = readGeoGroupings()
print a
b = a['geogroupings']
for location in b:
    print location.keys()
    for key in location.keys():
        print key,'##',location[key]
