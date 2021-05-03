#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = sys.argv[1]
    call_url = url + 'users/?id=' + user
    employee = json.loads(requests.get(call_url).text)
    call_url = url + 'todos/?userId=' + user
    total_tasks = json.loads(requests.get(call_url).text)
    call_url = url + 'todos/?userId=' + user + '&completed=true'
    done_tasks = json.loads(requests.get(call_url).text)
    print("Employee {} is done with tasks({}/{}):\
".format(employee[0]['name'], len(done_tasks), len(total_tasks)))
    for task in done_tasks:
        print("\t {}".format(task['title']))
