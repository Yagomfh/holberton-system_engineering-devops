#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys
import json
import csv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    call_url = url + 'users/?id=' + user_id
    employee = json.loads(requests.get(call_url).text)
    call_url = url + 'todos/?userId=' + user_id
    total_tasks = json.loads(requests.get(call_url).text)

    data_file = open(user_id + '.csv', 'w')
    csv_writer = csv.writer(data_file, quoting=csv.QUOTE_ALL)

    for task in total_tasks:
        row = []
        row.append(str(user_id))
        row.append(employee[0]['username'])
        row.append(task['completed'])
        row.append(task['title'])
        csv_writer.writerow(row)
    data_file.close()
