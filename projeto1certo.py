from random import seed
from random import random
import numpy as np
import plotly.express as px


seed(1417385655) #seed to be chosen
A1 = np.array([[random(),random()],[0,0]])
A2 = np.array([[random(),random()],[0,0]]) #3 diffusion networks get made from random entires on the first row
A3 = np.array([[random(),random()],[0,0]])
    
for a in range(0,2):
    A1[1][a] = 1 - A1[0][a]
    A2[1][a] = 1 - A2[0][a] #Making sure it's a diffusion matrix (row's sum = 1)
    A3[1][a] = 1 - A3[0][a]
    



def state(k, A):
    """
       Function that updates the system's state and the probability vector 
       (if, for example, the nextstep function returns 1 as an output, the state
       function updates the probability vector with the row of the adjacency matrix
       corresponding to 1)
       
    """
    Ab = A.transpose()
    prbs = Ab[k]
    return prbs
    
def nextstep(vec): #Random walks function
    i = 0
    p = vec[0]
    r = random()
    while r > p:
        i += 1
        p += vec[i]
    return i

h = []
iter = 1000
M = A1
print(M)
print( )
for g in range(0,iter):
    h.append(nextstep(state(1, M))) #The initial conditions of the system and the adjacency matriz get chosen
hl = np.append(h, 1)
print(hl)

print( )
#Frequency of spawn of elements gets calculated here
countzero = 0
countone = 0
for a in range(len(h)):
    if h[a] == 0:
        countzero += 1
    elif h[a] == 1:
        countone += 1
freq10 = countone/countzero

print("A taxa de aparição de elementos 1 em relação a elementos 0 é: " + str(freq10))
        

oper = np.arange(iter)

fig = px.scatter(x = oper, y = h)
fig.show()


input()
