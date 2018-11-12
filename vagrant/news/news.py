#!/usr/bin/env python3

from newsdb import get_articles, get_authors, get_errors, check_for_views
from pathlib import Path


def check_for_output_file():
    print("\nChecking if text file 'output.txt' exists...")
    output_file = Path("./output.txt")
    if output_file.is_file():
        print("\nFile 'output.txt' exists! Here are the results: ")
        file = open("output.txt", "r")
        print(file.read())
        file.close()
    else:
        new_file = open("output.txt", "w+")
        new_file.close()
        print("Text file 'output.txt' created. " +
              "Please open this file once script has finished running. \n")
        run_db_queries()


def run_db_queries():
    print("Running database queries. This may take a moment... \n")
    queries = {
        "a - articles": {
            "question": "What are the most popular" +
            " three articles of all time?",
            "results": get_articles()
        },
        "b - authors": {
            "question": "Who are the most popular" +
            " article authors of all time?",
            "results": get_authors()
        },
        "c - errors": {
            "question": "On which days did more than" +
            " 1 percent of requests lead to errors?",
            "results": get_errors()
        },
    }

    for query in sorted(queries.keys()):
        write_to_file(queries[query]["question"], queries[query]["results"])


def write_to_file(question, results):
    new_file = open("output.txt", "a")
    new_file.write("\n \n ===" + question + "\n \n")
    print("\n \n ===" + question + "\n \n")
    for result in results:
        if 'percent' in question:
            print("%s -- %.2f%% of errors" % (result[0], result[1]))
            new_file.write("%s -- %.2f%% of errors \n" %
                           (result[0], result[1]))
        else:
            print("%s -- %d views" % (result[0], result[1]))
            new_file.write("%s -- %d views \n" % (result[0], result[1]))
    new_file.close()


def start():
    check_for_views()
    check_for_output_file()
    print("\n \n ***Database queries complete!*** \n")


start()
