import psycopg2

name = "TestName"
surname = "TestSurname"

conn = psycopg2.connect(
    database="tutorial_db",
    user="postgres",  
    password="1234",  
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("CREATE TABLE users (id serial PRIMARY KEY, name VARCHAR, surname VARCHAR);")
cur.execute("INSERT INTO users (name, surname) VALUES (%s, %s);", (name, surname))

conn.commit()

cur = conn.cursor()

cur.execute("SELECT * FROM users")

datas = cur.fetchall()

for data in datas:
    print(data)

conn.close()
