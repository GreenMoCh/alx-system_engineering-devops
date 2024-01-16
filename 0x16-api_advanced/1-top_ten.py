#!/usr/bin/python3
"""Top Ten"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts[:10]:
            print(post['data']['title'])
    elif response_status_code == 404:
        print(None)
    else:
        print("Error: {}".format(response.status_code))
