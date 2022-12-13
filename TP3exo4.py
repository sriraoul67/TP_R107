n=int(input("Entrez un nombre"))
a="for"
b="while"
y=str(input("quelle boucle voulez vous for ou while"))
r=1
if y==a:
    for i in range (n):
        i=i+1
        r=r*i
        print(r)
elif y==b:
    i=1
    while i<= n:
        r = r * i
        i = i + 1


        print(r)