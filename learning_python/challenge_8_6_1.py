while (True):
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Try again.")
