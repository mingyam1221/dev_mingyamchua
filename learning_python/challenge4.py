message = input("Enter your message: ")
char = input("Enter the character to find in the message: ")
loc = message.find(char)
print(f"First occurence of {char} in {message} is at location {loc}.")
