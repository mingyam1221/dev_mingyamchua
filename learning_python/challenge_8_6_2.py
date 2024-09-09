try:
    string = input("Enter a string: ")
    index = int(input("Enter the index number to show: "))
    print(string[index])

except IndexError:
    print("Index is out of bound.")

except ValueError:
    print("The entered index is not a number.")
