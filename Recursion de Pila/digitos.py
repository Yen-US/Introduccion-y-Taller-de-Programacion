def Ap1234 (num):
    if isinstance (num,int) and (num>0):
        return Ap1234_aux (abs(num))
    else:
        return 'Error'
def Ap1234_aux (num):
    if (num==0):
        return True
    elif ((num%10)>=0) and ((num%10)<=4):
        return Ap1234_aux (num//10)
    else:
        return False 
    

    
