def Mayores (N,L):
    if isinstance (N,int) and N>0 and (L,list):
        return Mayores_aux(N,L)
    else:
        return "Por Favor ingrese un número y una lista validos"
def Mayores_aux (N,L):
    if L==[]:
        return 0
    elif N<L[0]:
        return 1 + Mayores_aux (N,L[1:])
    else:
        return Mayores_aux (N,L[1:])
                                                
    
