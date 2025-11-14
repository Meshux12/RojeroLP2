
class Parent:

       def greet(self):

           print("Hello from Parent")


class Child(Parent):

       def greet(self):

           print("Hello from Child")


child = Child()

child.greet()