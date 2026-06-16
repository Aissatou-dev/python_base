def k_plus_petit(liste, k):
    liste_triee = sorted(liste)
    return liste_triee[k-1]
L = [7, 2, 9, 1, 5]
print(k_plus_petit(L, 2))