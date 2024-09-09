num = int(input("Enter a positive integer: "))
for i in range(num):
    divisor = i + 1
    remainder = num % divisor
    if remainder == 0:
        print(f"{divisor} is a factor of {num}")
