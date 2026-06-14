import json

def view_projects(args):
     projects = []
     with open("data/Projects.json","r") as file:
            try:
                projects = json.load(file)
            except:
                projects = []
     for project in projects:  
        print(f"title: {project["title"]}, description: {project["description"]}, due_date: {project["due_date"]}, tasks: {project["tasks"]}, collaborators: {project["collaborators"]}")