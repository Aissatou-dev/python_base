from itertools import permutations

def toutes_permutations(liste):
    return list(permutations(liste))

print(toutes_permutations([1, 2, 3]))