def k_plus_grand(liste, k):
    liste_triee = sorted(liste, reverse=True)
    return liste_triee[k-1]

L = [7, 2, 9, 1, 5]
print(k_plus_grand(L, 2))