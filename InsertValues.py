import pymysql as sql

Connection = sql.connect(host="localhost", user="root", database="pythondb", password="12345")
Cursor = Connection.cursor()
Insert = f"""insert into myinfo values({21}, 'Mohana Krishnan', {21});"""
ShowTable = """select * from myinfo;"""
try:
    Cursor.execute(Insert)
    print(f" --> Table Created")
    ViewTable = Cursor.execute(ShowTable)
    for i in Cursor.fetchall():
        print(i)
    Connection.commit()
except Exception as e:
    print(f"Error Occurred --> {e}")

