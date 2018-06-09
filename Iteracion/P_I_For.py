def pares_impares (lista):
	if isinstance (lista,list) and lista!=[]:
		return pares_impares_aux (lista)
		
def pares_impares_aux (lista):
	listaPares =[]
	listaImpares=[]
	for valor in lista:
		if (valor%2==0): 
			listaPares+=[valor]
		else: 
			listaImpares+=[valor]
	return listaPares, listaImpares
	
