#Martes
def Suma_Digitos (num):
    if isinstance (num,int) and (num>0):
        return Suma_Digitos_aux (abs(num))
    else:
        return "Error"
def Suma_Digitos_aux (num):
    if num==0:
        return 0
    elif num>0:
        return num%10 + Suma_Digitos_aux (num//10)
    
