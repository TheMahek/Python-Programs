# Define a class
class My_class:
    # Define a class method using @classmethod decorator
    @classmethod
    def class_method(cls):
        print("This is Class Method.")

# Create an object of My_class
obj = My_class()

# Call class method using the object
obj.class_method()       # Output: This is Class Method.

# Call class method directly using the class
My_class.class_method()  # Output: This is Class Method.
