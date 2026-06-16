import json
from models.User import User
from colorama import Fore, Style, init
init(autoreset=True)

def add_user(args):
    users = []
    user = User(args.name,args.email)
  
    
    with open("data/Users.json","r") as file:
        try:
            users = json.load(file)
        except:
            users = []
    for entry in users:
        if entry["name"] == user.name:
            print(f"{Fore.RED}The user exists!")
            break
    else:
        users.append({"name":user.name,"email":user.email,"projects":user.projects})
        try:
            with open("data/Users.json","w") as file:
                json.dump(users,file,indent=4)
            print(f"{Fore.GREEN}{user.name} has been added successfully")
        except Exception:
            print(f"{Fore.RED}An error occured and {user.name} could not be added!")