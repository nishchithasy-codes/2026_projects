a = float(input("Enter the first number: "))
b = input("Enter the operator (+, -, *, /): ")
c = float(input("Enter the second number: "))

if b == "+":
    result = a + c

elif b == "-":
    result = a - c

elif b == "*":
    result = a * c

elif b == "/":
    if c == 0:
        result = "Cannot divide by zero"
    else:
        result = a / c

else:
    result = "Invalid operator"

print("Result:", result)