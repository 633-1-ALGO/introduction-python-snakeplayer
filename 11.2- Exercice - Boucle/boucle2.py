# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]
sizeB = len(B)

print(B)

i = 0
while i < sizeB:
    flag = False
    nb = B[i]
    for j in range(i + 1, sizeB):
        if not flag:
            if nb >= B[j]:
                B[i] = B[j]
                B[j] = nb
                flag = True
    i = i + 1

print(B)
