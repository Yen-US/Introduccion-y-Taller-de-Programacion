#7/3/18
def s3(num):
    if isinstance (num,int) and (num>0):
        return s3_aux (abs(num))
    else:
        return "Error"
def s3_aux (num):
    if num ==0:
        return 0
    else:
        return (num*num**3) + s3_aux(num-1)
    
