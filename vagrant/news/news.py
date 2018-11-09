#!/usr/bin/env python3

from newsdb import get_articles
from pathlib import Path

def get_most_popular_articles():
  result = get_articles()
  output_file = Path('./output.txt')
  question = 'What are the most popular three articles of all time?'
  if output_file.is_file():
    print("IN READ MODE")
    contents = output_file.read()
    print(contents)
  else:
    write_to_file(question, result)

def write_to_file(question, result):
  new_file = open('output.txt','w')
  print("IN WRITE MODE")
  for i in result:
    print(i[0])
    print(i[1])
    new_file.write(question)
    new_file.write('%s : %d' % (i[0], i[1]))
  new_file.close()


get_most_popular_articles()