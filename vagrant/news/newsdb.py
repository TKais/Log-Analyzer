import psycopg2

DBNAME="news"

def get_most_popular_articles():
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  select_query = "SELECT title, count(*) as view_count from articles, log WHERE log.path LIKE concat('%', articles.slug) GROUP BY articles.title ORDER BY view_count DESC LIMIT 3"
  cursor.execute(select_query)
  return cursor.fetchall()
  db.close()
  return articles