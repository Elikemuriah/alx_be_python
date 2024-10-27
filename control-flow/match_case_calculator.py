def match_case_calculator():
    # Prompt for the first and second numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Prompt for the operation
    operation = input("Select an operation (+, -, *, /): ")

    # Match case statement to perform the appropriate calculation
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        case "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        case "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        case "/":
            if num2 == 0:
                print("Error: Division by zero is undefined.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        case _:
            print("Invalid operation! Please select +, -, *, or /.")

# Run the calculator
if name == "main":
    match_case_calculator()