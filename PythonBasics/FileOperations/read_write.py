# Read Write operations in Python

file = open('test.txt') # Opens the file in read mode by default

# read all content
content = file.read()
print(f"All content of file:\n{content}\n")
# move the cursor to the beginning of the file
file.seek(0)

# read n number of characters
n=3
content_n = file.read(n)
print(f"First {n} characters of file are: \n{content_n}\n") # print first 3 characters, new line is also counted
# move the cursor to the beginning of the file
file.seek(0)

# read line by line
line1 = file.readline()
print(f"First line of the file is:\n{line1}\n")
line2 = file.readline()
print(f"Second line of the file is:\n{line2}\n")
line3 = file.readline()
print(f"Third line of the file is:\n{line3}\n")

# move the cursor to the third line
file.seek(len(line1)+1 + len(line2)+1) # +1 for newline character
line3_again = file.readline()
print(f"Third line of the file again is:\n{line3_again}\n")
# move the cursor to the beginning of the file
file.seek(0)

# read all lines into a list
lines = file.readlines()
print(f"All lines in the file are:\n")
for i in lines:
    print(f"{i}")
# move the cursor to the beginning of the file
file.seek(0)

# read all lines in the file using a loop
print(f"\nReading file line by line using a loop:\n")
line = file.readline()
while line != "":
    print(f"{line}")
    line=file.readline()

file.close()  # Closes the file