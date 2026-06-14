import json

def view_users(args):
     users = []
     with open("data/Users.json","r") as file:
            try:
                users = json.load(file)
            except:
                users = []
     for user in users:  
        print(user)