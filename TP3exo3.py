import random
n = random.randint(0,100)
temps = 10
mot = "?"
while temps > 0:
    var = input("Entrez un nombre")
    var = int(var)
    if var >= n:
        mot = "trop haut"
        print(temps, mot)
    else :
        mot = "trop bas"
        print(temps, mot)
    if var == n:
        mot = "bravo !"
        print(mot)
        break
