depenses = []
# afficher le total des mes dépenses

nombre_depenses = int(input("Combien de dépenses souhaitez vous saisir?\n"));

for i in range(nombre_depenses):
    depenses.append(int(input("Saisissez une dépense\n")));

print("Total des dépenses ", sum(depenses), "€", sep='')