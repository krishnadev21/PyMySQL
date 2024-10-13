import pymysql as sql

Connection = sql.connect(host="localhost", user="root", database="pythondb", password="12345")
Cursor = Connection.cursor()
Sql = f"""select * from myinfo where Age > {10};"""
try:
    Cursor.execute(Sql)
    Fetch = Cursor.fetchall()
    if not Fetch:
        print(f"Empty Fetch in tuple format --> {Fetch}")
        exit()
    # else:
    for i in Fetch:
        Number = i[0]
        Name = i[1]
        Age = i[2]
        print(f"{Fetch}")
        print(f"Number --> {Number} |, Name --> {Name} |, Age --> {Age} |")
    Connection.commit()
except Exception as e:
    Connection.rollback()
    print(f" Error Occurred --> {e}")