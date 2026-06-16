dict1 =  {0 : 10, 1 : 20, 2 :3, 3 : 5, 4 : 15}
liste = list()
for i in dict1.items():
   liste.append(i) 
   liste.sort(key=lambda a: a[1])
print(liste)