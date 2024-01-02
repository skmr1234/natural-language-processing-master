import sqlite3
class SQL:
    def __init__(self, database):
        self.conn= sqlite3.connect(database)
        self.cursor= self.conn.cursor()
    def exec(self, query):
        d= self.cursor.execute(query)
        #self.conn.commit()
        return d.fetchall()
    def __del__(self):
        self.conn.close()