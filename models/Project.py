class Project:
    def __init__(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.collaborators = []
        self.tasks = []
    
    def assign_project(self,user):
        pass