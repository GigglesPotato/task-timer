# Task_timer.py
# Written by Noah Leeper
# last updated on: 2/8/2025
# A simple task timer that can start tasks end them show when they are running as well as a timesheet that can be exported as a csv
# Github: GigglesPotato




import time
import csv
from datetime import datetime

tasks = {}
timesheet = []

def start_task(task_name):
    if task_name in tasks:
        print(f"'{task_name}' already running.")
    else:
        tasks[task_name] = time.time()
        print(f"Started '{task_name}'.")

def stop_task(task_name):
    if task_name in tasks:
        start_time = tasks.pop(task_name)
        duration = time.time() - start_time
        timesheet.append((task_name, start_time, time.time(), duration))
        print(f"Stopped '{task_name}', {duration:.2f}s.")
    else:
        print(f"'{task_name}' not running.")

def show_running_tasks():
    print("Running tasks:" if tasks else "No tasks running.")
    for task, start in tasks.items():
        print(f"{task}: {time.time() - start:.0f}s")

def show_timesheet():
    print("Timesheet:" if timesheet else "No completed tasks.")
    for task, start, end, duration in timesheet:
        print(f"{task}: {datetime.fromtimestamp(start)} - {datetime.fromtimestamp(end)}, {duration:.2f}s")
# function to export to a csv file
def export_to_csv(filename="timesheet.csv"):
    if timesheet:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task", "Start", "End", "Duration (s)"])
            writer.writerows([(t, datetime.fromtimestamp(s), datetime.fromtimestamp(e), f"{d:.2f}") for t, s, e, d in timesheet])
        print(f"Saved to {filename}")
    else:
        print("No data to export.")
 # Handle choice picking and call functions
def main():
    while True:
        print("\n1. Start a task \n2. Stop a task \n3. Check Running tasks \n4. Show Timesheet \n5. Export Timesheet as csv file \n6. Exit program")
        choice = input("Choice: ")
        choice = input("Choice: ")
        
        if choice == "1":
            start_task(input("Task name: "))
        elif choice == "2":
            stop_task(input("Task name: "))
        elif choice == "3":
            show_running_tasks()
        elif choice == "4":
            show_timesheet()
        elif choice == "5":
            export_to_csv(input("Filename (default: timesheet.csv): ") or "timesheet.csv")
        elif choice == "6":
            exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()