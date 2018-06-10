def palindromo (Numero):
    if isinstance (Numero,int) and Numero>0:
        return palindromo_aux(Numero, VueltaNumero(Numero,(LargoNum(Numero))-1))
    else:
        return "Error"
def LargoNum (Numero):
    if Numero ==0:
        return 0
    else:
        return 1 + LargoNum (Numero//10)
def VueltaNumero (Numero,Largo):
    if Numero == 0:
        return 0
    else:
        return  ((Numero %10)*(10**Largo))+VueltaNumero (Numero//10, Largo-1)
def palindromo_aux (Numero,NumeroInv):
    if Numero == NumeroInv:
        return True
    else: return False

