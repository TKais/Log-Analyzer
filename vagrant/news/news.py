from flask import Flask, request, redirect, url_for

from newsdb import get_most_popular_articles

app = Flask(__name__)

HTML = '''\
  <!DOCTYPE html>
  <html>
    <head>
      <title>Log Analyzer</title>
      <style>
        h3, p { text-align: center; }
        p { margin-bottom: 3rem; }
        
      </style>
    </head>
    <body>
      <h1>Log Analyzer</h1>
      <h3>What are the most popular three articles of all time?</h3>
      <h3>Who are the most popular article authors of all time?</h3>
      <h3>On which days did more than 1 percent of requests lead to errors?</h3>
      %s
    </body>
  </html>
'''

ARTICLE = '''\
  <div class=post><em class=date>%s</em><br>%s</div>
'''

@app.route('/', methods=['GET'])
def main():
  result = get_most_popular_articles()
  articles = "".join(ARTICLE % (title, view_count) for title, view_count in result)
  html_output = HTML % articles
  return html_output

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)