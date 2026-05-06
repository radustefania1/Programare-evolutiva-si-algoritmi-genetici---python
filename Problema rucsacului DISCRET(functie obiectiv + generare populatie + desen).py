import numpy as np
import matplotlib.pyplot as grafic
import random

def functie_obiectiv_rucsac_D(x,v,c,max):
    cost=np.dot(x,c)
    return cost<=max

def generare_populatie(fc,fv,max,dim):
    c=np.genfromtxt(fc)
    v=np.genfromtxt(fv)

    n=v.size
    populatie=[]

    for i in range(dim):
        x=[random.choice([0,1]) for _ in range(n)]
        while not functie_obiectiv_rucsac_D(x,v,c,max):
            x=[random.choice([0,1]) for _ in range(n)]
        val = np.dot(x, v)
        x.append(val)
        populatie.append(x)
    return populatie

def deseneaza(populatie,dim,n):
    x=[i for i in range(dim)]
    y=[populatie[i][n] for i in range(dim)]

    grafic.plot(x,y,"gs",markersize=10)
    grafic.show()

if __name__=="__main__":
    p=generare_populatie("cost.txt","valoare.txt",50,10)
    for element in p:
        print("Individ: ", element[:-1])
        print("calitate: ", element[-1])
    print(p)
    deseneaza(p,10,len(p[0])-1)
