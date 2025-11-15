# List

# list uses square brackets []
# lists can store multiple data types in a single list
# lists are mutable (can be changed after creation)

# creating a list with different data types
values = [1,2,2.5,"Raviprasad",True,3+4j]
print("values in the List are: ",values)

# accessing elements in the list using index
# accessing first and last element
print("First element in the List Value is: ", values[0])
# accessing last element using negative index
print("last element in the list Value is:", values[-1])
# while accessing a range of elements, the start index is inclusive and end index is exclusive
print("values of the elements 2nd to 4th are: ", values[1:4])

# insert an element in the list at a specific index
values.insert(4,"Chowdhary")
print("List after adding an element in between the list: ", values)

# append an element at the end of the list
values.append("The End")
print("List after appending an element at the end: ", values)

# replace an element at a specific index
print("List before replacing the 4th element: ", values)
values[3] = "Rohan"
print("List after replacing the 4th element: ", values)

# delete an elelment from the list
print("List before deleting the 2nd element: ", values)
del values[1]
print("List after deleting the 2nd element: ", values)