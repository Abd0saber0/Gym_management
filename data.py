import sqlite3
class Db:
    def __init__(self):
        DATA_PATH='./data_base/data.db'
        self.conn= sqlite3.connect(DATA_PATH)
        self.cursor=self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS members
            (f_name TEXT, l_name TEXT, id TEXT, status Text)    
            ''')
        self.conn.commit()
    def insert_data(self,f_name,l_name,member_id,status):
        self.cursor.execute("INSERT INTO members VALUES(?,?,?,?)",(f_name, l_name, member_id,status))
        self.conn.commit()
    def fetch(self):
        self.cursor.execute("SELECT ROWID, f_name, l_name, id,status FROM members") 
        #(f_name, l_name,id) ---> بيرجع tuple داخل tuple
        return self.cursor.fetchall()
    def remove(self,item_id):
        self.cursor.execute('DELETE FROM members WHERE ROWID= ?',(item_id,))
        self.conn.commit()
    def close(self):
        self.cursor.close()
        self.conn.close()