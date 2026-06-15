import json

def view_users(args):
     users = []
     with open("data/Users.json","r") as file:
            try:
                users = json.load(file)
            except:
                users = []
     for user in users:  
        print(f"name: {user["name"]}, email: {user["email"]}, projects: {user["projects"]}")