# 1.	Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines.
# 2.	Open the Names.txt file and display the data in Python.
# 3.	Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file.


def create_file():
    try:
        with open(fileName, "w") as file:
            file.write("Dan\n")
            file.write("Lisa\n")
            file.write("Adam\n")
            file.write("Sarah\n")
            file.write("Joe\n")
    except OSError as e:
        print("Error when creating file", e)

def read_file():
    try:
        with open(fileName) as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print("File not found", e)

def write_to_file(name):
    try:
        with open(fileName, "a") as file:
            file.write(f"{name}\n")
    except OSError as e:
        print("Error when updating file", e)


def main():
    print("Creating file...")
    create_file()

    print("Printing file...")
    read_file()

    name = input("Please enter a name\n")
    write_to_file(name)
    print("Printing file...")
    read_file()


fileName = "Names.txt"
main()