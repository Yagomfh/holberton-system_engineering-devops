#!/usr/bin/python3
"""Module for advance API exercices"""
import requests

url = 'http://reddit.com/r/{}/hot.json'

def count_words(subreddit, word_list, after=None, res={}):
    """Fetchers all hot posts of a subreddit"""
    headers = {"User-Agent": "Unix:0-subs:v1"}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != 'null':
            params['after'] = after
        else:
            res = res = sorted(res.items(), key=lambda x: x[1], reverse=True)
            sorted_dict = {k: v for k, v in res}
            for k in sorted_dict:
                print("{}: {}".format(k, sorted_dict[k]))
            return
    response = requests.get(url.format(subreddit),
                            headers=headers,
                            params=params)
    if response.status_code != 200:
        print()
        return None
    for elem in response.json()['data']['children']:
        title = elem['data']['title'].lower().split()
        for word in word_list:
            if word in title:
                if word in res:
                    res[word] += 1
                else:
                    res[word] = 1
    after = response.json()['data']['after']
    if after is None:
        after = 'null'
    return count_words(subreddit, word_list, after, res)
