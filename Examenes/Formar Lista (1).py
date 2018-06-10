def formarLista (Numero):
    if isinstance (Numero,int) and Numero>0:
        return formarLista_aux (Numero)
    else:
        return "Error"
def formarLista_aux (Numero):
    if Numero== 0:
        return []
    elif (Numero%10)%2 ==0:
        return [Numero%10]+ formarLista_aux (Numero//10)
    else:
        return formarLista_aux (Numero//10)
