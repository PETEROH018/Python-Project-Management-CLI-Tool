from colorama import Fore, Style, init
import sys
import re
init(autoreset=True)

class User:
    def __init__(self,name,email):
        self.name = name #Once an instance of the User class is created, this line calls the name property's setter function which does input validation on the name
        self.email = email #This line calls the email property's setter function which does input validation on the email
        self.projects = [] #This list holds the projects that a user is part of as a collaborator
    
    @property
    def name(self): #This the name property's getter function
        return self._name #If the name property is accessed by an instance, a protected variable is returned
    
    @name.setter 
    def name(self,value): #This is the name property's setter function
        if re.match(r"^[a-zA-Z0-9_]+$",value): #It checks whether the value passed as the name matches the given pattern
            self._name = value #If the pattern is matched, the protected variable is updated with the value that is passed as the name when an instance of the class is created
        else: #Otherwise, an error is displayed
             print(f"{Fore.RED}The user name should only contain numbers, letters and underscores!")
             sys.exit(1)
    
    @property
    def email(self): #This the email property's getter function
        return self._email #If the email property is accessed by an instance, a protected variable is returned
    
    @email.setter
    def email(self,value): #This is the email property's setter function
        if re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",value): #It checks whether the value passed as the email matches the pattern user@gmail.com
            self._email = value #If the pattern is matched, the protected variable is updated with the value that is passed as the email when an instance of the class is created
        else: #Otherwise, an error is displayed
            print(f"{Fore.RED}The email entered is invalid!{Style.RESET_ALL} Please use the format {Fore.GREEN}user@gmail.com{Style.RESET_ALL}")
            sys.exit(1)

