amount = float(input("Enter an amount: "))

for num_people in range(2, 6):
    amount_split = amount / num_people
    print(f"{num_people} people: ${amount_split:.2f} each")
