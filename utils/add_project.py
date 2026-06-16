import json
from models.Project import Project
from colorama import Fore, Style, init
init(autoreset=True)

def add_project(args):
    projects = []
    project = Project(args.title,args.description,args.due_date)
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    for entry in projects:
        if entry["title"] == project.title:
            print(f"{Fore.RED}The project exists!")
            break
    else:
        projects.append({"title":project.title,"description":project.description,"due_date":project.due_date,"tasks":project.tasks,"collaborators":project.collaborators})
        try:
            with open("data/Projects.json","w") as file:
                json.dump(projects,file,indent=4)
            print(f"{Fore.GREEN}{project.title} has been added successfully")
        except Exception:
            print(f"{Fore.RED}An error occured and {project.title} could not be added!")
