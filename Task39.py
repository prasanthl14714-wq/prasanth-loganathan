num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid number! Please enter 1, 2, or 3.")