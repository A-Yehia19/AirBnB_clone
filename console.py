#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the Command Interpreter."""

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """ EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def empty_line(self):
        """ Empty line - Not Excute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
