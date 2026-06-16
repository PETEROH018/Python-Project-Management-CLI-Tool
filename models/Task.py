from colorama import Fore, Style, init
import sys
import re
init(autoreset=True)

class Task:
    def __init__(self,title,status = 'available',assigned_to = None):
        self.title = title #Once an instance of the Task class is created, this line calls the title property's setter function which does input validation on the title
        self.status = status #Can be either available or assigned
        self.assigned_to = assigned_to #This is the user assigned to handle this task. Must be an existing user

    @property
    def title(self): #This the title property's getter function
        return self._title #If the title property is accessed by an instance, a protected variable is returned
    
    @title.setter 
    def title(self,value): #This is the title property's setter function
        if re.match(r"^[a-zA-Z0-9_ ]+$",value):  #It checks whether the value passed as the title matches the given pattern
            self._title = value #If the pattern is matched, the protected variable is updated with the value that is passed as the title when an instance of the class is created
        else: #Otherwise, an error is displayed
             print(f"{Fore.RED}The task title should only contain numbers, letters, underscores and spaces!")
             sys.exit(1)