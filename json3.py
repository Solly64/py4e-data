from urllib.request import urlopen
import json
total = 0
sum = 0


html = input('Enter location:')

htmls = urlopen(html).read()
print("Retrieved:", len(htmls), 'Characters')
jsonn = json.loads(htmls)
print(len(jsonn))
print(type(jsonn))
print(jsonn)
for jsonns in jsonn:
    print('#########################')
    print(jsonns)
    print('====================================')
    word = jsonn[jsonns]
    print(word)
    print('************************')
    print(len(word))
    print(type(word))
    print(word[1])
