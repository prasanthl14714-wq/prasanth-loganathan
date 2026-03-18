while True:
    user_input = input("Enter something (type 'stop' to quit): ")
    if user_input.lower() == "stop":
        print("Program stopped.")
        break
    else:
        print("You entered:", user_input)