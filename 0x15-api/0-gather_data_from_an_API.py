#!/usr/bin/python3
"""
   Script to fetch and display an employee's TODO list progress using a RST API
"""

import requests
import sys
import csv
import json

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
    #Prepare the todo tasks
    csv_data = []
    for task in todo_data:
        csv_data.append([employee_id, employee_data.get("username"),str(task["completed"]), task["title"]])

    #Export to csv
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode ="w", newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(csv_data)
    print("Data is exported to {}".format(csv_filename))

    #Export to JSON
    json_data = {employee_id:[{"task": task["title"], "completed": task["completed"], "username": employee_data.get("username")} for task in todo_data]}

    #write to JSON file
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, mode="w") as file:
        json.dump(json_data, file, indent=4)
    print("Data exported to{}".format(json_filename))


    #Organize the data
    all_todos = {}
    if employee_data and isinstance(employee_data, list):
        user_dict = {employee["id"]: str(employee["username"]) for employee in employee_data}
        print(user_dict)
    for task in todo_data:
        user_id = task["userId"]
        if user_id not in all_todos:
            all_todos[user_id] = []
        all_todos[user_id].append({"username": user_dict[user_id], "task": task["title"], "completed": task["completed"]})

    
    #Employee all employess task to Json
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode="w") as Json_file:
        json.dump(all_todos, json_file)
    print("Data exporrted to {}".format(json_filename))
    
    
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

