fname = input('Enter File Name')
fhand = open('words.txt')
fread = fhand.read()
for fread in  fhand:
        fread = fread.strip()
        print(fread.upper())
