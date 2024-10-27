def draw_square_pattern():
    # Prompt the user to input a positive integer for the pattern size
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
        return
    
    # Use nested loops to print the square pattern
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()  # Move to the next line after each row

# Run the function
if name == "main":
    draw_square_pattern()