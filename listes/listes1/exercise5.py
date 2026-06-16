liste= input("donner les elements de la liste ").split(',')
nbr=0
for i in liste:
    if (len(i)>=2 and i[0]==i[-1]):
        nbr +=1
print(nbr)
