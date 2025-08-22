# Grandfather class (base class)
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername  # Attribute for grandfather's name

# Father class (inherits from Grandfather)
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername  # Attribute for father's name
        super().__init__(grandfathername)  # Call Grandfather's constructor

# Son class (inherits from Father)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname  # Attribute for son's name
        super().__init__(fathername, grandfathername)  # Call Father's constructor

    def display(self):
        # Display all names
        print("Grandfather Name:", self.grandfathername)
        print("Father Name:", self.fathername)
        print("Son Name:", self.sonname)

# Create object of Son
s1 = Son("Michael", "John", "Robert")

# Display the names
s1.display()
