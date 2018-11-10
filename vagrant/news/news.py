#!/usr/bin/env python3

from newsdb import get_articles
from pathlib import Path

def get_most_popular_articles():
  results = get_articles()
  output_file = Path('./output.txt')
  question = 'What are the most popular three articles of all time?'
  if output_file.is_file():
    print("IN READ MODE")
    contents = output_file.read()
    print(contents)
  else:
    write_to_file(question, results)

def write_to_file(question, results):
  new_file = open('output.txt','w')
  new_file.write(question + '\n')
  print("IN WRITE MODE")
  for result in results:
    print(result[0])
    print(result[1])
    new_file.write('%s -- %d views \n' % (result[0], result[1]))
  new_file.close()


get_most_popular_articles()