fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.strip()
    if not line.startswith('From '): break
    words = line.split()
    email = words[1]
    pieces = email.split(',')
    for line in fh:
        count = count + 1
print(words[1],'There were', count, 'lines in the file with From as the first word')
