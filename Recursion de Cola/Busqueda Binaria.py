def BusquedaBinaria (N,L):
    if isinstance (N,int) and isinstance (L,list):
        return BB_aux (N,L,(len(L)-1)//2,2,len(L)-1)
    else: return "Error"
def BB_aux (N,L,I,I2,La):
    if I2>La or I==La:
        return False
    elif L[I]>N:
        return BB_aux (N,L,I//I2,I2+2,La)
    elif L[I]==N:
        return True
    else:
        return BB_aux (N,L,I+(La//I2),I2+2,La)
        
