age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected due to weight")
    else:
        print("Rejected due to height")
else:
    print("Rejected due to age")
