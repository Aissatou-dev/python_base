temp= float(input("Entrez la temperatuure : "));
choice = input("Entrez C pour Celsius, F pour Fahrenheit) : ");
if choice.lower() == "c":
  temp_f= (temp-32)*5/9;
  print(f"{temp}°c est égal à {temp_f}°f");
elif choice.lower() == "f":
  temp_c= (temp*9/5)+32;
  print(f"{temp}°f est égal à {temp_c}°c");
else:
  print("Choix invalide. Veuillez entrer C  F .");