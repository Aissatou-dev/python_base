dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# resultat={}
# resultat.update(dic1)
# resultat.update(dic2)
# resultat.update(dic3)
# print(resultat)

#resultat = {**dic1,**dic2,**dic3}

resultat = dic1|dic2|dic3 #la sortie de dic1 et l'entree de dic2 et la sortie de dic2 et l'entre de dic3 ce qui equivaut a des update successive
print(resultat)