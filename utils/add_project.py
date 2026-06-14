import json
from models.Project import Project
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
            print("The project exists!")
            break
    else:
        projects.append({"title":project.title,"description":project.description,"due_date":project.due_date,"tasks":project.tasks,"collaborators":project.collaborators})
        with open("data/Projects.json","w") as file:
            json.dump(projects,file,indent=4)