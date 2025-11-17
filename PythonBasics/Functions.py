# Functions

# A function is a block of reusable code that performs a specific task.
# Functions help to organize code, make it more readable, and allow for code reuse.

# Defining a function
def greet(name):
    print(f"Hello, {name}, how are you?")
# Calling a function
greet("Raviprasad")

# Function with return value
def sum_of_numbers(a,b):
    return a+b
# calling the function and printing the result
print(f"Sum: {sum_of_numbers(1,2)}")

# Function with default parameters
def greet_with_default(name="Guest"):
    print(f"Hello, {name}, Welcome!")
# calling the function with and without argument
greet_with_default("Raviprasad")
greet_with_default()
