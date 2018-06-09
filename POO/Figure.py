class Figure():
	def __init__(self, Numero):
		self.Numero = Numero
	def triangle (self):
		Triangulo = "*"
		for a in range(self. Numero):
			print(Triangulo)
			Triangulo+="*"

TR = Figure(3)
TR.triangle()