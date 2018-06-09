#Tarea de intro
#7/3/18
def E(num):
    if isinstance (num,int) and (num>0):
        return E_aux (abs(num))
    else:
        return "Error"
def E_aux(num):
    if num==0:
        return 0
    else:
        return num + E_aux(num-1)
        
    
