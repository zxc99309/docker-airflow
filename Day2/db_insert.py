# db_insert.py
import psycopg2

conn = psycopg2.connect(
    dbname='mydb',
    user='postgres',
    password='1234',
    host='localhost',  # Docker container 網址
    port=5432
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INT NOT NULL
    );
""")

cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("來瑋", 26))

conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
