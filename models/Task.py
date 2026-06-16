from colorama import Fore, Style, init
import sys
import re
init(autoreset=True)

class Task:
    def __init__(self,title,status = 'available',assigned_to = None):
        self.title = title
        self.status = status #Can be either available or assigned
        self.assigned_to = assigned_to #This is the user assigned to handle this task. Must be an existing user

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if re.match(r"^[a-zA-Z0-9_]+$",value):
            self._title = value
        else:
             print(f"{Fore.RED}The task title should only contain numbers, letters and underscores!")
             sys.exit(1)