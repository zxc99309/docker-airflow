import pandas as pd
import psycopg2
import time

# 等待資料庫啟動
time.sleep(5)

df = pd.read_csv("users.csv")

conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="1234",
    host="db",
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

for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO users (name, age) VALUES (%s, %s)",
        (row['name'], int(row['age']))
    )

conn.commit()
cur.close()
conn.close()

print("✅ 資料已成功寫入 PostgreSQL")
