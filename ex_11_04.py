import re
hand = open("regex_sum_122830.txt")
numbers = []
total = 0
for line in hand:
    line = line.strip()
    stuff = re.findall('([0-9]+)', line)
    numbers = numbers + stuff
for n in numbers:
    total = total + int(n)
print(total)
