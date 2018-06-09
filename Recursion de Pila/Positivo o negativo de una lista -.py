def N_PN (L):
    if isinstance (L,list):
        return N_PN_aux (L)
    else:
        return "Lo anterior no corresponde a una lista"
def N_PN_aux (L):
    if L==[]:
        return "Negativos"
    elif L[0]>0:
        return "Positivos"
    else:
        return N_PN_aux (L[1:])
    
    
 
