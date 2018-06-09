def MultiL (L):
    if isinstance (L,list):
        return MultiL_aux (L,1)
    else: return "Por Favor ingrese un Lista"
def MultiL_aux (L,R):
    if isinstance (L[0],list):
        return MultiL_aux (L[0],R)
    elif L==[]:
        return R
    else:
        return MultiL_aux (L[1:],R*L[0])

