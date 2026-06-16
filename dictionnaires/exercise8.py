dictionaire1={0:30,1:70, 2:20}
dictionaire2= {3:50,4:10, 5:290}
# resultat={}
# resultat.update(dictionaire2)
# resultat.update(dictionaire1)
resultat=dictionaire1|dictionaire2
print(resultat)

