import json
import sys
from models.Project import Project
from colorama import Fore, Style, init
init(autoreset=True)

def add_project(args):
    '''This part handles checking whether all arguments are provided in the command'''
    if args.title == None or args.description == None or args.due_date == None:
        print(f"{Fore.RED} add-project must have all arguments!{Style.RESET_ALL} Type{Fore.YELLOW} python3 main.py add-project --help{Style.RESET_ALL} to see which arguments to use ")
        sys.exit(1)
    projects = []
    project = Project(args.title,args.description,args.due_date)
    '''This part handles obtaining the data saved in the Projects.json file and loading it into a list known as projects'''
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    '''This part handles checking whether the project being created already exists'''
    for entry in projects:
        if entry["title"] == project.title:
            print(f"{Fore.RED}The project exists!")
            break
    
    else:
        '''If the project does not exist, it is appended to the projects list and that new list is used to overwrite the old data in Projects.json'''
        projects.append({"title":project.title,"description":project.description,"due_date":project.due_date,"tasks":project.tasks,"collaborators":project.collaborators})
        try:
            with open("data/Projects.json","w") as file:
                json.dump(projects,file,indent=4)
            print(f"{Fore.GREEN}{project.title} has been added successfully")
        except Exception:
            print(f"{Fore.RED}An error occured and {project.title} could not be added!")
