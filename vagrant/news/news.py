#!/usr/bin/env python3

from newsdb import get_articles, get_authors, check_for_view
from pathlib import Path

def get_most_popular_articles():
  results = get_articles()
  output_file = Path('./output.txt')
  question = 'What are the most popular three articles of all time?'
  if output_file.is_file():
    file = open('output.txt', 'r')
    print(file.read())
    file.close()
  else:
    write_to_file(question, results)

def get_most_popular_authors():
  results = get_authors()
  file = open('output.txt','a')
  for result in results:
    # print(result[0] + ' : ' + result[1] + ' views')
    file.write('%s -- %d views \n' % (result[0], result[1]))
  file.close()
  print(results)

def write_to_file(question, results):
  new_file = open('output.txt','w')
  new_file.write(question + '\n')
  print(question)
  for result in results:
    print(result[0] + ' : ' + result[1] + ' views')
    new_file.write('%s -- %d views \n' % (result[0], result[1]))
  new_file.close()

def start():
  check_for_view()
  get_most_popular_articles()
  get_most_popular_authors()

start()