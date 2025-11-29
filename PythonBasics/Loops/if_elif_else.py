# if, else if, else statements in Python
from openpyxl.descriptors import Integer
from openpyxl.pivot.fields import Number

# Python uses 'elif' for 'else if' statements
# Python does not have a switch-case statement like some other languages
# Python relies on if-elif-else constructs for conditional branching
# Python uses indentation to define blocks of code
# Python uses colons (:) to indicate the start of a new block
# Python evaluates conditions in order and executes the first block where the condition is true
# Python supports nested if-elif-else statements
# Python allows for multiple conditions to be checked in a single if statement using logical operators (and, or, not)
# Python does not require parentheses around conditions, but they can be used for clarity
# Python supports ternary conditional expressions for simple if-else statements

# Example of if, elif, else statements in Python

# code to find if age falls in child, teenager, adult category
age = 10
if age<13:
    print("The person is: Child")
elif 12 >= age >19:
    print("The person is: Teenager")
else:
    print("The person is adult")

# Example of nested if-elif-else statements

# code to find if a number is positive, negative or zero and also check if it is even or odd

number = 2
print(type(number))
if Integer == type(number):
    if number > 0:
        if number % 2 == 0:
            print(f"The number {number} is positive-even")
        else:
            print(f"The number {number} positive-odd")
    elif number < 0:
        if number % 2 == 0:
            print(f"The number {number} is negative-even")
        else:
            print(f"The number {number} is negative-odd")
    else:
        print(f"The number is zero")
else:
    print("The input is not a valid integer")

# Example of using logical operators in conditions
# Example of ternary conditional expression