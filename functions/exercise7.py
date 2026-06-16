def compter_lettres(chaine):
    majuscules = 0
    minuscules = 0

    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1
        elif caractere.islower():
            minuscules += 1

    print("Nombre de caractères majuscules :", majuscules)
    print("Nombre de caractères minuscules :", minuscules)

compter_lettres("The quick Brow Fox")