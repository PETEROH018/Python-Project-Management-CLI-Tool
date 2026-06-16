from colorama import Fore, Style, init
import sys
import re
init(autoreset=True)

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.projects = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if re.match(r"^[a-zA-Z0-9_]+$",value):
            self._name = value
        else:
             print(f"{Fore.RED}The user name should only contain numbers, letters and underscores!")
             sys.exit(1)
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,value):
        if re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",value):
            self._email = value
        else:
            print(f"{Fore.RED}The email entered is invalid!{Style.RESET_ALL} Please use the format {Fore.GREEN}user@gmail.com{Style.RESET_ALL}")
            sys.exit(1)

