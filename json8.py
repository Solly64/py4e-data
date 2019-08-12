import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'https://world.openfoodfacts.org/api/v0/product/737628064502.json?'

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
    for key, value in js.items():
        print(key,value)
        print('======================new line=============================')
        print('++++++++++++++++++++++++++++++++++++++++++++')
        print(json.dumps(js, indent=4))
        print('################################################')
        js1 = json.dumps(js, indent=4)
        print(js1)
