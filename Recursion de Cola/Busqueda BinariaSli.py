def BusquedaBinariaS (N,L):
    if isinstance (N,int) and isinstance (L,list):
        return BB_aux (N,L,(len(L)-1)//2)
    else: return "Error"
def BB_aux (N,L,M):
    if L==[]:
        return False
    elif L[M]<N:
        return BusquedaBinariaS(N,L[(M+1):])
    elif L[M]==N:
        return True
    else:
        return BusquedaBinariaS(N,L[:M])
