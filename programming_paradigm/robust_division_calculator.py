
def safe_divide(numerator, denominator):
    
    #Attempts to divide the numerator by the denominator.
    #Handles division by zero and non-numeric input errors.
    #Returns the result or an appropriate error message.

    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
