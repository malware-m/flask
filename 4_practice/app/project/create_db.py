import sqlite3
conn=sqlite3.connect('site.db') # create site.db if not exist 
cursor=conn.cursor() # create cursor to run sql commands

#  write sql to create table
cursor.execute('''   

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
)

''')

conn.commit()   # to make changed commit it
conn.close()  # close the file 