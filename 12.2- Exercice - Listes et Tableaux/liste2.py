# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]
pos = [0, 0]
for i in range(0, len(tab)):
    for j in range(0, len(tab[i])):
        if tab[i][j] > tab[pos[0]][pos[1]]:
            pos[0] = i
            pos[1] = j

print("La valeur maximum est : " + str(tab[pos[0]][pos[1]]) + " et elle se trouve à l'indice [ " + str(pos[0]) + " ][ " + str(pos[1]) + " ]")
