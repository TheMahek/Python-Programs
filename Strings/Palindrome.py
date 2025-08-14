# Input from user
text = input("Enter a string: ")

# Remove spaces and make lowercase for uniform comparison
cleaned_text = text.replace(" ", "").lower()

# Check palindrome by reversing the string
if cleaned_text == cleaned_text[::-1]:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
