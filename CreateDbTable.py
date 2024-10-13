import pymysql as sql

Connection = sql.connect(host="localhost", user="root", database="pythondb", password="12345")
Cursor = Connection.cursor()
CreateTable = """
create table if not exists MyInfo(
    FavNum int primary key, 
    Name varchar(30) not null,
    Age int not null,
    PhoneNumber int not null
);
"""
DescTable = """
desc MyInfo;
"""
try:
    Cursor.execute(CreateTable)
    print(f"Table created")
    Cursor.execute(DescTable)
    for data in Cursor.fetchmany(3):
        print(f"-->{data}")
    Connection.close()
except Exception as e:
    print(f"Error Occured --> {e}")

