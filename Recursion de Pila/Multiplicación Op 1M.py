#7/3/18
def s2(num):
    if isinstance (num,int) and (num>0):
        return s2_aux (abs(num))
    else:
        return "Error"
def s2_aux (num):
    if num ==0:
        return 1
    else:
        return (3*num-2) * s2_aux(num-1)
