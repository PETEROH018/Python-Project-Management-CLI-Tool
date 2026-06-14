class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.projects = [] #This contains the list of projects that user is part of as a collaborator