#Sumatoria de raices cuadradas
import math
def SQRT (L):
    if isinstance (L,list):
        return SQRT_aux(L)
    else:
        return 'Inserte una lista, ejemplo: "[1,2,3]"'
def SQRT_aux (L):
    if  L==[]:
        return 0
    else: 
        return math.sqrt (L[0])+SQRT_aux (L[1:])
