#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import sys
import models


class HBNBCommand(cmd.Cmd):
    """
    class defination of the cmd module
    """
    prompt = '(hbnb)'
    Classes = {
        "BaseModel"
    }

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Quit command to exit the program
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
        try:
            cls_name = args[0]
            if cls_name not in self.Classes:
                print("** class doesn't exist **")
            inst = eval(cls_name)()
            inst.save()
            print(inst.id)
        except Exception:
            pass

    def do_show(self, line):
        """
        print string representation of an instance
        based on class name and id
        """
        args = shlex.split(line)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
            K = args[0] + '.' + args[1]
            if K in obj_dict:
                print(obj_dict[K])
            else:
                print("** no instance found **")
        return

    def destroy(self, line):
        """
        deletes instance based on class name and id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
            obj_dict = models.storage.all()
            K = args[0] + '.' + args[1]
            if K in obj_dict:
                del obj_dic[K]
                models.storage.all()
            else:
                print("** no instance found **")

    def all(self, line):
        """
        prints all str representation of all instances
        """
        args = shlex.split(line)
        obj_str = []
        obj_dict = models.storage.all()
        if len(args) == 0:
            for K in obj_dict:
                str_rep = str(obj_dict[K])
                obj_str.append(str_rep)
            print(obj_str)

        if args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
            obj_str = []
            for K in obj_dict:
                cls_name = K.split('0')
                if cls_name[0] == args[0]:
                    str_rep = str(obj_dict[K])
                    obj_str.append(str_rep)
            print(obj_str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
