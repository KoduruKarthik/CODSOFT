num1 = float(input("Enter the first number: "))
operator = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter +, -, *, or /.")
print("Result:"result)
