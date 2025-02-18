"""
Written By Noah Leeper
edited on: 2/18/2025
Task Timer
A simple CLI tool for tracking task durations.
This program allows users to start, stop, and list tasks, storing them in a file for persistence.
"""
import datetime
import click
import os
import sys

# Dictionary to store tasks
tasks = {}

# Load tasks from a file if it exists
def load_tasks():
    # Check if the file exists
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                name, start_time, end_time = line.strip().split(",")
                tasks[name] = (datetime.datetime.fromisoformat(start_time), datetime.datetime.fromisoformat(end_time))

# Save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for name, (start, end) in tasks.items():
            file.write(f"{name},{start.isoformat()},{end.isoformat()}\n")

# Start a new task
def start_task():
    name = input("Enter task name: ")
    if name in tasks:
        print("Task already exists. Stop it before restarting.")
        return
    tasks[name] = (datetime.datetime.now(), None)
    print(f"Started task '{name}' at {tasks[name][0]}.")

# Stop an active task
def stop_task():
    name = input("Enter task name to stop: ")
    if name not in tasks or tasks[name][1] is not None:
        print("Task not found or already stopped.")
        return
    start_time, _ = tasks[name]
    tasks[name] = (start_time, datetime.datetime.now())
    print(f"Stopped task '{name}' at {tasks[name][1]}.")

# List all tasks and their durations
def list_tasks():
    for name, (start, end) in tasks.items():
        duration = (end - start).total_seconds() if end else "Ongoing"
        print(f"{name}: {start} - {end} | Duration: {duration} sec")

# Display the menu and handle user input
def menu():
    options = {
        "1": start_task,
        "2": stop_task,
        "3": list_tasks,
        "4": save_tasks,
        "5": exit
    }
    while True:
        print("\nTask Timer Menu:")
        print("1. Start Task")
        print("2. Stop Task")
        print("3. List Tasks")
        print("4. Save Tasks")
        print("5. Exit")
        choice = input("Choice: ").strip()
        if choice in options:
            options[choice]()
        else:
            print("Invalid choice, try again.")

# Command-line interface entry point
@click.command()
def cli():
    load_tasks()
    menu()

# Run the CLI if the script is executed directly
if __name__ == "__main__":
    cli()
