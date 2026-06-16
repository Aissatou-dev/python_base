def produit_liste(liste):
    produit = 1

    for nombre in liste:
        produit *= nombre

    return produit

print(produit_liste([8, 2, 3, -1, 7]))