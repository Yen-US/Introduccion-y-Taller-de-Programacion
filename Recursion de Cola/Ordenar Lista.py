def Ordenar (L):
    if isinstance (L,list):
        return Ord (L,0,0)
    else:
        return "Error"
def Ord (L,I1,I2):
    if I1==len(L)-1:
        return L
    elif I2==len(L)-1:
        return Ord (L,I1+1,0)
    elif L[I2]>L[I2+1]:
        aux=L[I2]
        L[I2]=L[I2+1]
        L[I2+1]=aux
        #L[I2],L[I2+1]=L[I2+1], L[I1]
        return Ord (L,I1,I2+1)
    else:
        return Ord (L,I1,I2+1)
