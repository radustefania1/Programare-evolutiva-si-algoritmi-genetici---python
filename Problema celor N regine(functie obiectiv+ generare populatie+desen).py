import numpy as np
import matplotlib.pyplot as grafic
import random

def functie_obiectiv_N_Regine(x):
    n=x.size
    c=n*(n-1)/2
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(i-j)==abs(x[i]-x[j]):
                c=c-1
    return c

def generare_populatie(n,dim):
    population=np.zeros((dim,n+1), dtype=int)
    for i in range(dim):
        population[i,:n]=np.random.permutation(n)
        population[i][n]=functie_obiectiv_N_Regine(population[i,:n])
    return population

def deseneaza(population, n, dim):
    x = [i for i in range(dim)]
    y = [population[i][n] for i in range(dim)]
    grafic.plot(x, y, "gs", markersize = 10)

    #grafic.xticks(range(dim))
    #grafic.yticks(range(min(y),max(y)+1))
    grafic.show()


if __name__=="__main__":
    p=generare_populatie(4,6)
    print(p)