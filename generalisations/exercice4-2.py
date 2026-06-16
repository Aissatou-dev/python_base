# for i in range(1,6):
#     for j in range(1, i+1):
#         print('*', end='')
#     print()
# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end='')
#     print() 
vert = "\033[32m"
jaune = "\033[33m"
rouge = "\033[31m"
couleurParDef = "\033[0m"

for i in range(5):
    for j in range(30):

        if j < 10:
            print(vert + "*", end="")

        elif j < 20:
            if i == 2 and j in [15] :

                print(vert + "*", end="")
            else:
                print(jaune + "*", end="")

        else:
            print(rouge + "*", end="")

    print(couleurParDef)