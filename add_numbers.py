def add_positive_numbers(num1, num2):
    """
    Add two positive numbers.
    
    Args:
        num1: First positive number
        num2: Second positive number
    
    Returns:
        Sum of the two numbers
    """
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Both numbers must be positive")
    
    return num1 + num2


if __name__ == "__main__":
    # Get input from user
    try:
        number1 = float(input("Enter the first positive number: "))
        number2 = float(input("Enter the second positive number: "))
        
        result = add_positive_numbers(number1, number2)
        print(f"The sum of {number1} and {number2} is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
