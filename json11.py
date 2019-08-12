import json
import sqlite3

conn = sqlite3.connect('json11.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Topic;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    key    TEXT UNIQUE,
    answer  TEXT UNIQUE
);

CREATE TABLE Topic (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    answer  TEXT UNIQUE
)
''')


fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'worldfood.txt'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#######THE JSON FILE HAS DICTIONARIES, TUPLES, AND LIST!
str_data = open(fname).read()
json_data = json.loads(str_data)
print(type(json_data))
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(json_data["status"])
js = json_data['product']
print(js)
print('-------------NEW LINE------------------------------------------')
#PUT THE VALUE IN A STRING VALUE SO IT CAN PASS FOR SQL
for key, value in js.items():
    key = str(key)
    answer = str(value)
    print(type(value))
    print('****************************2nd line^^^^^^^^^^^^^^^^^^^^^^^^^')

    cur.execute('''INSERT OR IGNORE INTO User (key, answer)
        VALUES ( ?, ? )''', ( key, answer ) )
    cur.execute('SELECT id FROM User WHERE key = ? ', (key, ))
    user_id = cur.fetchone()

    cur.execute('''INSERT OR IGNORE INTO Topic (answer)
        VALUES ( ? )''', ( answer, ) )
    cur.execute('SELECT id FROM Topic WHERE answer = ? ', (answer, ))
    food = cur.fetchone()[0]




    conn.commit()




cur.close()

#    print('======================new line=============================')
#    print(key)
#    print('======================new line=2============================')
#    print('++++++++++++++++++++++++++++++++++++++++++++')
#    print(type(key))
#    print('################################################')
#    js1 = json.dumps(json_data, indent=4)
#    print(js1)
