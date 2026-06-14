import json

def view_projects(args):
     projects = []
     with open("data/Projects.json","r") as file:
            try:
                projects = json.load(file)
            except:
                projects = []
     for project in projects:  
        print(f"{project[0]},{project[1]},{project[2]}")