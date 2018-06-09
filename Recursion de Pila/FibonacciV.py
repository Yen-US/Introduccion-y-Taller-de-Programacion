#Miercoles
def fibo (num):
    if isinstance (num,int) and (num>0):
        return fibo_aux (abs(num))
    else:
        return "Error"
def fibo_aux(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return fibo_aux (num-1)+fibo_aux(num-2)
