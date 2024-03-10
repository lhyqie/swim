import sqlite3

def create_fake_db():
  connection = sqlite3.connect('swimmers_test.db')
  with open('schema.sql') as f:
    connection.executescript(f.read())
  cur = connection.cursor()
  cur.execute("INSERT INTO swimmers (id, fastest_time) VALUES (?, ?)",
              ('abby-chan', '50 Y Free:23.37,100 Y Free:51.86')
              )
  cur.execute("INSERT INTO swimmers (id, fastest_time) VALUES (?, ?)",
              ('fake-swimmer', '50 Y Free:23.37,100 Y Free:51.86')
              )
  res = cur.execute("SELECT * FROM swimmers")
  print(res.fetchall())
  connection.commit()
  connection.close()

create_fake_db()
