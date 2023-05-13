#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class defination
    """
    prompt = '(hbnb)'
    Classes = {
        "BaseModel": BaseModel
    }

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
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]

        try:
            Class = self.Classes[cls_name]
            inst = Class()
            inst.save()
            print(inst.id)
        except NameError:
            print("** class doesn't exist **")

    
    def do_show(self, line):
        """
        print string representation of an instance
        based on class name and id
        """
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        
        cls_name = args[0]
        if cls_name not in self.Classes:
            print("** class doesn't exist **")

        if len(args) == 1:
            print("** instance id missing **")

        inst_id = args[1]
        key = "{} {}".format(cls_name, inst_id)
        if key not in obj_dict:
            print("** no instance found **")

        print(obj_dict[key])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
