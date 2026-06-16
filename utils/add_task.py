import json
from models.Task import Task

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
    else :
        print("The project selected does not exist!")

    with open("data/Projects.json","w") as file:
            json.dump(projects,file,indent=4)