total = 0
n = 10_000

for i in range(n):
    total = total + roll()

print(total/n)
