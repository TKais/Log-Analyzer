import psycopg2

DBNAME="news"

def get_result(db_query):
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  cursor.execute(db_query)
  return cursor.fetchall()
  db.close()
  return result

def check_for_view():
  check_for_view = "select viewname from pg_catalog.pg_views where viewname = 'author_view'";
  result = get_result(check_for_view)
  print(result)
  if len(result) == 0:
    create_view()

def create_view():
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor();
  view = "CREATE VIEW author_view AS SELECT authors.name, articles.title, count(log.path) AS view_count FROM authors, articles, log WHERE authors.id = articles.author and log.path LIKE concat('%', articles.slug) GROUP BY authors.name, articles.title, log.path;"
  cursor.execute(view)
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
  select_query = ""
  errors = get_result(select_query)
  return errors