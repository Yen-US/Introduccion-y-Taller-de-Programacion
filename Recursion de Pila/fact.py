def fact (num):
    if isinstance (num,int) and (num>0):
        return fact_aux (abs(num))
    else:
        return "Error"
def fact_aux(num):
    if num==0:
        return 1
    else:
        return num*fact_aux(num-1)
        
