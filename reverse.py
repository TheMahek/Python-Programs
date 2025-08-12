# reverse string 
string = input("Enter a string : ") #input from user 
reversed_string = " " #an empty string to store reversed version 
for char in string:
   reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")