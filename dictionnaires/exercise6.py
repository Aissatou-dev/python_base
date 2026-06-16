n = int(input("Donner une valeur: "))
dict1= dict()
for i in range(1, n + 1):
    dict1.update({i: i*i})

print(dict1)