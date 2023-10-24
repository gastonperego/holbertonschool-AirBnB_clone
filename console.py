#!/usr/bin/python3
"""console"""
import cmd


if __name__ == '__main__':
    
    class HBNBCommand(cmd.Cmd):
        """console"""

        prompt = "(hbnb) "
        intro = ""

        def do_EOF(self, args):
            """Exits from the console"""
            print()
            exit()

HBNBCommand().cmdloop()

