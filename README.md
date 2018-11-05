# Log-Analyzer

A log analyzer that queries a database containing newspaper articles. The log has a database row for each time a reader loaded a web page. Using that information, this analyzer answers the following questions about user activity:

* What are the most popular three articles of all time? Which articles have been accessed the most? The most popular article is listed at the top.
* Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? This is presented as a sorted list with the most popular author at the top.
* On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.


## The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site. 

## Technical Details
This project utilizes the following technologies:

* Python 3
* PostgreSQL
* Psycopg2
* SQL