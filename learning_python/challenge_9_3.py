data = ((1, 2), (3, 4))
print(f"1:  {data}")

for item in range(len(data)):
    total = sum(data[item])
    print(f"Row {item + 1} sum: {total}")

numbers = [4, 3, 2, 1]
print(f"3: {numbers}")

numbers_copy = numbers[:]
numbers_copy[1] = 0
print(f"4: numbers = {numbers}")
print(f"4: numbers_copy = {numbers_copy}")

numbers.sort()
print(f"5: sorted numbers = {numbers}")
