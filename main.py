import argparse
from utils import add_user,view_users,add_project,view_projects,add_task,assign_project

def main():
    parser = argparse.ArgumentParser(description=" Python Project Management CLI Tool ")
    subparsers = parser.add_subparsers() #subparsers group related CLI commands and help in organizing the CLI code

    '''Adding a new user using the add-user command '''
    add_user_parser = subparsers.add_parser("add-user",help="Add a new user")
    add_user_parser.add_argument("--name",help="type the user's name")
    add_user_parser.add_argument("--email",help="type the user's email")
    add_user_parser.set_defaults(func=add_user)

    '''Viewing the list of registred users using the view-users command'''
    view_users_parser = subparsers.add_parser("view-users",help="View all registred users")
    view_users_parser.set_defaults(func=view_users)

    '''Adding a new project using the add-project command'''
    add_project_parser = subparsers.add_parser("add-project",help="Add a new project")
    add_project_parser.add_argument("--title",help="type the project's title")
    add_project_parser.add_argument("--description",help="type the project's description")
    add_project_parser.add_argument("--due_date",help="type the project's due_date")
    add_project_parser.set_defaults(func=add_project)

    '''Viewing the list of projects using the view-projects command'''
    view_projects_parser = subparsers.add_parser("view-projects",help="View all projects")
    view_projects_parser.set_defaults(func=view_projects)

    '''Adding a new task using the add-task command'''
    add_tasks_parser = subparsers.add_parser("add-task",help="Add a new task to a project")
    add_tasks_parser.add_argument("--title",help="type the task's title")
    add_tasks_parser.add_argument("--project",help="type the project that contains that task")
    add_tasks_parser.set_defaults(func=add_task)

    '''Assign a project and tasks to a user using the assign-project command'''
    add_project_parser = subparsers.add_parser("assign-project",help="Add a project and tasks to a user")
    add_project_parser.add_argument("--name",help="type the user's name")
    add_project_parser.add_argument("--project",help="type the project's title")
    add_project_parser.add_argument("--tasks",nargs='+',help="type the tasks to assign to the user and separate them with spaces")
    add_project_parser.set_defaults(func=assign_project)


    args = parser.parse_args()
    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help

if __name__ == "__main__":
    main()

