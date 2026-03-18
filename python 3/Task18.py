for i in range(1, 6):          # Outer loop for tables 1 to 5
    print(f"Multiplication Table of {i}:")
    for j in range(1, 11):     # Inner loop for 1 to 10
        print(f"{i} x {j} = {i*j}")
    print()