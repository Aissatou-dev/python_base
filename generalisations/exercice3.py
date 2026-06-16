#deviner le nombre secret, un jeu de devinette
import random
nb_secret = random.randint(1, 9)

print("Devinez un nombre entre 1 et 9")
devine = int(input("Votre choix : "))

while devine != nb_secret:
    if devine < nb_secret:
        print('le nombre est plus grand ');
    else:
        print('le nombre est plus petit');
    devine = int(input("reesayez: "))
print("Bien deviné ! le nombre secret etait ", nb_secret)
              
       