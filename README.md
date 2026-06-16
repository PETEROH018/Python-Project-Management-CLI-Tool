## Commands
- To run a command: 
                    1. navigate to the folder containing main.py 
                    2. open the terminal
                    3. type the command starting with: python3 main.py <--command-->
                    4. type python3 main.py --help to see what each command does
                    5. type python3 main.py <--command--> --help to see what each argument means and how to use it

1. add-user --name user1 --email user1@gmail.com
    - It takes two arguments: the user's name which is like the username and should be unique and the user's email address.
    - It is used to add a new user and the user details are saved in the Users.json file.
    - Trying to add a user with an existing name will throw an error stating "The user exists!"
    - The user name should only contain letters, numbers and underscores. Otherwise, an error is thrown indicating "The user name should only contain numbers, letters and underscores!"
    - The email should follow the format user1@gmail.com. Otherwise an error is thrown indicating "The email entered is invalid! Please use the format user@gmail.com"
    - If all the input validation checks are successful and the changes have been made to the Users.json file, an success message is displayed indicating "User1 has been added successfully"
    - If the Users.json file cannot be written to, an error is displayed indicating " {Fore.RED}An error occured and user1 could not be added!"

2. view-user
    - It does not take any arguments.
    - It is used to obtain all the users and their details stored in the Users.json file and display them on the terminal on an organized way.
    - The details are the name, email and a list of all the projects the user is engaged in. 
    - Within the list of projects, all the tasks that the user has been assigned in each project is shown.

3. add-project --title project1 -- description "First Project" --due_date 20-06-2026
    - It takes three arguments: The project title which should be unique, the project description   which can be a paragraph but needs to be enclosed in single/double quotation marks and the due_date which should be in the DD-MM-YYYY format
    - It is used to add a new project and the project details are saved in the Projects.json file.
    - Trying to add a project with an existing title will throw an error stating "The project exists!"
    - The project title should only contain letters, numbers, spaces and underscores. Otherwise an error is thrown indicating "The project title should only contain numbers, letters, spaces and underscores!"
    - The project description should not exceed 300 characters. Otherwise, an error is thrown indicating "The project description should not exceed 300 characters!"
    - The project due date should follow the date format DD-MM-YYYY. Otherwise an error is thrown indicating "The date entered is invalid! Please use DD-MM-YYYY format"
    - If all the input validation checks are successful and the changes have been saved to the Projects.json file, a success message is displayed indicating "Project1 has been added successfully"
    - If the Projects.json file cannot be written to, an error is thrown indicating "An error occured and Project1 could not be added!"

4. view-projects
    - It does not take any arguments.
    - It is used to obtain all the projects and their details stored in the Projects.json file and display them on the terminal.
    - The details are the title, description, due_date, list of tasks in the project, list of collaborators in the project.
    - Each task has a title, a status of either available or assigned and the name of the assignee which should be a user in the collaborators list.

5. add-task --title "The first task" --project project1
    - It takes two arguments:  The task title which is also a brief description of the task and the project title of the project you are adding that task to
    - The task also has a status attribute which is initialized as "available" and an assigned_to attribute which is initialized as None
    - The task title should only contain letters, numbers, spaces and underscores. Otherwise an error is thrown indicating "The task title should only contain numbers, letters, spaces and underscores!"
    - If all the input validation checks are successful and the changes have been saved to the Projects.json file, a success message is displayed indicating "Task1 has been added successfully to project1"
    -If the Projects.json file cannot be written to, an error is thrown indicating "An error occured and task1 could not be added to project1!"


6. assign-project --name user1 --project project1 --tasks Task1 Task2 Task3
    - It takes three arguments: The name of the user to be assigned tasks in the project, the title of the project, the list of tasks that the user is to be assigned.
    - The list of tasks is separated by spaces after the --tasks flag
    - If a task title has multiple words, it is enclosed in single quotation marks
    - If the name does not match an existing user, an error is thrown indicating "The selected user does not exist!"
    - If the project title does not match and existing user, an error is thrown indicating "The selected project does not exist!"
    - If a task in the tasks list does not match an existing task in the project, an error is also thrown indicating "The task, task_title, does not exist in project_title tasks list!"
    - If task exists but has already been assigned to another user, an error is thrown showing "The task, task_title, is already assigned to assignee"
    - When all the checks are complete and the arguments in the command are consistent with the data stored in the json files, the project is added to the user's project list, the user is added as a collaborator in the project and the tasks are assigned to the user.
    - On successful assignment of the task(s) in a project to user, a success message is displayed indicating "user1 has been assigned the following tasks in project1 project:  task1
          task2
          task3 "
    - If the changes could not be written to the Users.json file or Projects.json file or both, an error is displayed indicating "An error occured when trying to assign user1 the tasks in project1 project"

