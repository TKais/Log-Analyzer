# Log-Analyzer

A log analyzer that queries a database containing newspaper articles. The log has a database row for each time a reader loaded a web page. Using that information, this analyzer answers the following questions about user activity:

* What are the most popular three articles of all time? Which articles have been accessed the most? The most popular article is listed at the top.
* Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? This is presented as a sorted list with the most popular author at the top.
* On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.


## The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site. 

## Before running the Log-Analyzer

* [Install VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Install Vagrant](https://www.vagrantup.com/downloads.html)
* This project is meant to be ran with Python 3.4 or higher

## Running the Log-Analyzer

* Clone Log-Analyzer repo
* Once cloned, change into the directory for the Log-Analyzer project and Run the command `cd vagrant`
* Run the command `vagrant up`
* Run the command `vagrant ssh`
* Run the command `cd /vagrant/news`
* Run the command `pip3 install psycopg2`
* Run the command `psql -d news -f newsdata.sql`
* Run the command `python3 news.py`
* Once the script has logged "***Database queries complete!***" in the terminal, you can see the answers in the logs in your terminal, or open the file `output.txt` in `Log-Analyzer/vagrant/news/output.txt`.

## Project Views
This project utilizes 3 views, which are created for you:

* author_view: 

  | Column     | Type    |
  | ---------  | -------:|
  | name       | text    |
  | title      | text    |
  | view_count | Integer |

* error_view: 

  | Column      | Type    |
  | ---------   | -------:|
  | date        | date    |
  | status      | text    |
  | staus_count | Integer |

* sum_view: 

  | Column      | Type    |
  | ---------   | -------:|
  | date        | date    |
  | status      | text    |
  | status_sum  | Integer |

## Technical Details
This project utilizes the following technologies:

* Python 3
* PostgreSQL
* Psycopg2
* SQL