#!/usr/bin/env python3
"""Module for console program."""

import json
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create method"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(command[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Show method"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy method"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            if key in objects.keys():
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all objects"""
        command = arg.split()
        objects = storage.all()
        if len(command) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == command[0]:
                    print(str(value))

    def do_update(self, arg):
        """Update instance"""
        command = arg.split()

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif len(command) == 2:
            print("** attribute name missing **")
        elif len(command) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"

            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                setattr(obj, command[2], command[3])
                obj.save()

    def default(self, arg):
        args = arg.split(".")
        cls_name = args[0]
        command = args[1].split("(")
        method = command[0]
        passed_arg = command[1].split(")")[0]
        all_args = passed_arg.split(",")  # for update method

        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        if method in argdict.keys():
            if method != "update":
                return argdict[method]("{} {}".format(cls_name, passed_arg))
            else:
                if "{" in passed_arg:
                    parts = passed_arg.split(',', 1)
                    kwargs = parts[1].strip()
                    kwargs = kwargs.replace("'", '"')
                    update_dict = json.loads(kwargs)
                    id = parts[0]

                    for key, value in update_dict.items():
                        argdict[method]("{} {} {} {}".format(
                            cls_name, id, key, value)
                        )
                    return
                else:
                    id, attr_name, attr_value = all_args
                    return argdict[method]("{} {} {} {}".format(
                        cls_name, id, attr_name, attr_value)
                    )

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Count number"""
        args = arg.split()
        cls_name = args[0]
        count = 0
        if len(args) == 1:
            if cls_name in self.__classes:
                for obj in storage.all().values():
                    if obj.__class__.__name__ == cls_name:
                        count += 1
                print(count)
            else:
                print("** class name invalid **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
