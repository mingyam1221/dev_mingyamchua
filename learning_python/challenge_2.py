number1 = "33"
number1_str = int(number1)
print(number1_str * 3)

number2 = "33.3"
number2_str = float(number2)
print(number2_str * 3)

str1 = "123"
int1 = 456
print(str1 + str(int1))

input1 = input("Enter first number: ")
input2 = input("Enter second number: ")
result = float(input1) * float(input2)
#print("The product of " + input1 + " and " + input2 + " is " + str(float(input1) * float(input2)) + ".")
print(f"The product of {input1} and {input2} is {float(input1)*float(input2)}.")
