#!/usr/bin/python3
"""
modules for the HBNB class
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import sys
import re
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
    prompt = '(hbnb) '
    Classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    """
    Parsing the input to figure out whether it's a 'class.method'
    pattern or not. If so, we can then match the method to a corresponding
    'do_<method>'
    """
    def do_BaseModel(self, arg):
        """Interprets BaseModel"""
        self.parser("BaseModel", arg)

    def do_User(self, arg):
        """Interprets User"""
        self.parser("User", arg)

    def do_State(self, arg):
        """Interprets State"""
        self.parser("State", arg)

    def do_City(self, arg):
        """Interprets City"""
        self.parser("City", arg)

    def do_Amenity(self, arg):
        """Interprets Amenity"""
        self.parser("Amenity", arg)

    def do_Place(self, arg):
        """Interprets Place"""
        self.parser("Place", arg)

    def do_Review(self, arg):
        """Interprets Review"""
        self.parser("Review", arg)

    def parser(self, cls, arg):
        """Parses command line"""
        argSplit = arg.split('.')
        command = argSplit[1].split('(')[0]
        try:
            if command == "all":
                self.do_all(cls)
            elif command == "count":
                self.do_count(cls)
            elif command == "show":
                id = argSplit[1].split('"')[1]
                self.do_show(cls + " " + id)
            elif command == "destroy":
                id = argSplit[1].split('"')[1]
                self.do_destroy(cls + " " + id)
            elif command == "update":
                id = re.split('"|\'', argSplit[1])[1]
                attr_name = re.split('"|\'', argSplit[1])[3]
                attr_value = re.split('"|\'', argSplit[1])[5]
                self.do_update(cls + " "
                               + id + " " + attr_name + " "
                               + attr_value)
            else:
                print("** command doesn't exist **")
        except Exception as e:
            print(e)

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
        obj_dict = models.storage.all()
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
            return
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
        obj_dict = models.storage.all()
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
            return
        else:
            K = args[0] + '.' + args[1]
            if K in obj_dict:
                del obj_dict[K]
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, line=None):
        """
        prints all str representation of all instances
        """
        obj_str = []
        obj_dict = models.storage.all()
        if not line:
            """
            Case scenario when only 'all' is called
            """
            for obj in obj_dict.values():
                str_rep = str(obj)
                obj_str.append(str_rep)
            print(obj_str)
        else:
            """Case scenario when it is called either by
            '<class_name>.all()' or 'all <class_name'"""
            if line not in self.Classes:
                print("** class doesn't exist **")
                return
            else:
                for obj in obj_dict.values():
                    if obj.__class__.__name__ == line:
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
            print("** attribute name or dictionary missing **")
            return
        if isinstance(args[2], dict):
            attr_dict = args[2]
            for attr, value in attr_dict.items():
                if attr not in ['id', 'created_at', 'updated_at']:
                    setattr(obj_dict[K], attr, value)
        else:
            attr_name = args[2]
            if attr_name == "id" or attr_name == "created_at"\
                    or attr_name == "updated_at":
                print("** attribute id, created_at and\
                      updated_at cannot be updated  **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            attr_val = args[3]
            attr_type = type(getattr(obj_dict[K], attr_name))
            try:
                result = attr_type(attr_val)
                setattr(obj_dict[K], attr_name, result)
            except ValueError:
                print("** Value not found **")
            models.storage.save()
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
