import psycopg2

DBNAME="news"

def _connect_to_db():
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  return (db, cursor)

def get_most_popular():
  db = _connect_to_db()[0]
  cursor = _connect_to_db()[1]

  select_query = "select author from articles"
  cursor.execute(select_query)
  return cursor.fetchall()
  db.close()
  return articles