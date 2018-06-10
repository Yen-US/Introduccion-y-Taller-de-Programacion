def contarConsonantes (Palabra):
    if isinstance (Palabra,str):
        return contarConsonantes_aux (Palabra)
    else: return "Error"
def contarConsonantes_aux (Palabra):
    if Palabra == "":
        return 0
    elif Palabra [0]== "a" or Palabra [0] == "e" or Palabra [0]== "i" or Palabra[0] == "o" or Palabra [0]=="u":
        return contarConsonantes_aux (Palabra [1:])
    else:
        return 1 + contarConsonantes_aux (Palabra[1:])
