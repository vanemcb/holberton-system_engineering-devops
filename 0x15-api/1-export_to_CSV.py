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
        data.append([(name.get('id')), name.get('username'), items.get(
            'completed'), items.get('title')])

    # h = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    # for items in tasks:
    #     dict_data = {h[0]: str(name.get('id')), h[1]: name.get(
    #         'username'), h[2]: items.get(
    #             'completed'), h[3]: items.get('title')}
    #     data.append(dict_data)

    with open('{}.csv'.format(name.get('id')), 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write multiple rows
        writer.writerows(data)
