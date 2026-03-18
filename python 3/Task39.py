numbers = [10, 20, 30, 40, 50]  # initial list
reversed_list = []

# Reverse using loop
for i in numbers:
    reversed_list = [i] + reversed_list  # prepend each element

print("Reversed list:", reversed_list)