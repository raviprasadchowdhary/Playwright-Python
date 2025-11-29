with open('test2.txt') as file:
    content = file.read()
    print(f"File content:\n{content}")

# read the file
# reverse the lines
# write the reversed lines to the same file
with open('test2.txt', 'r') as reader:
    lines = reader.readlines()
    reversed(lines)
    with open('test2.txt', 'w') as writer:
        for i in reversed(lines):
            writer.write(i)

with open('test2.txt') as file:
    content = file.read()
    print(f"Reversed file content:\n{content}")