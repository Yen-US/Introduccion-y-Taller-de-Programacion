#Quiz
def Pot_dos (num):
    if isinstance (num,int) and (num>0 or num==0):
        return Pot_dos_aux (abs(num))
    else:
        return "Error"
def Pot_dos_aux (num):
    if num==0:
        return 1
    else:
        print (2**num,end =" ")
        return Pot_dos_aux (num-1)
