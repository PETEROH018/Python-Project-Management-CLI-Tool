from datetime import datetime
from colorama import Fore, Style, init
import sys
import re
init(autoreset=True)

class Project:
    def __init__(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.collaborators = [] #This contains the list of users collaborating in the project
        self.tasks = [] #This contains the list of tasks to be done in the project
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if re.match(r"^[a-zA-Z0-9_]+$",value):
            self._title = value
        else:
            print(f"{Fore.RED}The project title should only contain numbers, letters and underscores!{Style.RESET_ALL}")
            sys.exit(1)
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self,value):
        if len(value) > 300:
            print(f"{Fore.RED}The project description should not exceed 300 characters!{Style.RESET_ALL}")
            sys.exit(1)
        else:
            self._description = value

    
    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self,value):
        valid = False
        try:
            datetime.strptime(value,"%d-%m-%Y")
            valid = True
        except ValueError:
            valid = False
        if valid :
            self._due_date = value
        else:
            print(f"{Fore.RED}The date entered is invalid!{Style.RESET_ALL} Please use DD-MM-YYYY format")
            sys.exit(1)


