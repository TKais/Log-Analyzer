import psycopg2

DBNAME="news"

def get_result(db_query):
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  cursor.execute(db_query)
  return cursor.fetchall()
  db.close()
  return result

def create_views():
  views = {
    "author_view": "CREATE OR REPLACE VIEW author_view AS SELECT authors.name, articles.title, count(log.path) AS view_count FROM authors, articles, log WHERE authors.id = articles.author and log.path LIKE concat('%', articles.slug) GROUP BY authors.name, articles.title, log.path;",
    "error_view": "CREATE OR REPLACE VIEW error_view AS SELECT DATE(time), status, count(status) as num from log GROUP BY DATE(time), status;",
    "sum_view": "CREATE OR REPLACE VIEW sum_view AS SELECT date, SUM(num) from error_view GROUP BY date;",
  }
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  for view in views:
    cursor.execute(views[view])
    db.commit()
  db.close()

def get_articles():
  select_query = "SELECT title, count(*) as view_count from articles, log WHERE log.path LIKE concat('%', articles.slug) GROUP BY articles.title ORDER BY view_count DESC LIMIT 3"
  articles = get_result(select_query)
  return articles

def get_authors():
  select_query = "SELECT name, SUM(view_count) AS total_views FROM author_view GROUP BY name ORDER BY total_views DESC;"
  authors = get_result(select_query)
  return authors

def get_errors():
  select_query = "SELECT * FROM (SELECT date, ROUND(num * 100 / sum, 2) AS percentage FROM error_view, sum_view WHERE date = day AND status = '404 NOT FOUND') AS example GROUP BY date, percentage HAVING percentage > 1;"
  errors = get_result(select_query)
  return errors