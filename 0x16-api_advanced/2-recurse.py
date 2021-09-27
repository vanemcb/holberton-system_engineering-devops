#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit  """
import requests


def recurse(subreddit, hot_list=[], after=""):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
            Safari/537.36"}
    data = requests.get(
        'http://www.reddit.com/r/{}/hot.json?limit=30&after={}'.format(
            subreddit, after), headers=headers)

    if data.status_code != 200:
        return None
    else:
        after = data.json().get('data').get('after')
        if after is not None:
            for index in range(0, 30):
                hot_list.append(data.json().get('data').get(
                    'children')[index].get('data').get('title'))
            recurse(subreddit, hot_list, after)
        return(hot_list)
