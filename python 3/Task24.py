text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # add each char at the beginning

print("Reversed string:", reversed_text)