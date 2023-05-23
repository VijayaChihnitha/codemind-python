def is_isogram(s):
    # Convert the string to lowercase to consider characters as case-insensitive
    s = s.lower()
    
    # Create a set to store the unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the set, it is not an isogram
        if char in unique_chars:
            return False
        # Add the character to the set
        unique_chars.add(char)
    
    # If all characters are unique, it is an isogram
    return True

# Get the input string from the user
s = input()

# Check if the string is an isogram
is_isogram = is_isogram(s)

# Display the result
print(is_isogram)