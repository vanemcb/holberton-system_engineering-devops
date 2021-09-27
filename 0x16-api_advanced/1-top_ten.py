#!/usr/bin/python3
""" unction that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit """

import requests


def top_ten(subreddit):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
            Safari/537.36"}
    data = requests.get(
        'http://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=headers).json()

    if data.status_code != 200:
        return None
    else:
        for index in range(0, 10):
            print(data.get('data').get(
                'children')[index].get('data').get('title'))
