# Parent class
class Parent:
    # Method inside Parent class
    def func1(self):
        print("This Function is in parent class")

# Child class inheriting Parent
class Child(Parent):
    # Method inside Child class
    def func2(self):
        print("This Function is in Child class")

# Create object of Child class
object = Child()

# Child class can access Parent class method because of inheritance
object.func1()   # Output: This Function is in parent class

# Child class can also access its own method
object.func2()   # Output: This Function is in Child class
