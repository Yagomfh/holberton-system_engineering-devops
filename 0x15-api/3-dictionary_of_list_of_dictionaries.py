#!/usr/bin/python3
"""Gather data from an API"""
import requests
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employees = json.loads(requests.get(url + 'users').text)

    data = {}

    for employee in employees:
        call_url = url + 'todos/?userId=' + str(employee['id'])
        total_tasks = json.loads(requests.get(call_url).text)
        tasks = []
        for task in total_tasks:
            tmp = {'task': task['title'],
                   'completed': task['completed'],
                   'username': employee['username']}
            tasks.append(tmp)
        data[employee['id']] = tasks

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(data, outfile)
