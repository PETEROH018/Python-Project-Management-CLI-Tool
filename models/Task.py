class Task:
    def __init__(self,title,status = 'available',assigned_to = None):
        self.title = title
        self.status = status #Can be either available or assigned
        self.assigned_to = assigned_to #This is the user assigned to handle this task. Must be an existing user