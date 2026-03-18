numbers = [10, 25, 5, 40, 30]  # example list
element = int(input("Enter a number to check: "))

if element in numbers:
    print(element, "exists in the list.")
else:
    print(element, "does not exist in the list.")