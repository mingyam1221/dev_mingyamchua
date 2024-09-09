def invest(amount, rate, years):
    for loop in range(years):
        amount = amount * (1 + 0.05)
        print(f"year {loop + 1}: ${amount:.2f}")

amount = float(input("Enter initial amount: "))
rate = float(input("Enter annual percentage rate: "))
years = int(input("Enter the number of years: "))
invest(amount, rate, years)
