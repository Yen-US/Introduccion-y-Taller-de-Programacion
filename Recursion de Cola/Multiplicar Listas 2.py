def ML (L):
    if isinstance (L,list):
        return ML_aux (L,1)
    else: return "Error"
def ML_aux (L,R):
    if L==[]:
        return R
    elif isinstance (L[0],list):
        return ML_aux (L[0],R)* ML_aux (L[1:],R)
    else:
        return ML_aux (L[1:], L[0]*R)
