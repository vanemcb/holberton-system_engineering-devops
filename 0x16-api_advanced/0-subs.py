#!/usr/bin/python3
""" Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0. """

import requests


def number_of_subscribers(subreddit):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
            Safari/537.36"}
    data = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(
            subreddit), headers=headers)

    if data.status_code != 200:
        return 0
    else:
        return data.json().get('data').get('subscribers')
