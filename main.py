"""
Calculator Project (Python)
Author: TRISNA ROY

Features:
- Addition, Subtraction, Multiplication, Division
- Error Handling
- Loop system
- Calculation History
"""

# store calculation history
history = []

# calculator function
def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"


# main program
print("=== Welcome to TRISNA ROY's Calculator ===")

while True:
    try:
        # input numbers
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        # input operator
        op = input("Enter operator (+, -, *, /): ")

        # calculation
        result = calculate(num1, num2, op)

        # output
        print("Result:", result)

        # save history (only if valid)
        if result != "Invalid operator":
            history.append(f"{num1} {op} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    # continue option
    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() == "no":
        break


# show history
print("\n=== Calculation History ===")
for item in history:
    print(item)

print("\nThank you for using TRISNA ROY's calculator!")