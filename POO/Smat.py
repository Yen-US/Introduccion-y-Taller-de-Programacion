Lista=[5,76,12,90,876]

class SumEl():
	def __init__(self, Lista):
		self.Lista = Lista
		self.TopeI = len(Lista)

	def SumaMat (self):
		Resultado = 0
		for Indice in range(self.TopeI):
			Resultado+=self.Lista[Indice]
		print (Resultado)

SL = SumEl(Lista)
SL.SumaMat()