
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using a global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using a global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature and unit from the user
        temp = input("Enter the temperature (numeric value): ")
        unit = input("Is this in Celsius or Fahrenheit? (Enter 'C' for Celsius or 'F' for Fahrenheit): ").strip().upper()

        # Convert input temperature to a float
        temp = float(temp)

        # Convert and display the result based on the unit
        if unit == 'F':
            print(f"The temperature in Celsius is: {convert_to_celsius(temp):.2f}°C")
        elif unit == 'C':
            print(f"The temperature in Fahrenheit is: {convert_to_fahrenheit(temp):.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
