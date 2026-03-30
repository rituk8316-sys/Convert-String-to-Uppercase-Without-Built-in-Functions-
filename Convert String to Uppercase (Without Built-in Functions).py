# Program to convert a string to uppercase without using built-in functions
# Author: Your Name
# Description: This program converts lowercase letters to uppercase manually

def to_uppercase(text):
    result = ""

    for char in text:
        # Check if character is lowercase letter
        if 'a' <= char <= 'z':
            # Convert using ASCII value
            upper_char = chr(ord(char) - 32)
            result += upper_char
        else:
            result += char

    return result


# Taking input from user
input_string = input("Enter a string: ")

# Function call
output_string = to_uppercase(input_string)

# Output
print("Uppercase string is:", output_string)
