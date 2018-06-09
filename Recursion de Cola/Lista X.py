def ListaX (L):
    if isinstance (L,list) and L!=[]:
        return ListaX_aux (L,0,len (L),1)
    else:return "Error"
def ListaX_aux (L, ind, La, res):
    if ind==La:
        return res
    else:
        return ListaX_aux (L, ind+1, La, res * L[ind])
