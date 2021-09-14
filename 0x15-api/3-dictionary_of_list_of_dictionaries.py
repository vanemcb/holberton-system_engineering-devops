#!/usr/bin/python3
""" Script that exports data in the CSV format """

import json
import requests
from sys import argv

if __name__ == "__main__":

    final_dict = {}

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    final_dict = {}
    for user_dict in user:
        tasks_list = []
        for task_dict in tasks:
            if user_dict['id'] == task_dict['userId']:
                task_dict_final = {
                    "task": task_dict.get('title'),
                    "completed": task_dict.get("completed"),
                    "username": user_dict.get('username')}
                tasks_list.append(task_dict_final)
                final_dict[user_dict['id']] = tasks_list

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(final_dict, f)
