from urllib.request import urlopen
import json
total = 0
counts = dict()

html = input('Enter location:')

htmls = urlopen(html).read()
print("Retrieved:", len(htmls), 'Characters')
jsonn = json.loads(htmls)
print(len(jsonn))
print(type(jsonn))
print(len(jsonn['stores_debug_tags']))
comment_sum = 0
for jsonns in jsonn['stores_debug_tags']:
    print('#########################')
    print(type(jsonns))
    print(jsonns)
    comment_sum = comment_sum + int(jsonns['count'])
    print('Sum:', comment_sum)
