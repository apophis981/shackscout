import sqlite3

class DBhelper(Homescraper):
    print(dbname)
    conn = sqlite3.connect('example.db')
