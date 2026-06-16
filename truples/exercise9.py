mon_tuple = (1, 2, 3, 4, 1, 4, )
compteur = 0
for i in range(len(mon_tuple)):
    if mon_tuple[i] in mon_tuple[i+1:]:
        print(mon_tuple[i])
       
        