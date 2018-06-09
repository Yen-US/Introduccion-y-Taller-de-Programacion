#Intro 16/3/18
#Tarea 3
def MinMax (L):
    if isinstance (L,list):
        return Min_aux(L)#, Max_aux (L)
    else:
        return 'Inserte una lista, ejemplo: "[1,2,3]"'
def Min_aux (L):
    if L==[L[0]]:
        #len (L)==1 *longitud*
        return L[0]
    elif L[0]<=L[1]:
        return Min_aux ([L[0]]+L[2:])
    else:
        return Min_aux (L[1:])
#def Max_aux (L):
    if L==[L[0]]:
        #len (L)==1 *longitud*
        return L[0]
    elif L[0]>=L[1]:
        return Max_aux ([L[0]]+L[2:])
    else:
        return Max_aux (L[1:])
