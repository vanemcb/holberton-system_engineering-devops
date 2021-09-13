#!/usr/bin/python3
""" script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
from sys import argv

if __name__ == "__main__":

    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])).json()

    count = 0
    list_tasks = []
    for items in tasks:
        if items.get('completed') == True:
            list_tasks.append(items.get('title'))
            count += 1

    print('Employee {} is done with tasks({}/{}):'.format(name.get('name'),
          count, len(tasks)))

    for i in list_tasks:
        print('\t {}'.format(i))
