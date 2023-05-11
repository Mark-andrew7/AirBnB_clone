#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class defination
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """
        exits the program
        """
        return True

    def do_EOF(self, line):
        """
        exits the program
        """
        return True

    def emptyline(line):
        """
        plus enter doesnt execute anything
        """
        pass

    def do_create(self, line):
        """
        create new instance of Basemodel and saves it
        """
        if not line:
            print("** class name missing **")

        try:
            Class = eval(line)
            inst = Class()
            inst.save()
            print (inst.id)
        except NameError:
            print("** class doesn't exist **")

    
    def do_show(
if __name__ == '__main__':
    HBNBCommand().cmdloop()
