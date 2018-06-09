def potencia (num):
    if isinstance (num,int) and (num==0)or(num>0):
        return potencia_aux(num)
    else:
        return"error"

def potencia_aux (num):
    if num>0:
        print("fin")
    else:
        print (2**num)
        return potencia_aux(num-1)
    
        
