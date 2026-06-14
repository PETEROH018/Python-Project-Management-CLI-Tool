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
        if entry[0] == project.title:
            print("The project exists!")
            break
    else:
        projects.append((project.title,project.desctription,project.due_date))
        with open("data/Projects.json","w") as file:
            json.dump(projects,file)
