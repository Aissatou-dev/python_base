liste= [1, 4, 9, 8, 4, 23 ,2, 4, 1]
for i in liste:
    if(liste.count(i)>1):
        liste.remove(i)
print(liste)
