def EL3 (N):
    if isinstance (N,int):
        return EL3_aux (N,0,0)
    else: return "Por Favor Ingrese un Número Válido"
def EL3_aux (N,L,R):
    if N==0:
        return R
    elif not (N%10)%3==0 or N%10==0:
        return EL3_aux (N//10,L+1,(R+((N%10)*10**L)))
    else:
        return EL3_aux (N//10,L,R)
    
