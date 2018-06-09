def BusquedaLinealS (N,L):
    if L!=[] and N!=[]:
        return BL_aux (N,L)
    else: return "Por Favor ingrese valores validos"
def BL_aux (N,L):
    if L==[] or L=="":
        return False
    elif L[0]==N:
        return True
    else: return BL_aux (N,L[1:])
