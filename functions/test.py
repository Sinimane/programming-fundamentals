
print("Lecture version 1")
with open("test.txt") as file:
    result = file.readlines()
    for line in result:
        print(line)

print("Lecture version 2")
with open("test.txt") as file:
    for line in file:
        print(line)