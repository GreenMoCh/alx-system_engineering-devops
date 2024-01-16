#!/usr/bin/python3
"""Recurse it!"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list contaning the ttles of all hot articles fo a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('childer', [])

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        print("None")
        return None
    else:
        return None
