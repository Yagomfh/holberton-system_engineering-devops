#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = sys.argv[1]
    employee = json.loads(requests.get(url + 'users/?id=' + user).text)
    total_tasks = json.loads(requests.get(url + 'todos/?userId=' + user).text)
    done_tasks = json.loads(requests.get(url + 'todos/?userId=' + user + '&completed=true').text)
    print("Employee {} is done with tasks({}/{}):".format(employee[0]['name'],
                                                          len(done_tasks), len(total_tasks)))
    for task in done_tasks:
        print("\t{}".format(task['title']))
