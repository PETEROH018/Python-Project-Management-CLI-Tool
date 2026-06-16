from datetime import datetime
from colorama import Fore, Style, init
import sys
import re
init(autoreset=True)

class Project:
    def __init__(self,title,description,due_date):
        self.title = title #Once an instance of the Project class is created, this line calls the title property's setter function which does input validation on the title
        self.description = description #This line calls the description property's setter function which does input validation on the description
        self.due_date = due_date #This line calls the due_date property's setter function which does input validation on the due_date
        self.collaborators = [] #This contains the list of users collaborating in the project
        self.tasks = [] #This contains the list of tasks to be done in the project
    
    @property
    def title(self): #This the title property's getter function 
        return self._title #If the title property is accessed by an instance, a protected variable is returned
    
    @title.setter
    def title(self,value): #This is the title property's setter function
        if re.match(r"^[a-zA-Z0-9_ ]+$",value): #It checks whether the value passed as the title matches the given pattern
            self._title = value #If the pattern is matched, the protected variable is updated with the value that is passed as the title when an instance of the class is created
        else: #Otherwise, an error is displayed
            print(f"{Fore.RED}The project title should only contain numbers, letters, spaces and underscores!")
            sys.exit(1)
    
    @property 
    def description(self): #This the description property's getter function
        return self._description #If the description property is accessed by an instance, a protected variable is returned
    
    @description.setter
    def description(self,value): #This is the description property's setter function
        if len(value) > 300: #It checks whether the value passed as the description exceeds 300 characters
            print(f"{Fore.RED}The project description should not exceed 300 characters!") #If it exceeds, an error is displayed
            sys.exit(1)
        else:
            self._description = value #Otherwise, the protected variable is updated with the value that is passed as the description when an instance of the class is created

    
    @property
    def due_date(self): #This the due_date property's getter function
        return self._due_date #If the due_date property is accessed by an instance, a protected variable is returned
    
    @due_date.setter
    def due_date(self,value): #This is the due_date property's setter function
        valid = False
        try:
            datetime.strptime(value,"%d-%m-%Y") #It checks whether the value passed as the due_date follows the DD-MM-YYYY format
            valid = True
        except ValueError:
            valid = False
        if valid :
            self._due_date = value #If the format is okay, the protected variable is updated with the value that is passed as the due_date when an instance of the class is created
        else: #Otherwise, an error is displayed
            print(f"{Fore.RED}The date entered is invalid!{Style.RESET_ALL} Please use DD-MM-YYYY format")
            sys.exit(1)


