food = ["rice", "beans"]
print(f"1: {food}")

food.append("broccoli")
print(f"2: {food}")

food.extend(["bread", "pizza"])
print(f"3: {food}")

print(f"4: {food[0:2]}")

print(f"5: {food[-1]}")

breakfast = list("eggs, fruit, orange juice".split(", "))
print(f"6: {breakfast}")

print(f"7: {len(breakfast)}")

lengths = [len(item) for item in breakfast]
print(f"8: {lengths}")
