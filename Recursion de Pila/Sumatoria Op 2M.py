#7/3/18
def s1(num):
    if isinstance (num,int) and (num>0):
        return s1_aux (abs(num))
    else:
        return "Error"
def s1_aux (num):
    if num ==0:
        return 0
    else:
        return (num+5*(num*num)**2) + s1_aux(num-1)
