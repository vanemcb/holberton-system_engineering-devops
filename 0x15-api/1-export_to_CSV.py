#!/usr/bin/python3
""" Script that exports data in the CSV format """

import csv
import requests
from sys import argv

if __name__ == "__main__":

    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            argv[1])).json()

    count = 0
    data = []
    for items in tasks:
        data.append([(name.get("id")), name.get('username'), items.get(
            'completed'), items.get('title')])

    with open('{}.csv'.format(name.get('id')), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # write multiple rows
        writer.writerows(data)
