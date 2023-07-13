# 0x00. AirBnB clone - The console
`Group project` `Python` `OOP` <br>
An implementation to know and understand how the airbnb project works

![alt text](pics/hbnb.png)

## Tasks
0. **README, AUTHORS** <br>
*mandatory*
- Write a README.md:
- description of the project

**Description of the project**
- The overall goal of the project is to deploy a simple copy of the AirBnB website from my server
- After 4 Months, we should have a complete web application composed by:
  - A command interpreter to manipulate data without a visual interface, like in a shell (perfect for development and debugging)
  - A website (the front-end) that shows the final product to everybody: static & dynamic
  - A database or files that store data (data == objects)
  - An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

**First Part - The console**
- Create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

- The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My Object" and "How they are stored and persisted".
- This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won't have to pay attention (take care) of how your objects are stored
- This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
- The console will be a tool to validate this storage engine.

![alt text](pics/console.png)

#### More Info
**Description of the command line interpreter**
- command line interpreter that allows users to interact through command lines.Users interact with a system.
- Designed to be both interactive and non-interactive
- CMD module provides a framework for building line-oriented command interpreters.

**How to start it**
- Open a terminal or a command prompt
- Create a file, begin with importing the CMD module and write your contents
- Run your file using `(./)` example, `./main.py`
`(cmd)` appears without parentheses.

**How to use it**
- To execute a command type the word that occurs after do, method will be called
- help command shows a list of commands available
- help followed by a command name displays more information of the command
- Tab key is used for auto-completion commands

**Examples**
```Python
  >> commandName
To execute a command
  >> commandName arg1
Execute a command with arguments
  >> help
Shows a list of available commands
  >> help commandName
Displays more information of the command
```

- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page

- You should use branches and pull requests on GitHub - it will help you as team to organize your work

1. **Be pycodestyle compliant!** <br>
*mandatory*
- Write beautiful code that passes the pycodestyle checks.

2. **Unittests** <br>
*mandatory*
- All your files, classes, functions must be tested with unit tests
- Unit tests must also pass in non-interactive mode:

3. **BaseModel** <br>
*mandatory*
- Write a class BaseModel that defines all common attributes/methods for other classes
- models/base_model.py
- Public instance attributes:
 - id: string - assign with an uuid when an instance is created
 - you can use uuid.uuid4() to generate unique id but don't forget to convert to a stirng
 - the goal is to have unique id for each BaseModel
- created_at: datetime-assign with the current datetime when an instance is created
- updated_at: datetime-assign with the current datetime when an instance is created and it will be updated every time you change your object
- __str__: should print [<class name>] (<self.id>) <self.__dict__>
- public instance methods:
 - save(self): updates the public instance attribute updated_at with the current datetime
 - to_dict(self): returns a dictionary containing all key/values of __dict__ of the instance:
   - by using self.__dict__, only instance attributes set will be returned
   - a key __class__ mst be added to this dictionary with the class name of the object
   - created_at and updated_at must be converted to string object in ISO format:
   - format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
   - you can use isoformat() of datetime object
- This method will be the first piece of the serialization/deserialization process: create a dictionary representation with "simple object type" of our BaseModel

4. **Create BaseModel from dictionary**
*mandatory*
- re-create an instance with this dictionary representation.
```Python
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
- Update models/base_model.py:
`__init__(self, *args, **kwargs):`
- you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
- *args won’t be used
- if kwargs is not empty:
- each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
- each value of this dictionary is the value of this attribute name
- Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
- otherwise:
- create id and created_at as you did previously (new instance)

5. **Store first object** <br>
*mandatory*
- Now we can recreate a BaseModel from another one by using a dictionary representation
```Python
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
- it's great but it's still not persistent; every time you launch the program, you don't restore all objects created before... The first way you will see here is to save these objects to a file
- So, we will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.
- Now the flow of serialization-deserialization will be:
```Python
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
- Write a class `Filestorage` that serializes instances to a JSON file and deserializes JSON file to instances:
  - models/engine/file_storage.py
  - Private class attributes:
    - __file_path: string - path to the JSON file (ex: file.json)
    - __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
  - Public instance methods:
    - all(self): returns the dictionary __objects
    - new(self, obj): sets in __objects the obj with key <obj class name>.id
    - save(self): serializes __objects to the JSON file (path: __file_path)
    - reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
  - Update models/__init__.py: to create a unique FileStorage instance for your application
    - import file_storage.py
    - create the variable storage, an instance of FileStorage
    - call reload() method on this variable
  - Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage
    - import the variable storage
    - in the method save(self):
      - call save(self) method of storage
    - __init__(self, *args, **kwargs):
      - if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage

6. **Console 0.0.1** <br>
*mandatory*
Write a program called `console.py` that contains the entry point of the command interpreter:
- You must use the module `cmd`
- Your class definition must be: `class HBNBCommand(cmd.Cmd):`
- Your command interpreter should implement:
  - quit and EOF to exit the program
  - `help`` (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
  - a custom prompt: (hbnb)
  - an empty line + ENTER shouldn’t execute anything
  - Your code should not be executed when imported
**Warning:**
You should end your file with:
```Python
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```
to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise
```Python
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
guillaume@ubuntu:~/AirBnB$
```
**No unittests needed**