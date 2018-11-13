import psycopg2

DBNAME = "news"


def get_result(db_query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(db_query)
    return cursor.fetchall()
    db.close()
    return result


def check_for_views():
    views = {
        "sum_view": "CREATE OR REPLACE VIEW sum_view" +
                    " AS SELECT date AS day, SUM(status_count)" +
                    " AS status_sum from error_view GROUP BY day;",
        "error_view": "CREATE OR REPLACE VIEW error_view" +
                      " AS SELECT DATE(time), status, count(status) as" +
                      " status_count from log GROUP BY DATE(time), status;",
        "author_view": "CREATE OR REPLACE VIEW author_view" +
                       " AS SELECT authors.name, articles.title," +
                       " count(log.path) AS view_count FROM authors,"
                       " articles, log WHERE authors.id = articles.author" +
                       " and log.path LIKE concat('%', articles.slug)" +
                       " GROUP BY authors.name, articles.title, log.path;",
    }
    all_current_views = "select viewname from pg_catalog.pg_views"
    results = get_result(all_current_views)
    for view in sorted(views.keys()):
        view_as_tuple = (view,)
        if view_as_tuple not in results:
            create_views(view, views[view])


def create_views(view_key, view_value):
    print("Creating view for %s..." % (view_key))
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(view_value)
    db.commit()
    db.close()
    print("View for %s complete." % (view_key))


def get_articles():
    select_query = """
        SELECT title, count(*) as view_count from articles, log
        WHERE log.path LIKE concat('%', articles.slug)
        GROUP BY articles.title ORDER BY view_count DESC LIMIT 3"""
    articles = get_result(select_query)
    return articles


def get_authors():
    select_query = """SELECT name, SUM(view_count)
    AS total_views FROM author_view GROUP BY name
    ORDER BY total_views DESC;"""
    authors = get_result(select_query)
    return authors


def get_errors():
    select_query = """SELECT * FROM
    (SELECT date, ROUND(status_count * 100 / status_sum, 2)
    AS percentage FROM error_view, sum_view WHERE date = day
    AND status = '404 NOT FOUND') AS percentages GROUP BY date,
    percentage HAVING percentage > 1;"""
    errors = get_result(select_query)
    return errors
