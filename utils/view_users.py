import json
from colorama import Fore, Style, init
init(autoreset=True)

def view_users(args):
     users = []
     '''This part handles obtaining the data saved in the Users.json file and loading it into a list known as users'''
     with open("data/Users.json","r") as file:
            try:
                users = json.load(file)
            except:
                users = []
     user_count = 1
     '''This part handles diplaying the users data on the terminal in an organized manner'''
     for user in users:  
        print(f"{user_count}. {Fore.MAGENTA}name{Style.RESET_ALL}: {user["name"]}, {Fore.MAGENTA}email{Style.RESET_ALL}: {user["email"]}")
        print(Fore.YELLOW + "projects:")
        project_count = 1
        for project in user["projects"]:
            print(f"    {project_count}.{Fore.GREEN} {project["title"]} {Style.RESET_ALL} -> description: {project["description"]}, due_date {project["due_date"]}")
            project_count += 1
            print(Fore.YELLOW + "       tasks")
            task_count = 1
            for task in project["tasks"]:
                 print(f"       {task_count}. {task["title"]}")
                 task_count += 1
        print("\n")
        user_count += 1