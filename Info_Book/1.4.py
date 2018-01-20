#################################################################################
#   Programme permettant de calculer le prix TTC d'un article en ne sachant que #
#   son prix HT                                                                 #
#   Auteur : Raphaël                                                            #
#   Changement :                                                                #
#   -Ajout de la possibilité de choisir le taux de TVA                          #
#################################################################################

print("Quel est le prix hors taxes ?")
ht = float(input())
print("quel est le taux de TVA ?")
tva = float(input())
ttc = ht + (ht * tva / 100.0)
print("Le prix TTC est :", end="")
print(ttc)
