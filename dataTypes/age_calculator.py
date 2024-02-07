age = int(input("Quel age avez vous?\n"))
decenies = age // 10
annees = age % 10
print("Votre age est de " + str(age) + " ans dont " + str(decenies) + " décénies et "+ str(annees) + " années")
print("Votre age est de", age, "ans dont", decenies, "décénies et", annees, "années")
print("Votre age est de {} ans dont {} décénies et {} années".format(age, decenies, annees))