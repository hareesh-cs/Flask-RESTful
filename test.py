import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_user = "INSERT INTO users VALUES(?,?,?)"
users = [
    (1, "Hareesh", "1234"),
    (2, "Sameer", "1234"),
    (3, "Nikhil", "5678"),
]
cursor.executemany(insert_user, users)

select_query = "SELECT * from users"
cursor.execute(select_query)
records = cursor.fetchall()

for record in records:
    print(record)

conn.commit()
conn.close()
