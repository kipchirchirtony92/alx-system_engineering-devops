#!/usr/bin/env python3
"""Gather data from an API about an employee's TODO list progress."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found")
        return
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list for the employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch TODO list for employee {employee_id}")
        return

    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed = len(completed_tasks)

    # Display the results in the exact required format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
