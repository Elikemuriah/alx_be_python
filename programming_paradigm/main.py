import sys
from robust_division_calculator import safe_divide

def main():
    # Ensure that two arguments (numerator and denominator) are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return
    
    # Retrieve the numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform division and display result or error message
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
