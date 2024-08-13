# Program to find the least repeated character in a string
input_string = input("Enter a string: ")

# Create a dictionary to count occurrences of each character
char_count = {}

# Count occurrences of each character
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find the least repeated character
least_repeated_char = min(char_count, key=char_count.get)
least_repeated_count = char_count[least_repeated_char]

print(f"The least repeated character is '{least_repeated_char}' with {least_repeated_count} occurrences.")
