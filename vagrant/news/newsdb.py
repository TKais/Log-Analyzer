import psycopg2

DBNAME="news"

def get_result(db_query):
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  cursor.execute(db_query)
  return cursor.fetchall()
  db.close()
  return result

def get_articles():
  select_query = "SELECT title, count(*) as view_count from articles, log WHERE log.path LIKE concat('%', articles.slug) GROUP BY articles.title ORDER BY view_count DESC LIMIT 3"
  articles = get_result(select_query)
  return articles

def get_authors():
  select_query = "SELECT"
  authors = get_result(select_query)
  return authors