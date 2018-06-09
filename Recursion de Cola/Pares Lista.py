def PL(L):
    if isinstance (L,list):
        return PL_aux (L,[],0,len (L))
    else:
        return "Error"
def PL_aux (L,R,I,F):
    if I==F:
        return R
    elif isinstance (L[I],list):
        return PL_aux (L[I],[],0,len (L[I]))+ PL_aux(L,R,I+1,F)
    elif L[I]%2==0:
        return PL_aux (L,[L[I]]+R,I+1,F)
    else:
        return PL_aux (L,R,I+1,F)
