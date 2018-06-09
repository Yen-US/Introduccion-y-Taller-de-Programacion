# tarea de intro solo pares
def sumalista (L):
    if isinstance (L,list):
        return sumalistap_aux (L), sumalistai_aux (L)
    else:
        return "Error, el valor ingresado no es una lista"
def sumalistap_aux (L):
    if L == []:
        return 0
    elif L[0] % 2 ==0:
        return L[0]+sumalistap_aux (L[1:])
    else:
        return sumalistap_aux (L[1:])
def sumalistai_aux (L):
    if L == []:
        return 0
    elif L[0] % 2 ==0:
        return sumalistai_aux (L[1:])
    else:
        return L[0]+sumalistai_aux (L[1:])
    
    


    
