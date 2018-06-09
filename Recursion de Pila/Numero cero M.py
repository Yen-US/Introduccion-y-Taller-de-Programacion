# tarea de taller (14/3)
def N0 (L):
    if isinstance (L,list):
        return N0_aux (L)
    else:
        return "Error, lo anterior no corresponde a una lista"
def N0_aux (L):
    if L==[]:
        return False
    elif L[0]==0:
        return True
    else:
        return N0_aux (L[1:])
    
