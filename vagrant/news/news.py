from flask import Flask, request, redirect, url_for

# from newsdb import get_answers

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
    <h3>On which days did more than 1% of requests lead to errors?</h3>
  </body>
</html>
'''

@app.route('/', methods=['GET'])
def main():
  print "Hey"
  return HTML

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)