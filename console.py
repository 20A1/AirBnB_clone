#!/usr/bin/python3
"""
This module contains the definition for the 'Console' class which is the entry
points of the command interpreter
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                 "Review"]
    __method_arg = ["all", "count", "show", "destroy", "update"]

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

    def do_BaseModel(self, line):
        """
        Retrieves all instances of a class by using BaseModel.all()
        """
        error_string = "*** Unknown syntax: BaseModel{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
            return
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "BaseModel"
            if key.split(".")[0] == class_name:
                instances.append(BaseModel(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_User(self, line):
        """
        Retrieves all instances of a class by using User.all()
        """
        error_string = "*** Unknown syntax: User{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
            return
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "User"
            if key.split(".")[0] == class_name:
                instances.append(User(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_State(self, line):
        """
        Retrieves all instances of a class by using State.all()
        """
        error_string = "*** Unknown syntax: State{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "State"
            if key.split(".")[0] == class_name:
                instances.append(State(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_City(self, line):
        """
        Retrieves all instances of a class by using City.all()
        """
        error_string = "*** Unknown syntax: City{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "City"
            if key.split(".")[0] == class_name:
                instances.append(City(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_Amenity(self, line):
        """
        Retrieves all instances of a class by using Amenity.all()
        """
        error_string = "*** Unknown syntax: Amenity{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "Amenity"
            if key.split(".")[0] == class_name:
                instances.append(Amenity(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_Place(self, line):
        """
        Retrieves all instances of a class by using Place.all()
        """
        error_string = "*** Unknown syntax: Place{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "Place"
            if key.split(".")[0] == class_name:
                instances.append(Place(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_Review(self, line):
        """
        Retrieves all instances of a class by using Review.all()
        """
        error_string = "*** Unknown syntax: Review{:s}".format(line)
        if line is None or len(line) <= 0:
            print(error_string)
            return
        arg = line.split(".")
        if len(arg) <= 1:
            print(error_string)
            return
        arg_type = arg[1].split("(")[0]
        if arg_type not in self.__method_arg:
            print(error_string)
        class_id = arg[1].split("\"")
        if len(class_id) <= 1:
            print(error_string)
            return
        class_id = class_id[1]
        instances = []
        dictionary = storage.all()
        for key in dictionary:
            class_name = "Review"
            if key.split(".")[0] == class_name:
                instances.append(Review(**dictionary[key]))
        if arg_type == "all":
            print("[", end="")
            for i in range(len(instances)):
                if i > 0:
                    print(", ", end="")
                print(instances[i], end="")
            print("]")
        elif arg_type == ".count()":
            print(len(instances))
        elif arg_type == "show":
            for obj in instances:
                if obj.id == class_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_create(self, line):
        """
        Creates a new instance of the class passed to the line argument,
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel

        - If the class name is missing, print '** class name missing **'
        (ex: $ create)
        - If the class name class name doesn't exist, print
        '**class doesn't exist **' (ex. $ create MyModel)
        """

        if line is None or len(line) <= 0:
            print("** class name missing **")
        elif line not in self.__classes:
            print("** class doesn't exist **")
        else:
            inst = None
            if line == "BaseModel":
                inst = BaseModel()
            elif line == "User":
                inst = User()
            elif line == "State":
                inst = State()
            elif line == "City":
                inst = City()
            elif line == "Amenity":
                inst = Amenity()
            elif line == "Place":
                inst = Place()
            elif line == "Review":
                inst = Review()
            inst.save()
            print(inst.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id. Ex $ show BaseModel 1234-1234-1234-1234

        Some edge case and their handles are as follows:
            - If the class name is missing, print ** class name missing **
            (ex: $ show)
            - If the class name doesn’t exist, print ** class doesn't exist **
            (ex: $ show MyModel)
            - If the id is missing, print ** instance id missing **
            (ex: $ show BaseModel)
            - If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ show BaseModel 121212)
        """

        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) > 0:
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{0:s}.{1:s}".format(args[0], args[1])
                dictionary = storage.all()
                instance = None
                if key in dictionary:
                    class_name = key.split(".")[0]
                    if class_name == "BaseModel":
                        instance = BaseModel(**dictionary[key])
                    elif class_name == "User":
                        instance = User(**dictionary[key])
                    elif class_name == "State":
                        instance = State(**dictionary[key])
                    elif class_name == "City":
                        instance = City(**dictionary[key])
                    elif class_name == "Amenity":
                        instance = Amenity(**dictionary[key])
                    elif class_name == "Place":
                        instance = Place(**dictionary[key])
                    elif class_name == "Review":
                        instance = Review(**dictionary[key])
                    print(instance)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234

        - If the class name is missing, print ** class name missing **
        (ex: $ destroy)
        - If the class name doesn’t exist, print ** class doesn't exist **
        (ex:$ destroy MyModel)
        - If the id is missing, print ** instance id missing **
        (ex: $ destroy BaseModel)
        - If the instance of the class name doesn’t exist for the id, print
        ** no instance found ** (ex: $ destroy BaseModel 121212)
        """

        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) > 0:
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{0:s}.{1:s}".format(args[0], args[1])
                dictionary = storage.all()
                if key in dictionary:
                    del (dictionary[key])
                    storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all

        - The printed result must be a list of strings
        - If the class name doesn’t exist, print ** class doesn't exist **
            (ex: $ all MyModel)
        """

        instances = []
        dictionary = storage.all()
        if arg is None or len(arg) == 0:
            for key in dictionary:
                class_name = key.split(".")[0]
                if class_name == "BaseModel":
                    instances.append(BaseModel(**dictionary[key]))
                elif class_name == "User":
                    instances.append(User(**dictionary[key]))
                elif class_name == "State":
                    instances.append(State(**dictionary[key]))
                elif class_name == "City":
                    instances.append(City(**dictionary[key]))
                elif class_name == "Amenity":
                    instances.append(Amenity(**dictionary[key]))
                elif class_name == "Place":
                    instances.append(Place(**dictionary[key]))
                elif class_name == "Review":
                    instances.append(Review(**dictionary[key]))
        else:
            if arg not in self.__classes:
                print("** class doesn't exist **")
            else:
                for key in dictionary:
                    if key.split(".")[0] == arg:
                        if arg == "BaseModel":
                            instances.append(BaseModel(**dictionary[key]))
                        elif arg == "User":
                            instances.append(User(**dictionary[key]))
                        elif arg == "State":
                            instances.append(State(**dictionary[key]))
                        elif arg == "City":
                            instances.append(City(**dictionary[key]))
                        elif arg == "Amenity":
                            instances.append(Amenity(**dictionary[key]))
                        elif arg == "Place":
                            instances.append(Place(**dictionary[key]))
                        elif arg == "Review":
                            instances.append(Review(**dictionary[key]))
        print_str = []
        for items in instances:
            print_str.append(items.__str__())
        print(print_str)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Some edge case and their handles are as follows:
            - If the class name is missing, print ** class name missing **
            (ex: $ update)
            - If the class name doesn’t exist, print ** class doesn't exist **
            (ex: $ update MyModel)
            - If the id is missing, print ** instance id missing **
            (ex: $ update BaseModel)
            - If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ update BaseModel 121212)
            - If the attribute name is missing, print ** attribute name missing
            ** (ex: $ update BaseModel existing-id)
            - If the value for the attribute name doesn’t exist, print
            ** value missing ** (ex: $ update BaseModel existing-id first_name)
        """

        if arg is None or len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = "{0:s}.{1:s}".format(args[0], args[1])
                    dictionary = storage.all()
                    if key not in dictionary:
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            numbers = ["number_rooms", "number_bathrooms",
                                       "max_guest", "price_by_night"]
                            dec_numbers = ["latitude", "longitude"]
                            attrib = args[2]
                            value = args[3]
                            value = value.strip("\"")
                            if attrib in numbers:
                                dictionary[key][attrib] = int(value)
                            elif attrib in dec_numbers:
                                dictionary[key][attrib] = float(value)
                            elif attrib == "amenity_ids":
                                dictionary[key][attrib] = list(value)
                            else:
                                dictionary[key][attrib] = str(value)
                            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
