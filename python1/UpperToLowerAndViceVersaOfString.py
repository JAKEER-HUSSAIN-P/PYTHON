# Program to swap uppercase to lowercase and vice versa
input_string = input("Enter a string: ")

# Initialize an empty result string
converted_string = ''

# Iterate through each character in the input string
for char in input_string:
    if 'A' <= char <= 'Z':  # Check if character is uppercase
        # Convert to lowercase by adding 32 to ASCII value
        converted_string += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':  # Check if character is lowercase
        # Convert to uppercase by subtracting 32 from ASCII value
        converted_string += chr(ord(char) - 32)
    else:
        # Keep non-alphabetic characters unchanged
        converted_string += char

print("Converted string:", converted_string)
