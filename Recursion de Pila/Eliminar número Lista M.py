def delete (L,num):
    if isinstance (L,list) and (num,int):
        return delete_aux(L,num)
    else:
        return 'Ingrese valores válidos, ejemplo: "delete([1,2,3],3)"'

def delete_aux(L,num):
    if L==[]:
        return []
    elif isinstance (L[0],list):
        return  delete_aux (L[0],num) + delete_aux (L[1:],num)
    elif L [0]==num:
        return delete(L[1:],num)
    else:
        return [L[0]]+delete_aux(L[1:],num)
    
