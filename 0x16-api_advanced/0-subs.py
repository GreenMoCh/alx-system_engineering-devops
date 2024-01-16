#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subs for a give subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headres=headers)

    if response.status_code == 200:
        data = response.json()
        subs_count = data['{}']['{}'].format(data, subscribers) 
        return subs_count
    elif response.status_code == 404:
        return 0
