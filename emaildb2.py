


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Nutrients.csv'
fh = open(fname)
for line in fh:
    pieces = line.split(',')
    email = pieces[0]
    fire = pieces[2]
    water = pieces[4]
    print(water)
