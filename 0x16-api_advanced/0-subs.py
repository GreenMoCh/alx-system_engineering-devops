#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subs for a give subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headres=headers, allow_redirets=False)

    if response.status_code == 404:
        return 0
    data = response.json().get("data") 
    return data.get("subscribers")
    
