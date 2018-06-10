class PyOperaciones():
	def __init__(self):
		pass
	def contar (self):
		Numero = int(input("Ingrese Numero: "))
		Numero1 = Numero
		Digitos = 1
		while Numero1>9:
			Numero1 = Numero1 // 10
			Digitos += 1
		print(Numero, "tiene", Digitos, "digitos")

	def ordenar_lista (self,lista):
		lista1 = lista
		for contador in range(len(lista)): #Olvide el range()
			if lista1[contador] > lista1[contador+1]:
				lista1[contador] = lista1[contador+1]
				lista1[contador+1] = lista1[contador]
			print ("El resultado de ordenar la lista", lista, "es", lista1)

	def multi_matriz(self, matriz1, matriz2):
		nuevo_valor = 0
		nueva_matriz = []
		nueva_fila = []
		for contador in range(len(matriz1)):
			for valor in matriz1[contador]:
				for contador2 in range(len(matriz2[0])):
					for contador1 in range(len(matriz2)):
						nuevo_valor += valor * matriz2 [contador1][contador2]
					nueva_fila += [nuevo_valor]
					nuevo_valor = 0
			nueva_matriz += [nueva_fila]
			nueva_fila = []
		print ("El resultado es", nueva_matriz)