def pares (num):
    if isinstance (num,int) and (num>0):
        return pares_aux (abs(num)),impares_aux(abs(num))
    else:
        return "Error"
def pares_aux(num):
    if (num==0):
        return 0
    elif((num%10)%2)==0:
        return 1+pares_aux(num//10)
    else:
        return pares_aux(num//10)

def impares_aux(num):
    if (num==0):
        return 0
    elif((num%10)%2)==0:
        return impares_aux(num//10)
    else:
        return 1+impares_aux(num//10)

