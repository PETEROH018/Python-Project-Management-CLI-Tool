import json
from models.Task import Task
import sys
from colorama import Fore, Style, init
init(autoreset=True)

def add_task(args):
    task = Task(args.title)
    projects = []
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    for project in projects:  
        if project["title"] == args.project:
            project["tasks"].append({"title":task.title,"status":task.status,"assignee":task.assigned_to})
            break
    else:
        print(f"{Fore.RED}The project selected does not exist!")
        sys.exit(1)
    try:
        with open("data/Projects.json","w") as file:
            json.dump(projects,file,indent=4)
        print(f"{Fore.GREEN}{task.title} has been added successfully to {args.project}")
    except Exception:
        print(f"{Fore.RED}An error occured and {task.title} could not be added to {args.project}!")