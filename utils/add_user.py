import json
from models.User import User

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
            print("The user exists!")
            break
    else:
        users.append({"name":user.name,"email":user.email,"projects":user.projects})
        with open("data/Users.json","w") as file:
            json.dump(users,file,indent=4)


