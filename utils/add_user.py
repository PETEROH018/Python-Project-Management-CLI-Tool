import json
import sys
from models.User import User
from colorama import Fore, Style, init
init(autoreset=True)

def add_user(args):
    '''This part handles checking whether all arguments are provided in the command'''
    if args.name == None or args.email == None:
        print(f"{Fore.RED} add-user must have all arguments!{Style.RESET_ALL} Type{Fore.YELLOW} python3 main.py add-user --help{Style.RESET_ALL} to see which arguments to use ")
        sys.exit(1)
    users = []
    user = User(args.name,args.email)
  
    '''This part handles obtaining the data saved in the Users.json file and loading it into a list known as users'''
    with open("data/Users.json","r") as file:
        try:
            users = json.load(file)
        except:
            users = []
    '''This part handles checking whether the user being added already exists'''
    for entry in users:
        if entry["name"] == user.name:
            print(f"{Fore.RED}The user exists!")
            break
    else:
        '''If the user does not exist, they are appended to the users list and that new list is used to overwrite the old data in Users.json'''
        users.append({"name":user.name,"email":user.email,"projects":user.projects})
        try:
            with open("data/Users.json","w") as file:
                json.dump(users,file,indent=4)
            print(f"{Fore.GREEN}{user.name} has been added successfully")
        except Exception:
            print(f"{Fore.RED}An error occured and {user.name} could not be added!")