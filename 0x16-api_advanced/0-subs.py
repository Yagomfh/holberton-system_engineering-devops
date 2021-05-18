#!/usr/bin/python3
"""Module for advance API exercices"""
import requests


def number_of_subscribers(subreddit):
    """Fetchers number of subs of a subreddit"""
    headers = {"User-Agent": "Unix:0-subs:v1"}
    url = "https://www.reddit.com/r/" + subreddit + "/about/.json"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
