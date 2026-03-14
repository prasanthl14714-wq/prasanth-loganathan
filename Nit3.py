age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected for sports")
        else:
            print("Rejected due to weight")
    else:
        print("Rejected due to height")
else:
    print("Rejected due to age")