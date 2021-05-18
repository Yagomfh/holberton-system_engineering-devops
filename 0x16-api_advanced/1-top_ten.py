#!/usr/bin/python3
"""Module for advance API exercices"""
import requests


def top_ten(subreddit):
    """Fetchers top 10 posts of a subreddit"""
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; \
    CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 \
    (KHTML, like Gecko) Mobile/15E148"}
    url = ("https://www.reddit.com/r/" +
           subreddit +
           "/hot/.json?count=10&limit=10")
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 302:
        for elem in response.json()['data']['children']:
            print(elem['data']['title'])
    return None
