# Program to find the most repeated character in a string
input_string = input("Enter a string: ")

# Create a dictionary to count occurrences of each character
char_count = {}

# Count occurrences of each character
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find the most repeated character
most_repeated_char = max(char_count, key=char_count.get)
most_repeated_count = char_count[most_repeated_char]

print(f"The most repeated character is '{most_repeated_char}' with {most_repeated_count} occurrences.")
