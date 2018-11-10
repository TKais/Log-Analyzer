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
    write_to_file(question, 'w', results)

def get_most_popular_authors():
  results = get_authors()
  question = 'Who are the most popular article authors of all time?'
  write_to_file(question, 'a', results)

def write_to_file(question, mode, results):
  new_file = open('output.txt', mode)
  new_file.write('\n' + question + '\n \n')
  print(question + '\n')
  for result in results:
    print('%s : %d views' % (result[0], result[1]))
    new_file.write('%s -- %d views \n' % (result[0], result[1]))
  new_file.close()

def start():
  check_for_view()
  get_most_popular_articles()
  get_most_popular_authors()

start()