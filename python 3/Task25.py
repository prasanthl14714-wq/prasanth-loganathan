text = input("Enter a string: ")
reversed_text = ""

# Reverse the string
for char in text:
    reversed_text = char + reversed_text

# Check if original and reversed strings are the same
if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")