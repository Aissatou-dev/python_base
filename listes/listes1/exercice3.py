list = [int(x) for x in input("donnez la liste ").split(',')]
max=list[0]
for i in range(len(list)):
    if(list[i]>max):
        max= list[i]
print(max)
