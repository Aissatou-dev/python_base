def union_intersection(liste1, liste2):
    union = list(set(liste1) | set(liste2))
    intersection = list(set(liste1) & set(liste2))
    return union, intersection

L1 = [1, 2, 3, 4]
L2 = [3, 4, 5, 6]

u, i = union_intersection(L1, L2)

print("Union :", u)
print("Intersection :", i)