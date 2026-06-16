import argparse
from utils import add_user,view_users

def main():
    parser = argparse.ArgumentParser(description=" Python Project Management CLI Tool ")
    subparsers = parser.add_subparsers()

    '''Adding a new user using the add-user command '''
    add_user_parser = subparsers.add_parser("add-user",help="Add a new user")
    add_user_parser.add_argument("--name",help="type the user's name")
    add_user_parser.add_argument("--email",help="type the user's email")
    add_user_parser.set_defaults(func=add_user)

    '''Viewing the list of registred users'''
    view_users_parser = subparsers.add_parser("view-users",help="View all registred users")
    view_users_parser.set_defaults(func=view_users)

    args = parser.parse_args()
    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help

if __name__ == "__main__":
    main()

