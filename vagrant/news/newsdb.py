import psycopg2

DBNAME="news"

def get_most_popular():
  print "Are we here?"
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  select_query = "SELECT title, count(*) as total from articles, log WHERE log.path LIKE concat('%', articles.slug) GROUP BY articles.title ORDER BY total DESC LIMIT 3"
  cursor.execute(select_query)
  return cursor.fetchall()
  db.close()
  return articles