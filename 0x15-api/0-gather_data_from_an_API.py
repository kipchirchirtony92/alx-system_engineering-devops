#!/usr/bin/python3
"""Module to fetch and display employee TODO list progress from an API."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display employee TODO list progress.

    Args:
        employee_id (int): Employee ID
    """
    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    "/todos"

    try:
        # Get employee data
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Get TODO list
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data
                           if task.get('completed')]
        num_completed = len(completed_tasks)

        # Display results
        print(
            f"Employee {employee_name} is done with tasks"
            "({num_completed}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
