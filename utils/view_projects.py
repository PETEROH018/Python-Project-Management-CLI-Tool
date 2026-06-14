import json

def view_projects(args):
    projects = []
    with open("data/Projects.json","r") as file:
        try:
            projects = json.load(file)
        except:
            projects = []
    for project in projects:  
        print(f"title: {project["title"]}, description: {project["description"]}, due_date: {project["due_date"]}")
        print("collaborators:")
        collaborator_count = 1
        for user in project["collaborators"]:
            print(f"{collaborator_count}. name: {user["name"]}, email: {user["email"]}")
        print("tasks:")
        task_count = 1
        for task in project["tasks"] :
            print(f"{task_count}. title: {task["title"]}, status: {task["status"]}, assignee: {task["assignee"]} ")
            task_count+=1
        print("\n")