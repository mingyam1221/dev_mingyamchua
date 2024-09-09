print("Using for loop,")
for m in range(2, 11):
    print(m)

print("\nUsing while loop,")
n = 2
while n <= 10:
    print(n)
    n = n + 1

print("\n\n")
def doubles(num):
    return num * 2

num = 2
for loop in range(3):
    num = doubles(num)
    print(num)


