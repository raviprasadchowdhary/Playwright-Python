# For loops in Python are used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# The for loop in Python is more like a "for each" loop found in other programming languages.
# Here's the syntax of a for loop in Python:
# for item in sequence:
#     # do something with item

# Example of a for loop iterating over a list:
fruits = ["apple", "banana", "citrus", "grapes"]
for item in fruits:
    print(item)

# Example of a for loop iterating over a string:
givenName = "Raviprasad"
for singleCharacter in givenName:
    print(singleCharacter)

# Example of a for loop iterating over a dictionary:
studentDetails = {
    "givenName": "Raviprasad"
    , "surname": "Chowdhary"
    , "age": 25
    , "isStudent": False
    , "address": {
        "House Number": 123
        ,"addressLine1": "Church Street"
        ,"addressLine2": "4th Cross"
        ,"city": "Pune"
        ,"State": "MH"
        , "Country": "India"
    }
}
for key in studentDetails:
    if type(studentDetails[key]) == dict:
        print("Address details:")
        for nestedKey in studentDetails[key]:
            print("    ", nestedKey, ": ", studentDetails[key][nestedKey])
    else:
        print(key, ": ", studentDetails[key])

# Example of using the range() function with a for loop:
for i in range(5): # generates numbers from 0 to 4
    print(i)

for i in range(1,10,2):  # start from 1, go up to (but not including) 10, step by 2
    print(i)

# Example of nested for loops:
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Example of using break and continue statements in a for loop:
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)  # this will print only odd numbers less than 5

# Example of using else with a for loop:
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
# The else block will execute only if the loop completes normally (i.e., not terminated by a break statement).

