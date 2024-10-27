
# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to go through each row of the square pattern
while row < size:
    # Use a for loop to print the asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Move to the next line after printing a full row
    row += 1  # Increment the row counter
