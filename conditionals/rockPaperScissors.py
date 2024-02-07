import random

joueur_1 = input("Choisissez pierre, feuille ou sciseaux?\n")
seq = ["pierre", "feuille", "sciseaux"]
computer = random.choice(seq)
print("Computer choice est", computer)

if joueur_1 != "pierre" and joueur_1 != "feuille" and joueur_1 != "sciseaux":
    print("Vous devez choisir pierre, feuille ou sciseaux")
elif joueur_1 == "pierre" and computer == "sciseaux":
    print("GAGNE")
elif joueur_1 == "sciseaux" and computer == "feuille":
    print("GAGNE")
elif joueur_1 == "feuille" and computer == "pierre":
    print("GAGNE")
elif joueur_1 == computer:
    print("EGALITE")
else:
    print("PERDU")
