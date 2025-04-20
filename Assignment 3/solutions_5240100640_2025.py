"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    name_parts = full_name.split()
    initials = ''.join([name[0].upper() for name in name_parts])
    return initials
user_full_name = input("Enter your full name: ")
print("Your initials are:", get_initials(user_full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(string):
    # Remove any spaces and convert the string to lowercase for comparison
    clean_string = string.replace(" ", "").lower()
    return clean_string == clean_string[::-1]
user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Please enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The number of words in the sentence is: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print("Modified string:", modified_string)
