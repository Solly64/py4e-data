#Input the information into SQl or SAS
import sqlite3

conn = sqlite3.connect('mrt21.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS name;
DROP TABLE IF EXISTS gender;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    gender TEXT UNIQUE
);

CREATE TABLE Topic (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    gender  TEXT UNIQUE
)
''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'C:/Users/Solly/Desktop/data-science/July2.xlsx'
fh = open(fname)

gender = str(rows)
name = str(row)

#print(gender,name)

cur.execute('''INSERT OR IGNORE INTO User (name, gender)
        VALUES ( ?, ? )''', ( name, gender ) )
cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
user_id = cur.fetchone()

cur.execute('''INSERT OR IGNORE INTO Topic (gender)
    VALUES ( ? )''', ( gender, ) )
cur.execute('SELECT id FROM Topic WHERE gender = ? ', (gender, ))
crisis = cur.fetchone()[0]

sqlstr = '''SELECT User.name, user.gender
    FROM name JOIN gender
    ORDER BY User.name LIMIT 3'''
print(sqlstr)

#for rower in cur.execute(sqlstr):
 #   print(str(rower[0]),str(rower[1]),str(rower[2]),str(rower[3]))


conn.commit()

cur.close()
#C:/Users/Solly/Desktop/py4e/mbox.txt
