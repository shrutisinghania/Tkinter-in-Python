import sqlite3

def createTable():
    conn = sqlite3.connect('contacts.db')
    conn.execute('DROP table IF EXISTS ABC')
    conn.execute('''CREATE TABLE ABC
             (Id INTEGER PRIMARY KEY AUTOINCREMENT,
             Name TEXT NOT NULL,
             Phone CHAR(50) NOT NULL)''')
    print ("Table created successfully")
    conn.commit()
    conn.close()

def updateTable(name, phn, Id):
    conn = sqlite3.connect('contacts.db')
    sql = "UPDATE ABC SET Name='"+name+"' ,Phone='"+phn+"' WHERE id="+str(Id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    
def delFromTable(Id):
    conn = sqlite3.connect('contacts.db')
    sql = 'DELETE FROM ABC WHERE id='+ str(Id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def insertInTable(name, phn):
    conn = sqlite3.connect('contacts.db')
    sql = ''' INSERT INTO ABC(Name,Phone)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, phn))
    conn.commit()
    conn.close()
    
def readFromTable(Id):
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    sql = "SELECT Name,Phone FROM ABC WHERE Id=" + str(Id)
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        return(row)
    
def readAllTable():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("SELECT Name,Phone FROM ABC")
    rows = cur.fetchall()
    conn.close()
    r = [list(ele) for ele in rows]
    return(r)

def insertAllInTable(contactlist):
    conn = sqlite3.connect('contacts.db')
    sql = ''' INSERT INTO ABC(Name,Phone)
              VALUES(?,?) '''
    cur = conn.cursor()
    for a in contactlist:
        cur.execute(sql, (a[0], a[1]))
    conn.commit()
    conn.close()
    
def readByName(name):
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    sql = "SELECT id FROM ABC WHERE Name= '" + name + "'"
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        return(int(row[0]))