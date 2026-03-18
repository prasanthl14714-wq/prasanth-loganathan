num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10   # remove last digit
    count += 1        # increase digit count

print("Number of digits:", count)