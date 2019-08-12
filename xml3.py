from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
total = 0
sum = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location:')

xmll = urlopen(address, context=ctx).read()
print('Retrieved:', len(xmll), 'Characters')
print(xmll.decode())
tree = ET.fromstring(xmll)
lst = (tree.findall('.//count'))
print(type(lst))
print('Count:',  len(lst))
for count in lst:
    sum += int(count.text)
    total += 1
    print('Count:', total)
    print('Sum:', sum)

    # DON'T GIVE UP, YOU ARE GETTING BETTER WITH PYTHON EVERYDAY. I JUST NEED MORE PRACTICE
