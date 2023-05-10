#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
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
        print(class_name)
        print(class_id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
