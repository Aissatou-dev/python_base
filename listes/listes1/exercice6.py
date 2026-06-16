liste =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in liste:
    triee= sorted(liste, x=lambda a: a[-1])
print(triee)
