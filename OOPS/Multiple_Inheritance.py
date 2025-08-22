# Parent class Mother
class Mother:
    mothername = ""  # Attribute to store mother's name
    
    def mother(self):
        # Method to print mother's name
        print(self.mothername)

# Parent class Father
class Father:
    fathername = " "  # Attribute to store father's name
    
    def father(self):
        # Method to print father's name
        print(self.fathername)

# Child class Son inheriting from both Mother and Father
class Son(Mother, Father):
    def parents(self):
        # Method to print both parents' names
        print("Father: ", self.fathername)
        print("Mother: ", self.mothername)

# Creating an object of Son
s1 = Son()

# Assigning names to inherited attributes
s1.fathername = "John"
s1.mothername = "Mary"

# Calling method to display parents' names
s1.parents()
