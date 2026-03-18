text = input("Enter a string: ")
if len(text) > 2:
    result = text[1:-1]
    print("String after removing first and last character:", result)
else:
    print("String is too short to remove characters.")