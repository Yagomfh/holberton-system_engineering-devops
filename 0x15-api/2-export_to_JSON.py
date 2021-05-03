#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = sys.argv[1]
    call_url = url + 'users/?id=' + user
    employee = json.loads(requests.get(call_url).text)
    call_url = url + 'todos/?userId=' + user
    total_tasks = json.loads(requests.get(call_url).text)

    tasks = []
    data = {user: tasks}

    for task in total_tasks:
        tmp = {'task': task['title'],
               'completed': task['completed'],
               'username': employee[0]['username']}
        tasks.append(tmp)
    with open(user + ".json", "w") as outfile:
        json.dump(data, outfile)
