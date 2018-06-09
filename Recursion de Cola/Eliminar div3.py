def E3 (N):
    if isinstance (N,int):
        return E3_aux (N,0,0)
    else: return "Error"

def E3_aux (N,R,E):
    if N==0:
        return R
    elif (N%10)%3==0 and (N%10)!=0:
        return E3_aux (N//10,R,E)
    else:
        return E3_aux (N//10,((N%10)*(10**E))+R,E+1)
    
