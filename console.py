#!/usr/bin/python3
"""
This module contains the definition for the 'Console' class which is the entry
point of the command interpreter
"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    A customised command line interpreter for the AirBnB_clone project
    """

    prompt = "(hbnb) "

    def help_quit(self):
        "Handles for the quit command with a 'help' argument"
        print("Quit command to exit the program\n")

    def help_EOF(self):
        "Handles for the quit command with a 'EOF' argument"
        print("Quit command to exit the program\n")

    def do_quit(self, line):
        """
        Exits the program
        """

        return (True)

    def do_EOF(self, line):
        """
        Exits the program
        """

        return (True)

    def emptyline(self):
        """
        Do nothing
        """

        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. Ex: $ create BaseModel

        - If the class name is missing, print '** class name missing **'
        (ex: $ create)
        - If the class name class name doesn't exist, print
        '**class doesn't exist **' (ex. $ create MyModel)
        """

        if line == "BaseModel":
            base = BaseModel()
            base.save()
            print(base.id)
        elif line != "BaseModel" and len(line) > 0:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def show(self, class_name, class_id):
        """
        Prints the information about the specified class
        """
        print(class_name)
        print(class_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
