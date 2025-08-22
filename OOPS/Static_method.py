class My_class:
    # Define a static method
    @staticmethod
    def static_method():
        return "This is a static method."

# Create an object
obj = My_class()

# Call static method using object
print(obj.static_method())     # Output: This is a static method.

# Call static method using class
print(My_class.static_method())  # Output: This is a static method.
