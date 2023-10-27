#!/usr/bin/python3
"""console"""
import cmd
import models
import json

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
            
        def do_create(self, arg):
            """Creates a BaseModel instance"""
            args = arg.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                instance = models.base_model.BaseModel()
                instance.save()
                print(instance.id)
                
        def do_show(self, arg):
            "Prints the string representation of an instance based on the class name and id."
            args = arg.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                flag = 0
                with open("file.json", "r", encoding="utf-8") as file:
                    dic = json.loads(file.read())
                    for key in dic.keys():
                        id = key.split(".")
                        if id[1] == args[1]:
                            instance = models.base_model.BaseModel(dic[key])
                            print(instance)
                            flag = 1
                    if flag != 1:
                        print("** no instance found **")
        
        def do_destroy(self, arg):
            "Erases an instance from the json file based on the class name and id."
            args = arg.split()
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                flag = 0
                with open("file.json", "r+", encoding="utf-8") as file:
                    dic = json.loads(file.read())
                    for key in dic.keys():
                        id = key.split(".")
                        if id[1] == args[1]:
                            key_copy = key
                            flag = 1
                    dic.pop(key_copy)
                with open("file.json", "w", encoding="utf-8") as file:
                    file.write(json.dumps(str(dic)))    
                if flag != 1:
                    print("** no instance found **")

    HBNBCommand().cmdloop()
