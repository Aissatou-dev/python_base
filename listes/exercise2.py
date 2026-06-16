def longueur_croissante(liste):
    if len(liste) == 0:
        return 0

    max_longueur = 1
    longueur = 1

    for i in range(1, len(liste)):
        if liste[i] > liste[i-1]:
            longueur += 1
        else:
            longueur = 1

        if longueur > max_longueur:
            max_longueur = longueur

    return max_longueur

print(longueur_croissante([1, 2, 3, 1, 2, 3, 4]))