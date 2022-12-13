tarif = 0
debut = 0
un = 0
deux = 0

debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

while debut == fin or debut>fin or debut<0 or debut>24 or fin>24 or fin<0:
    if debut==fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    elif debut>fin:
        print("Attention ! le début de la location est après la fin ...\n")
    elif debut<0 or debut>24 or fin>24 or fin<0:
        print("Les heures doivent être comprises entre 0 et 24 ! \n")

    debut = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

for i in range(debut, fin):
    if debut>=0 and debut<7 or debut>=17 and debut<24:
        tarif = tarif+1
        debut = debut+1
        un = un+1
    elif debut>=7 and debut<17:
        tarif = tarif+2
        debut = debut+1
        deux = deux +1


print("Vous avez loué votre vélo pendant")
print(f"{un} heure(s) au tarif horaire de 1.0 euro(s)")
print(f"{deux} heure(s) au tarif horaire de 2.0 euro(s)")
print(f"Le montant total à payer est de {tarif} euro(s).")