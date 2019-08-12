import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    print('==== Next Line ====')
    print(data)
    print('===============3rd Line===============')
    js = json.loads(data)
    for jsonn in js['results']:
        print(jsonn)
        print(json.dumps(js, indent=4))
        latss = jsonn["place_id"]
        lan = jsonn["place_id"]
        print('place id', latss, lan)
