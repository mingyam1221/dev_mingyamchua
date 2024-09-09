def convert_cel_to_far(C):
    """A function that takes a value in degree Celcius and returns its temperature in degree Farenheit"""
    F = C * 9/5 + 32
    return F

def convert_far_to_cel(F):
    """A function that takes a value in degree Fahrenheit and returns its temperature in degree Celcius"""
    C = (F - 32) * 5/9
    return C

F1 = input("Enter a temperature in degrees F: ")
C1 = convert_far_to_cel(float(F1))
print(f"{F1} degrees F = {C1:.2f} degrees C")

C2 = input("Enter a temperature in degrees C: ")
F2 = convert_cel_to_far(float(C2))
print(f"{C2} degrees C = {F2:.2f} degrees F")
