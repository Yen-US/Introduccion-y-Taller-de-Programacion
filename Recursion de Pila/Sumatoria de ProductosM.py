#7/3/18
def sumaprod (n):
    if isinstance (n,int)and n>0:
        return sumatoria_aux (n)
    else:
        return "Error"
    
def sumatoria_aux (n):
    if n==0:
        return 0
    else:
        return producto (n) + sumatoria_aux (n-1)
    
def producto (n):
    if n ==0:
        return 1
    else:
        return (3*n**2-n)* producto(n-1)
    
