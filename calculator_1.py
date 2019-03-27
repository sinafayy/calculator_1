x = int(input("Please enter the first number: "))
operation = input("Choose math operation (+, -, *, /) ")
y = int(input("Please enter the second number: "))


if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "/":
    print(x / y)
elif operation == "*":
    print(x * y)
else:
    print("I don't understand")
