def MaxMin(L):
    if isinstance (L,list):
        return Min_aux(L,0,-1,(len(L))-1,0),Max_aux(L,0,-1,(len(L))-1,0)
    else: return "Error"
def Min_aux (L,I,I2,La,R):
    if I==La or I2==-(La):
        return R
    elif L[I]<L[I2]:
        return Min_aux(L,I,I2-1,La,L[I])
    else:
        return Min_aux(L,I+1,I2,La,L[I2])
def Max_aux (L,I,I2,La,R):
    if I==La or I2==-(La):
        return R
    elif L[I]>L[I2]:
        return Max_aux(L,I,I2-1,La,L[I])
    else:
        return Max_aux(L,I+1,I2,La,L[I2])
    
