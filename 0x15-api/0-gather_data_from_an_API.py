#! usr/bin/python3
"""
   Script to fetch and display an employee's TODO list progress using a RST API
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    
    base_url = "https://jsonplaceholder.typicode.com"
    
    #Fetch employee details 
    employee_url = "{}/users/{}".format(base_url, employee_id)

    response = requests.get(employee_url)
    if response.status_code != 200:
        print("Error: Unable to fetch employee data of ID {}".format(employee_id))
        return
    print(response)
    employee_data = response.json()
    employee_name = employee_data.get("name")

    #Fetch the todo list of the employees
    todo_url = "{}/todos".format(base_url)
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: unable to fetch the TODO list for the employee ID: {}".format(employee_id))
        return
    todo_data = response.json()

    #Filter the completed tasks
    completed_tasks = [task for task in todo_data if task.get("completed")]

    #dispay the result in the terminal
    total_tasks = len(todo_data)
    done_tasks = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Python3 O-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

