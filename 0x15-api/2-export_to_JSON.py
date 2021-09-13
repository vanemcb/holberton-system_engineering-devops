#!/usr/bin/python3
""" Script that exports data in the CSV format """

import json
import requests
from sys import argv

if __name__ == "__main__":

    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            argv[1])).json()

    tasks_list = []
    for items in tasks:
        tasks_dict = {"task": items.get('title'), "completed": items.get(
            "completed"), "username": name.get('username')}
        tasks_list.append(tasks_dict)

    final_dict = {name.get('id'): tasks_list}
    with open('{}.json'.format(name.get('id')), 'w', encoding='UTF8') as f:
        json.dump(final_dict, f)
