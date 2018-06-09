def BusquedaLineal (N,L):
    if L!=[] and N!=[]:
        return BL_aux (N,L,0,len(L))
    else: return "Por Favor ingrese valores validos"
def BL_aux (N,L,I,La):
    if I==La:
        return False
    elif L[I]==N:
        return True
    else: return BL_aux (N,L,I+1,La)
