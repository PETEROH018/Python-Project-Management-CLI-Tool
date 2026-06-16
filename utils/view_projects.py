import json
from colorama import Fore, Style, init
init(autoreset=True)

def view_projects(args):
    projects = []
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    projects_count = 1
    for project in projects:  
        print(f"{projects_count}. {Fore.MAGENTA}{project["title"]}{Style.RESET_ALL} -> description: {project["description"]}, due_date: {project["due_date"]}")
        print(f"    {Fore.GREEN}collaborators:")
        collaborator_count = 1
        for user in project["collaborators"]:
            print(f"        {collaborator_count}. name: {user["name"]}, email: {user["email"]}")
        print(f"    {Fore.YELLOW}tasks:")
        task_count = 1
        for task in project["tasks"] :
            print(f"        {task_count}. title: {task["title"]}, status: {task["status"]}, assignee: {task["assignee"]} ")
            task_count+=1
        projects_count += 1
        print("\n")