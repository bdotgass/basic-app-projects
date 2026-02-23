"""
The function of this application is to take in an 8 digit binary number and return the decimal conversion
"""
import math


# Setup the core function. Accepts a binary number as a string
def binary_to_decimal(binary: str):
    # Check if binary is the right length
    if len(binary) > 8:
        return ValueError(f"{binary} is too long. 8 digits only.")
    
    # Check if entered string contains anything other than a 0 or 1
    allowed_nums = {'1', '0'}

    if not set(binary).issubset(allowed_nums):
        return ValueError(f"{binary} is not a valid binary number")
    
    # Make sure the entered value is not empty
    if (binary):
    
        # Create reversed version of string for ease of using enum for exponent values
        reversed_binary = binary[::-1]

        decimal_value = 0

        for i, letter in enumerate(reversed_binary):
            decimal_value = decimal_value + (int(letter) * math.pow(2, i))

        return int(decimal_value)
    
    else:
        return ValueError("Invalid input")

""" USE THIS PRINT FOR TESTING IN FUNCTION"""
#print(binary_to_decimal("111010"))
