numbers = [40, 10, 50, 20, 30]  # unsorted list
for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]  # swap

print("Sorted list:", numbers)