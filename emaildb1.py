import sqlite3

conn = sqlite3.connect('emaildb1.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Nutrition;

CREATE TABLE Nutrition (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nutrient_name TEXT UNIQUE,
    grams_output TEXT UNIQUE
)
''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Nutrients.csv'
fh = open(fname)
for line in fh:
    pieces = line.split(',')
    id = pieces[0]
    nutrient_name = pieces[2]
    grams_output = pieces[4]

    cur.execute('''INSERT OR IGNORE INTO Nutrition (nutrient_name, grams_output)
        VALUES ( ?, ? )''', ( nutrient_name, grams_output ) )
    cur.execute('SELECT id FROM Nutrition WHERE nutrient_name = ? ', (nutrient_name, ))
    user_id = cur.fetchone()

    conn.commit()

# https://www.sqlite.org/lang_select.html



cur.close()
