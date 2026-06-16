vert = "\033[32m"
jaune = "\033[33m"
reset ="\033[0m"
paire=0
impaire=0
nombre ={1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in nombre:
    if (i%2==0):
        paire+=1
    else:
        impaire +=1
print(f" {vert}le nombre de valeur paire {paire} \n {jaune} nombre de valeurs impaires {impaire} {reset}")
        

