class Project:
    def __init__(self,title,description,due_date):
        self.title = title
        self.desctription = description
        self.due_date = due_date
        self.user = None
        self.tasks = []
    
    def assign_project(self,user):
        pass