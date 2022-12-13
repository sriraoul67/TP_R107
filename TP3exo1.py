from time import sleep

N=int(input("entrez une valeur"))

for i in range(N+1):
    sleep(0.2)
    print(N)
    N=N-1

