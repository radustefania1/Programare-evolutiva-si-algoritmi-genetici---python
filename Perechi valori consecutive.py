#Scrieți o funcție Python care generează o matrice (populație) cu 18 linii vectori cu 6 elemente: 5 biți reprezentând
# un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui individ este dată de numărul perechilor
# de valori consecutive diferite (de exemplu, calitatea lui [1,0,0,1,1] = 2). Calculați și afișați indivizii  cu cea mai
# mare valoare a funcției calitate.

import numpy as np
import matplotlib.pyplot as grafic
import random

def functie_obiectiv_p2(x):
    n=len(x)
    s=0
    for i in range(n-1):
        if x[i]!=x[i+1]:
            s=s+1
    return s

def generare_populatie(dim, n):
    population=[]
    for i in range(dim):
        x=[random.choice([0,1]) for _ in range(n)]
        calitate=functie_obiectiv_p2(x)
        x.append(calitate)
        population.append(x)
    return population

def deseneaza(population,dim,n):
    x=[i for i in range(dim)]
    y=[population[i][n] for i in range(dim)]

    grafic.plot(x,y,"gs",markersize=10)
    grafic.show()

if __name__=="__main__":
    p=generare_populatie(18,6)
    for element in p:
        print("Individ: ", element[:-1])
        print("calitate: ", element[-1])
    deseneaza(p,18,6)


