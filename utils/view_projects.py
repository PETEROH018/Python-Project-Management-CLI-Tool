import json
from colorama import Fore, Style, init
init(autoreset=True)

def view_projects(args):
    projects = []
    '''This part handles obtaining the data saved in the Projects.json file and loading it into a list known as projects'''
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    projects_count = 1
    '''This part handles diplaying the projects data on the terminal in an organized manner'''
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