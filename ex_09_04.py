# Open the file
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
# Put counts in a dictionary so the file can be store
counts = dict()
for line in fh:
    line = line.strip()
    if not line.startswith('From:'): continue
    # Break the line into pieces, so it can be retrieve
    words = line.split()
    email = words[1]
    pieces = email.split(',')
    # The word is in there, just break it up to words and counts to make a histogram
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(word, counts[word])



fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    line = line.strip()
    if not line.startswith('From:'): continue
    words = line.split()
    email = words[1]
    pieces = email.split(',')
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(word, counts[word])
