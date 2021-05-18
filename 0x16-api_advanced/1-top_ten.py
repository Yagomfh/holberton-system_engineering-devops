#!/usr/bin/python3
"""Module for advance API exercices"""
import requests


def top_ten(subreddit):
    """Fetchers top 10 posts of a subreddit"""
    headers = {'User-agent': 'Unix:0-subs:v1'}
    url = ("https://www.reddit.com/r/" +
           subreddit +
           "/hot/.json?limit=10")
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        for elem in response.json()['data']['children']:
            print(elem['data']['title'])
