import json
# from models.Task import Task
# from models.Project import Project
# from models.User import User

def assign_project(args):
    users = []
    with open("data/Users.json","r") as file: #Getting user data that is saved in the Users.json file
        try:
            users = json.load(file) #If the file is readable, the data is read and loaded into a list
        except:
            users = [] #If the file is unreadable, the list is initialized as an empty list
    user = next((user for user in users if user.get("name") == args.name), None) #A user dictionary is created with details of the user who has the name specified in the command argument
    projects = []
    with open("data/Projects.json","r") as file: #Getting project data that is saved in the Projects.json file
        try:
            projects = json.load(file) #If the file is readable, the data is read and loaded into a list
        except:
            projects = []
    project = next((project for project in projects if project.get("title") == args.project), None) #A project dictionary is created with details of the project that has the title specified in the command argument

    if user != None: 
#If the user exists, the next step is to check whether the project in the command argument exists
        if project != None: 
#If the project exists, the next step is to check whether the tasks specified in the argument of the command exist in the list of tasks for that particular project

            '''This part handles checking whether the tasks given in the command argument exist in storage'''
            tasks_to_be_assigned = [] #This list holds the tasks that have been confirmed to exist in the list of tasks of the project
            for entry in args.tasks: #Looping through the list of tasks specified in the argument of the command
                for task in project["tasks"]: #Inner loop to compare the tasks supplied in the command with the tasks of the selected project saved in the JSON file 
                    if entry == task["title"]: #If they match, then the task exists
                        tasks_to_be_assigned.append(task) #The task is appended to the tasks_to_be_assigned list for further processing
                        break
                else:
                    print(f"The task, {entry}, does not exist in {project["title"]} tasks list!") # If there is no match, then the task does not exist

            '''This part handles checking the availability of a task for assignment to a collaborator'''
            assigned_tasks = [] #This holds the tasks that have been confirmed to exist in memory and have been assigned to a user
            for task_entry in tasks_to_be_assigned: #Looping through the tasks that have been confirmed to exist in memory
                if task_entry["status"] == "available": #If the status is available, then the task is added to the assigned tasks list
                    assigned_tasks.append(task_entry) 
                else:
                    print(f"The task, {task_entry["title"]}, is already assigned to {task_entry["assignee"]}")

            '''This part handles looping through the users stored in Users.json and finding the user specified in the command argument '''
            for user_entry in users: #Looping through the entire list of users stored in the Users.json file
                if user_entry["name"] == args.name  : #For a user with the name provided in the command argument, the project specified in the command is added to their project list
                    '''This part handles checking whether a project already exists in the list of projects the user is part of to prevent duplicating the same project'''
                    for user_project in user_entry["projects"]: #Looping through the projects that a user is already collaborating in
                        if user_project["title"] == args.project: #If the project specified in the command argument exists, there is no need to re-add the project again
                            user_project["tasks"].extend(assigned_tasks) #Instead, the tasks list for that project is extended to include the new tasks
                            break
                    else:
                        user_entry["projects"].append({"title":project["title"],"description":project["description"],"due_date":project["due_date"],"tasks":assigned_tasks})

            '''This part handles looping through the projects stored in Projects.json and finding the project specified in the command argument for modification'''
            for project_entry in projects: #Looping through the entire list of projects stored in the Projects.json file 
                if project_entry["title"] == args.project: #For a project with the title provided in the command argument, the user specified in the command is added as a collaborator
                    '''This part handles checking whether a user has already been added as a collaborator to a project to prevent duplicating collaborators'''
                    for collaborator in project_entry["collaborators"]: #Looping through existing collaborators in the project specified in the command argument
                        if collaborator["name"] == args.name: #If the collaborator already exists, there is no need to re-add them
                            break
                    else:
                        project_entry["collaborators"].append({"name":user["name"],"email":user["email"]})
                    '''This part handles changing the status of an assigned task to 'assigned' and updating the assignee to the user specified in the command argument '''
                    for project_task in project_entry["tasks"]: #Looping through the list of tasks in the project specified in the argument
                        for assigned_task in assigned_tasks: #Inner loop comparing the tasks saved in the Project.JSON file to the tasks assigned to the user
                            if project_task["title"] == assigned_task["title"]: # If they match, the task status is updated to assigned and the assignee is updated as well
                                project_task["status"] = "assigned"
                                project_task["assignee"] = user["name"]

        else:
            print("The selected project does not exist!")
            
    else:
        print("The selected user does not exist!")
    with open("data/Users.json","w") as file:
            json.dump(users,file,indent=4)
    with open("data/Projects.json","w") as file:
            json.dump(projects,file,indent=4)