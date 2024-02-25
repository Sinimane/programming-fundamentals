# Saisie d'acronyme
# lecture du fichier et recherche
# Repondre a l'utilisateur

def find_acronym(acronym):
    found = False
    try:
        with open(fileName) as file:
            for line in file:
                if acronym in line:
                    print("Acronym found\n", line, sep='')
                    found = True
                    break
            if not found:
                print("Acronym not found")
            return found
    except FileNotFoundError as e:
        print("The file was not found:", e)


def write_in_file(acronym, definition):
    try:
        with open(fileName, "a") as file:
            file.write(f"{acronym} - {definition}\n")
        print(f"{acronym} was added to the file {fileName}")
    except OSError as e:
        print("Error when writing file:", e)
        #print("The error type:", type(e))

def main():
    acronym = input("Please enter an acronym\n")
    found = find_acronym(acronym)
    if not found:
        definition = input("Please enter the acronym definition\n")
        write_in_file(acronym, definition)

fileName = "files/acronyms.txt"
main()
