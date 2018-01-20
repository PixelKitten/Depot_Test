#################################################################################
#   Programme de mini bataille navale                                           #
#   Auteur : Raphaël                                                            #
#   Modifications :                                                             #
#   -Changement du premier print "A vous de jouer" vers "A toi de jouer"        #
#   -Changement des valeurs de a et b. anciennes valeurs : a=4,b=7              #
#   -Changement du else : if : en elif                                          #
#   -Prise en compte des cases voisines du bateau pour le "En vue" Exo 1.5      #
#################################################################################

a = 6
b = 9
print("A toi de jouer !")
print("Entrez x :")
x = int(input())
print("entrez y :")
y = int(input())
if x == a and y == b:
    print("Coulé !")
elif (x == a) or (x == a-1) or (x == a+1) or (y == b) or (y == b-1) or (y == b+1):
    print("En vue")
else:
    print("A l'eau !")
