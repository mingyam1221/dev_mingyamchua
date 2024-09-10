import random

def roll():
    """Return a random integer between 1 and 6."""
    return random.randint(1, 6)

total = 0
n = 100_000

for i in range(n):
    total = total + roll()

print(total)
print(n)
print(total/n)
