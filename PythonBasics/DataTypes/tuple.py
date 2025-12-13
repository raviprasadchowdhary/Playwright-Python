# Tuple
# difference between list and tuple is that list is mutable and tuple is immutable
# Tuple is defined using parentheses () and elements are separated by commas

# Creating a tuple
tuple = (1, 2, 3.1, 3.2, True, False, "Raviprasad", "Chowdhary", 3 + 4j, 1 + 9j)
print("The elements of the tuple are: ", tuple)

# Accessing elements of a tuple
# accessing elements using index
# first element has index 0
print("The first element of the tuples is: ", tuple[0])
# last element has index -1
print("the last element of the tuple is: ", tuple[-1])

# Slicing a tuple
# slicing syntax: tuple[start:end:step]

# slicing from index 2 to index 4
print("slicing the tuple from index 2 to index 4: ", tuple[2:5])
# slicing from index 0 to index 6 with step 2
print("slicing the tuple from index 0 to index 6 with step 2: ", tuple[0:7:2])
# slicing the tuple from index -1 to index -6 with step -1 which reverses the tuple from index -1 to index -6
print("slicing the tuple from index -1 to index -6 with step -1: ", tuple[-1:-7:-1])
