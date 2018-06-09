#9/3/18
def clasificar_numero (num):
    if isinstance (num,int):
        return clasificar_numero_0y1 (abs(num))
    else:
        return "Error"
    
def clasificar_numero_0y1 (num):
    if num==1 or num==0:
        return "Número Especial"
    else:
        return clasificar_numero_primo(num,num-1)
    
def clasificar_numero_primo(numero,divisor):
    if divisor==1:
        return "Número Primo"
    elif numero % divisor ==0:
        return "Número Compuesto" 
    else:
        return clasificar_numero_primo(numero,divisor-1)
