import psycopg2

DBNAME="news"

def get_most_popular():
  print "Are we here?"
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();

  select_query = "SELECT path, count(*) AS num FROM log GROUP BY path ORDER BY num DESC LIMIT 4 OFFSET 1"
  # 1. ('/article/candidate-is-jerk', 338647L)
  # 2. ('/article/bears-love-berries', 253801L)
  # 3. ('/article/bad-things-gone', 170098L)
  # "SELECT path, count(*) AS num FROM log GROUP BY path ORDER BY num DESC LIMIT 4 OFFSET 1"
  cursor.execute(select_query)
  return cursor.fetchall()
  db.close()
  return articles