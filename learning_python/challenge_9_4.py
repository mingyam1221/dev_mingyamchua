universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]

def enrollment_stats(data):
    """ enrollment stats """
    list1 = []
    list2 = []
    for i in range(len(data)):
        list1.append(data[i][1])
        list2.append(data[i][2])
    return (list1, list2)

(enrollment, fees) = enrollment_stats(universities)
print(enrollment)
print(fees)

def mean(data):
    """Calculate mean of a list."""
    result = sum(data)/len(data)
    return result

def median(data):
    """Calculate median of a list."""
    data.sort()
    result = data[round(len(data) / 2)]     # not the most properway
    return result

print("******************************")
print(f"Total students:    {sum(enrollment):,}")
print(f"Total tuition:   $ {sum(fees):,.2f}")
print("\n")
print(f"Student mean:      {mean(enrollment):,.2f}")
print(f"Student median:    {median(enrollment):,.2f}")
print("\n")
print(f"Tuition mean:    $ {mean(fees):,.2f}")
print(f"Tuition median:  $ {median(fees):,.2f}")
print("****************************")
