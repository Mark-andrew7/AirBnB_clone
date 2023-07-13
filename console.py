#!/usr/bin/python3
"""
modules for the HBNB class
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import sys
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class defination of the cmd module
    """
    prompt = '(hbnb)'
    Classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
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
        print()
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

    def do_destroy(self, line):
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
                del obj_dict[K]
                models.storage.all()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        prints all str representation of all instances
        """
        args = shlex.split(line)
        obj_str = []
        obj_dict = models.storage.all()
        if len(args) == 0:
            for obj in obj_dict.values():
                str_rep = str(obj)
                obj_str.append(str_rep)
            print(obj_str)

        if args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
            for obj in obj_dict.values():
                if obj.__class__.__name__ == args[0]:
                    str_rep = str(obj)
                    obj_str.append(str_rep)
            print(obj_str)

    def do_update(self, line):
        """
        updates instance based on class name and id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in self.Classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        inst = args[1]
        obj_dict = models.storage.all()
        K = args[0] + '.' + args[1]
        if K not in obj_dict:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
            print("** attribute id, created_at and updated_at cannot be updated  **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attr_val = args[3]
        attr_type = type(getattr(obj_dict[K], attr_name))

        try:
            result = attr_type(attr_val)
            setattr(obj_dict[K], attr_name, result)
            models.storage.save()
        except ValueError:
            print("** Value not found **")

        models.storage.reload()

    def do_count(self, line):
        """
        retrieves number of instances of a class
        """
        args = shlex.split(line)
        if len(args) == 1:
            cls_name = args[0]
        else:
            cls_name = args[0] + '.' + args[1]

        count = 0
        obj_dict = models.storage.all()
        for obj in obj_dict.values():
            if obj.__class__.__name__ == cls_name:
                count += 1

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
