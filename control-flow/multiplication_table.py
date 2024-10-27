def multiplication_table():
    # Prompt the user to input a number
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return
    
    # Use a for loop to print the multiplication table for the entered number
    print(f"Multiplication table for {number}:")
    for i in range(1, 11): # range works with n, n-1 that's why this is 11 not 10
        result = number * i
        print(f"{number} * {i} = {result}")

# Run the function
if name == "main":
    multiplication_table()
