cats = [False for i in range(100)]
print(cats)

for j in range(100):
    for i in range(100):
        if ((i + 1) % (j + 1)) == 0:
            cats[i] = not(cats[i])
            print(f"i = {j + 1}, j = {i + 1}, {(i + 1) % (j + 1)}")
    print(cats)
