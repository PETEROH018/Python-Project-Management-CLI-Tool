class Project:
    def __init__(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.collaborators = [] #This contains the list of users collaborating in the project
        self.tasks = [] #This contains the list of tasks to be done in the project
    
    def assign_project(self,user):
        pass