#!/usr/bin/python3
"""console"""
import cmd


if __name__ == '__main__':

    class HBNBCommand(cmd.Cmd):
        """console"""

        prompt = "(hbnb) "
        intro = ""

        def emptyline(self):
            """Pass if the input is an empty line"""

        def do_quit(self, args):
            """Quit command to exit the program"""
            exit()

        def do_EOF(self, args):
            """Exits from the console"""
            print()
            exit()

    HBNBCommand().cmdloop()
