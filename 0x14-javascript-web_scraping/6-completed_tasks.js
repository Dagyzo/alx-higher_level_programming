#!/usr/bin/python3
import requests

def count_completed_tasks(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        todos = response.json()
        completed_tasks = {}
        for todo in todos:
            if todo['completed']:
                user_id = todo['userId']
                completed_tasks[user_id] = completed_tasks.get(user_id, 0) + 1

        for user_id, count in completed_tasks.items():
            print(f"User ID: {user_id}, Completed Tasks: {count}")
    else:
        print(f"Error: Failed to retrieve data from {api_url}")

# Main script
api_url = "https://jsonplaceholder.typicode.com/todos"
count_completed_tasks(api_url)
