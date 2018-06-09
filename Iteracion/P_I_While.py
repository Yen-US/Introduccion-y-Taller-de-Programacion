def pares (num):
	if isinstance (num,int) and num>=0:
		return pares_aux(num)

def pares_aux(num):
	listaPares=[]
	listaImpares=[]
	while num>0:
		digit = num%10
		if (digit%2==0):
			listaPares+=[digit]
		else: listaImpares+=[digit]
		num=num//10
	return listaPares, listaImpares
print (pares(123456789))