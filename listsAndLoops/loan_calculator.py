montant_total = 50000
taux_annuel = 3
payment_mensuel = 1000
nombre_mois = 60

# taux mentuel
taux_mentuel = taux_annuel/12/100

totaly_payed = False
for i in range(nombre_mois):
    # calcul des interets mentuels
    interets_mentuel = montant_total * taux_mentuel

    montant_total = montant_total + interets_mentuel
    print("Vous payez {:.2f}".format(payment_mensuel), "le mois numero", i+1, "dont {:.2f}%".format(interets_mentuel), "d'interets")
    if totaly_payed:
        print("Vous avez termine vos paiements")
        break

    if montant_total > payment_mensuel:
        montant_total = montant_total - payment_mensuel
        print("Le reste serait de {:.2f}".format(montant_total))
        if payment_mensuel > montant_total:
            payment_mensuel = montant_total
            totaly_payed = True


#prochaine intruction apres le break
print("Fin du programme")