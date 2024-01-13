#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """Defines the Command Interpreter."""

    prompt = "(hbnb)"
    classes = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]

    def do_EOF(self, arg):
        """ EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def emptyline(self):
        """ Empty line - Not Excute anything"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id"""
        a = arg.split()
        if not arg:
            print("** class name missing **")
        elif a[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(a) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(a[0], a[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(a[0], a[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        a = arg.split()
        if not arg:
            print("** class name missing **")
        elif elif a[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(a) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(a[0], a[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(a[0], a[1])]
            storage.save()

    def d0_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
