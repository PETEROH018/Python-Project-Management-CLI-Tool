## Commands
1. add-user --name user1 --email user1@gmail.com
    - It takes two arguments: the user's name which is like the username and should be unique and the user's email address.
    - It is used to add a new user and the user details are saved in the Users.json file.
    - Trying to add a user with an existing name will throw an error stating "The user exists!"

2. view-user
    - It does not take any arguments.
    - It is used to obtain all the users and their details stored in the Users.json file and display them on the terminal on an organized way.
    - The details are the name, email and a list of all the projects the user is engaged in. 
    - Within the list of projects, all the tasks that the user has been assigned in each project is shown.

3. add-project --title project1 -- description "First Project" --due_date 20-06-2026
    - It takes three arguments: The project title which should be unique, the project description   which can be a paragraph but needs to be enclosed in double quotation marks and the due_date which should be in the DD-MM-YYYY format
    - It is used to add a new project and the project details are saved in the Projects.json file.
    - Trying to add a project with an existing title will throw an error stating "The project exists!"

4. view-projects
    - It does not take any arguments.
    - It is used to obtain all the projects and their details stored in the Projects.json file and display them on the terminal.
    - The details are the title, description, due_date, list of tasks in the project, list of collaborators in the project.
    - Each task has a title, a status of either available or assigned and the name of the assignee which should be a user in the collaborators list.

5. add-task --title "The first task" --project project1
    - It takes two arguments:  The task title which is also a brief description of the task and the project title of the project you are adding that task to
    - The task also has a status attribute which is initialized as "available" and an assigned_to attribute which is initialized as None

6. assign-project --name user1 --project project1 --tasks Task1 Task2 Task3
    - It takes three arguments: The name of the user to be assigned tasks in the project, the title of the project, the list of tasks that the user is to be assigned.
    - The list of tasks is separated by spaces after the --tasks flag
    - If a task title has multiple words, it is enclosed in single quotation marks
    - If the name does not match an existing user, an error is thrown indicating "The selected user does not exist!"
    - If the project title does not match and existing user, an error is thrown indicating "The selected project does not exist!"
    - If a task in the tasks list does not match an existing task in the project, an error is also thrown indicating "The task, task_title, does not exist in project_title tasks list!"
    - If task exists but has already been assigned to another user, an error is thrown showing "The task, task_title, is already assigned to assignee"
    - When all the checks are complete and the arguments in the command are consistent with the data stored in the json files, the project is added to the user's project list, the user is added as a collaborator in the project and the tasks are assigned to the user.