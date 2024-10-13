import pymysql as sql

Con = sql.connect(host="localhost", user="root", db="pythondb", password="12345")
Cur = Con.cursor()
Sql = f"""select version();"""
Cur.execute(Sql)
Data = Cur.fetchone()
print(f" --> {Data}")
