def MinMaxS (L):
    if isinstance (L,list):
        print ("El menor de la lista es:",MinS_aux (L,0))
        print ("El mayor de la lista es:",MaxS_aux (L,0))
    else:
        return "Por favor ingrese un lista valida"
def MinS_aux (L,R):
    if len (L)==1:
        return R
    elif L[0]<L[1]:
        return MinS_aux ([L[0]]+L[2:],L[0])
    else:
        return MinS_aux (L[1:],L[1])
def MaxS_aux (L,R):
    if len (L)==1:
        return R
    elif L[0]>L[1]:
        return MaxS_aux ([L[0]]+L[2:],L[0])
    else:
        return MaxS_aux (L[1:],L[1])

        
