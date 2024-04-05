import sqlite3

def create_db(db_file):
  connection = sqlite3.connect(db_file)
  with open('schema.sql') as f:
    connection.executescript(f.read())
  cur = connection.cursor()
  cur.execute("INSERT INTO swimmers (id, fastest_time) VALUES (?, ?)",
              ('abby-chan', '50 Y Free-23.37|100 Y Free-1:01.86')
              )
  cur.execute("INSERT INTO swimmers (id, fastest_time) VALUES (?, ?)",
              ('fake-swimmer', '50 Y Free-23.37|100 Y Free-1:01.86')
              )
  res = cur.execute("SELECT * FROM swimmers")
  print(res.fetchall())
  connection.commit()
  connection.close()

def clear_table(db_file):
  connection = sqlite3.connect(db_file)
  cur = connection.cursor()
  cur.execute("DELETE FROM swimmers")
  connection.commit()
  connection.close()

# create_db('swimmers_test.db')
# create_db('swimmers.db')
# clear_table('swimmers.db')