
from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date():
    # Prompt the user to enter a number of days
    try:
        days_to_add = int(input("Enter the number of days to add: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    # Calculate the future date by adding the specified days
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days: {formatted_future_date}")

# Run the functions
if name == "main":
    display_current_datetime()
    calculate_future_date()