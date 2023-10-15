#!/usr/bin/python3
"""This the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
     _valid_classes = {
     'BaseModel': BaseModel,
     'Place': Place,
     'State': State,
     'City': City,
     'Amenity': Amenity,
     'Review': Review,
}

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        arg1 = arg.split()
        if len(arg1) == 0:
            print("** class  name  missing **")
        else:
            class_name = arg1[0]
            try:
               new_instance = eval(class_name)()
               new_instance.save()
               print(new_instance.id)
            except NameError:
                print("** class doesn't exist  **")

     def do_show(self, arg):
         arg1 = arg.split()
         if len(arg1) == 0:
             print("** class name missing **")
         elif len(arg1) == 1:
             print("** instance id missing **")
         else:
             class_name = arg1[0]
             instance_id = arg1[1]

             try:
                instance = storage.all()[f"{class_name}.{instance_id}"]
                print(instance)
             except KeyError:
                 print("** no instance found **")

       def do_destroy(self, arg):
           arg1 = arg.spilt()
           if len(arg1) == 0:
               print("** class name missing **")
           elif len(arg1) == 1:
                print("** instance id missing **")
           else:
               class_name = arg1[0]
               instance_id = arg1[1]

               try:
                  objects = storage.all()
                  key = f"{class_name}.{instance_id}"
                  if key in objects:
                      del objects[key]
                      storage.save()
                  else:
                     print("** no instance found **")
               except KeyError:
                   print("** class doesn't exist  **")

        def do_all(self, arg):
            if not arg:
                print([str(instance) for instance in storage.all().values()])
            else:
                class_name = arg
                try:
                   print([str(instance) for key, instance in storage.all().items() if key.spilt('.')[0] == class_name])
                except NameError:
                    print("** class doesn't exist **")

        def do_update(self, arg):
            arg1 = arg.split()
            if len(arg1) == 0:
                print("** class name missing **")
            elif len(arg1) == 1:
                print("** instance id missing **")
            elif len(arg1) == 2:
                print("** attribute name missing **")
            elif len(arg1) == 3:
                print("** value missing **")
            else:
                class_name = arg1[0]
                instance_id = arg1[0]
                attribute_name = arg1[2]
                attribute_value = arg1[3]

            try:
               objects = storage.all()
               key = f"{class_name}.{instance_id}"
               if key in objects:
                   instance = objects[key]
                   setattr(instance, attribute_name, attribute_value)
                   instance.save()
               else:
                  print("** no instance found **")
           except KeyError:
               print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop
