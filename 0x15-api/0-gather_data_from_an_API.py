#!/usr/bin/python3
"""Access employee TODO list progress via API and display it."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: Prints the employee's TODO progress to stdout.
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee's TODO list
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task.get("completed"))

    # Display progress
    print(
        f"Employee {employee_name}"
        "is done with tasks({done_tasks}/{total_tasks}):"
    )

    # Display completed tasks
    for task in todos_data:
        if task.get("completed"):
            print(f"\t {task.get('title')}")


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
