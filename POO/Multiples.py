class Multiples ():
	def __init__ (self):
		pass
	def Table (self):
		tabla = int(input("Ingrese la tabla de multiplicar: "))
		a=0
		while a!=11:
			print (tabla,"x",a,"=",tabla*a)
			a+=1
Tabla= Multiples()
Tabla.Table()