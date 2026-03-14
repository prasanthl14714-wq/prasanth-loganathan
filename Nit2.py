marks = int(input("Enter your marks: "))
age = int(input("Enter your age: "))

if marks >= 60:
    if age >= 17:
        print("Eligible for admission")
    else:
        print("Not eligible due to age")
else:
    print("Not eligible due to marks")