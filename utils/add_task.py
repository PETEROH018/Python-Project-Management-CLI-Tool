import json
from models.Task import Task
import sys
from colorama import Fore, Style, init
init(autoreset=True)

def add_task(args):
    '''This part handles checking whether all arguments are provided in the command'''
    if args.title == None or args.project == None:
        print(f"{Fore.RED} add-task must have all arguments!{Style.RESET_ALL} Type{Fore.YELLOW} python3 main.py add-task --help{Style.RESET_ALL} to see which arguments to use ")
        sys.exit(1)
    task = Task(args.title)
    projects = []
    '''This part handles obtaining the data saved in the Projects.json file and loading it into a list known as projects'''
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    '''This part handles checking whether the project specified in the command argument exists in the Projects.json file'''
    '''If the project exists, the task is appended to that project's tasks list'''
    for project in projects:  
        if project["title"] == args.project:
            project["tasks"].append({"title":task.title,"status":task.status,"assignee":task.assigned_to})
            break
    else:
        '''Otherwise an error is displayed'''
        print(f"{Fore.RED}The project selected does not exist!")
        sys.exit(1)
    try:
        '''The updated projects list is then used to overwrite the old data in the Projects.json file '''
        with open("data/Projects.json","w") as file:
            json.dump(projects,file,indent=4)
        print(f"{Fore.GREEN}{task.title} has been added successfully to {args.project}")
    except Exception:
        print(f"{Fore.RED}An error occured and {task.title} could not be added to {args.project}!")