# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# it is similar to a real-life dictionary where you have a word (key) and its meaning (value).
# in java, it is similar to HashMap.

# Creating a dictionary
dictionary = {
    "givenName": "Raviprasad"
    , "surname": "Chowdhary"
    , "age": 25
    , "isStudent": True
    , "heigh": 172.5
    , "hobbies": ["coding", "reading", "gaming"]
    , "address": {
        "street": "123 Main St"
        , "city": "Bangalore"
        , "state": "Karnataka"
        , "zip": "560001"
    }
    , "favoriteComplexNumber": 3 + 4j
    , "favoritwQuotes": ("Stop holding back, go for it", "Fear is just a state of mind", "Fear nobody but yourself")
    , "nullValue": None
    , 1: "This is a key with integer type"
    , (2,3): "This is a key with tuple type"
    , True: "This is a key with boolean type"
    , 3.14: "This is a key with float type"
    , 3 + 4j: "This is a key with complex number type"
    , None: "This is a key with None type"
    , "duplicateKey": "First Value"
    , "duplicateKey": "Second Value"  # This will overwrite the first value
    , "listAsKey": [1,2,3]  # This will raise a TypeError as lists are unhashable
    # , "dictAsKey": {"key": "value"}  # This will raise a TypeError as dictionaries are unhashable
    , frozenset([1,2,3]): "This is a key with frozenset type"  # frozenset is hashable
    , b'byteKey': "This is a key with bytes type"  # bytes is hashable
    # , bytearray(b'byteArrayKey'): "This is a key with bytearray type"  # bytearray is unhashable
    , range(5): "This is a key with range type"  # range is hashable
    , complex(1,2): "This is a key with complex type"
    , "setAsKey": {1,2,3}  # This will raise a TypeError as sets are unhashable
    , "frozenSetAsKey": frozenset([4,5,6])  # frozenset is hashable
    , "tupleAsKey": (4,5,6)  # tuple is hashable
}

# accessing elements of a dictionary
# accessing elements using keys
print("The given name is: ", dictionary["givenName"])
print("The surname is: ", dictionary["surname"])

# accessing nested dictionary
print("The city is: ", dictionary["address"]["city"])

# accessing elements using get() method
print("The age is: ", dictionary.get("age"))
print("Is student: ", dictionary.get("isStudent"))

# accessing a key that does not exist using get() method
print("The country is: ", dictionary.get("country", "Not Found XX"))

# accessing a key that does not exist using indexing method will raise a KeyError
# print("The country is: ", dictionary["country"])  # Uncommenting this line will raise a KeyError

# accessing nested elements with get() method
print("The street address is: ", dictionary.get("address").get("street"))

# accessing elements using keys of different data types
print("The integer key value is: ", dictionary[1])
print("The tuple key value is: ", dictionary[(2,3)])
print("The boolean key value is: ", dictionary[True])
print("The float key value is: ", dictionary[3.14])
print("The complex number key value is: ", dictionary[3 + 4j])
print("The None key value is: ", dictionary[None])
print("The frozenset key value is: ", dictionary[frozenset([1,2,3])])
print("The bytes key value is: ", dictionary[b'byteKey'])
print("The range key value is: ", dictionary[range(5)])
print("The complex key value is: ", dictionary[complex(1,2)])
print("The frozenSetAsKey value is: ", dictionary["frozenSetAsKey"])
print("The tupleAsKey value is: ", dictionary["tupleAsKey"])
# print("The listAsKey value is: ", dictionary[ [1,2,3] ])  # Uncommenting this line will raise a TypeError
# print("The dictAsKey value is: ", dictionary[ {"key": "value"} ])  # Uncommenting this line will raise a TypeError
# print("The bytearray key value is: ", dictionary[ bytearray(b'byteArrayKey') ])  # Uncommenting this line will raise a TypeError
# print("The setAsKey value is: ", dictionary["setAsKey"])  # Uncommenting this line will raise a TypeError
