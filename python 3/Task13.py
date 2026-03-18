num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10       # get the last digit
    rev = rev * 10 + digit # append digit to reverse
    num = num // 10        # remove last digit

print("Reversed number is:", rev)