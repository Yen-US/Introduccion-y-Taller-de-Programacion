#Martes
def largo (num):
    if isinstance (num,int) and (num>0):
        return largo_aux (abs(num))
    else:
        return "Error"
def largo_aux (num):
    if num == 0:
        return 0
    elif num >0:
        return 1+largo_aux(num//10)
        
