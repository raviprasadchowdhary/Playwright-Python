# String
# Strings are used to store text data in Python. They are enclosed in either single quotes (' ') or double quotes (" ").

# Creating strings
string1 = 'Hello, World!'
string2 = "Python is fun."

# Accessing characters in a string
first_char = string1[0]  # 'H'
last_char = string1[-1]  # '!'
substring = string1[0:5]  # 'Hello'
print("First Character:", first_char)
print("Last Character:", last_char)
print("Substring:", substring)

# String methods
upper_string = string1.upper()  # 'HELLO, WORLD!'
lower_string = string2.lower()  # 'python is fun.'
split_string = string1.split(',')  # ['Hello', ' World!']
joined_string = ' '.join(['Python', 'is', 'awesome!'])  # 'Python is awesome!'
print("Uppercase:", upper_string)
print("Lowercase:", lower_string)
print("Split String:", split_string)
print("Joined String:", joined_string)

# String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)

# String concatenation
greeting = string1 + " " + string2  # 'Hello, World! Python is fun.'
print("Concatenated String:", greeting)
# String repetition
repeated_string = "Ha! " * 3  # 'Ha! Ha! Ha! '
print("Repeated String:", repeated_string)
# String length
length_of_string = len(string1)  # 13
print("Length of String:", length_of_string)
# Checking substring
contains_world = 'World' in string1  # True
print("Contains 'World':", contains_world)

# Example usage:
print("Original String 1:", string1)
print("Original String 2:", string2)
print("Greeting:", greeting)
print("Repeated String:", repeated_string)
print("Length of String 1:", length_of_string)
print("Does String 1 contain 'World'?", contains_world)

# Output:
# First Character: H
# Last Character: !
# Substring: Hello
# Uppercase: HELLO, WORLD!
# Lowercase: python is fun.
# Split String: ['Hello', ' World!']
# Joined String: Python is awesome!
# Formatted String: My name is Alice and I am 30 years old.
# Concatenated String: Hello, World! Python is fun.
# Repeated String: Ha! Ha! Ha!
# Length of String: 13
# Contains 'World': True
# Original String 1: Hello, World!
# Original String 2: Python is fun.
# Greeting: Hello, World! Python is fun.
# Repeated String: Ha! Ha! Ha!
# Length of String 1: 13
# Does String 1 contain 'World'? True
