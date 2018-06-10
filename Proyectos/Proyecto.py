#Se importan la librerias a utilizar
import pygame
from pygame.locals import *
#Se definen las variables, colores e instancias a utilizar
Modo=0
ModoA=0
Cambio=2
angle=90

Puntuacion=0

PosX, PosY=80,220
Pos2X, Pos2Y= 110,210
PosX_2, PosY_2= 130,310
PosEX, PosEY= 110,210
PosE1X, PosE1Y= 110,310
PosE2X, PosE2Y= 70, 300
PosEX_2, PosEY_2= 60, 330
PosE1X_2, PosE1Y_2= 60, 380
PosE2X_2, PosE2Y_2= 130, 370
Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
PDX, PDY=0 ,0
Blanco=(255,255,255)
Lista_Disparos=pygame.sprite.Group()
Todos_sprites1 = pygame.sprite.Group()
Todos_sprites2 = pygame.sprite.Group()

E=True
C=True
Disparos=True
Colisiones=False
#Lista_Disparos=pygame.sprite.Group()

#Se define la clase que se va a utilizar con todos los objetos
class PyObj (pygame.sprite.Sprite) :
	#Se define la clase constructora con las variables para los metodos de los objetos
	def __init__ (self, Imagen, Angulo, PX, PY): 
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load (Imagen)
		self.rect = self.image.get_rect()
		self.PX=PX
		self.PY=PY
	#Se define el metodo update, el responsable de mover al actualizar los objetos, es decir actualizando su pocision
	def update (self,PX,PY):
		self.rect.x=PX
		self.rect.y=PY

	def rotar(self, angle):
		self.image = pygame.transform.rotate(self.image, angle)
		self.rect = self.image.get_rect()

	def rotarI (self, img):
		self.image = img
		self.rect = self.image.get_rect()

	def disparo (self,x,y):
		NBala=Bala(x,y)		
		Lista_Disparos.add(NBala)
		Todos_sprites1.add(NBala)
		Todos_sprites2.add(NBala)

class Bala(PyObj):
	def __init__(self, PDX, PDY):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([1000,1000])
		self.image=self.image.fill([0,0,0])
		self.image= pygame.image.load("Imagenes/Bala.png")
		self.rect = self.image.get_rect()
		self.rect.top= PDY
		self.rect.left= PDX
		self.VDisp=20
	def update (self):
		self.rect.top=PDY
		self.rect.left=PDX
		self.rect.left -= self.VDisp


Reloj = pygame.time.Clock()

#Se inicia pygame
pygame.init() 

#Se crea la ventana
ventana = pygame.display.set_mode ((1300,625))
pygame.display.set_caption ("Death Race")

#Se importan las imagenes a utilizar como objetos de imagen
Pista = pygame.image.load ("Imagenes/pista.png")
Pista1=pygame.image.load ("Imagenes/Pista2.png")
Inicio = pygame.image.load ("Imagenes/Inicio.jpg")
Fondo = pygame.image.load ("Imagenes/Calle.jpg")
Fondo1=pygame.image.load ("Imagenes/Calle2.jpg")
GameOver = pygame.image.load ("Imagenes/GO.jpg")
Explosion = pygame.image.load ("Imagenes/Explosion.png")

Jugador= PyObj("Imagenes/C1P1.png",angle,PosX,PosY)
Jugador2=PyObj ("Imagenes/C1P1.png",angle,Pos2X,Pos2Y)
Jugador_2=PyObj("Imagenes/C1P1.png",angle,PosX_2,PosY_2)

#Se importan las imagenes para las diferentes pocisiones del jugador
JP0=pygame.image.load("Imagenes/C1P0.png")
JP1=pygame.image.load("Imagenes/C1P1.png")
JP2=pygame.image.load("Imagenes/C1P2.png")
JP3=pygame.image.load("Imagenes/C1P3.png")

JP0_2=pygame.image.load("Imagenes/C1P0_2.png")
JP1_2=pygame.image.load("Imagenes/C1P1_2.png")
JP2_2=pygame.image.load("Imagenes/C1P2_2.png")
JP3_2=pygame.image.load("Imagenes/C1P3_2.png")
#Se importa e inicia la reproduccion del track principal
pygame.mixer.music.load("Sonidos/Track1.wav")

#El -1 indica al mixer que reproduzca la cancion infinitas veces
pygame.mixer.music.play(-1)

#Se crean los rectangulos de limite con (cordenada x, cordenaday, ancho, alto) para el tercer nivel
Rect1=pygame.Rect  (0,0,60,625)
Rect2=pygame.Rect  (0,0,1300,30)
Rect3=pygame.Rect  (1239,0,61,625)
Rect4=pygame.Rect  (0,408,252,219)
Rect5=pygame.Rect  (0,599,1300,30)
Rect6=pygame.Rect  (1050,411,252,213)
Rect7=pygame.Rect  (615,251,83,375)
Rect8=pygame.Rect  (170,140,335,162)
Rect9=pygame.Rect  (360,140,147,357)
Rect10=pygame.Rect  (806,140,134,353)
Rect11=pygame.Rect  (806,138,324,162)

#Se crean los rectangulos de limite con (cordenada x, cordenaday, ancho, alto) para el segundo niverl
Rect2_1=pygame.Rect (205,210,885,208) 
Rect2_2=pygame.Rect (0,0,58,56) 
Rect2_3=pygame.Rect (1227,0,76,47) 
Rect2_4=pygame.Rect (0,565,61,67)
Rect2_5=pygame.Rect (1234,567,67,58)
Rect2_6=pygame.Rect (0,0,1300,2)
Rect2_7=pygame.Rect (0,0,2,625)
Rect2_8=pygame.Rect (1298,0,2,625)
Rect2_9=pygame.Rect (0,623,1300,2)

#Se define la funcion de la ventana de Game Over
def pyGO(Modo):
	global C
	#Se crea un loop infinito
	while C:
		#Se dibuja la imagen antes importada de game over
		ventana.blit(GameOver,(0,0))
		#Se define el detector de eventos de pygame el cual va a ser responsable de los eventos del usuario
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			#Se define la funcion de cada tecla	
			elif event.type==pygame.KEYDOWN:
				if event.key==K_UP:
					pygame.quit()
					exit()
				elif event.key==K_DOWN:
					C= False
					pyModos(Modo)
		#se actualiza la ventana
		pygame.display.update()

# se define la funcion del menu
def pymenu(Modo):
	#Se crea un loop infinito pero con limite para el Modo 0 el cual es el menu 
	while Modo==0:
		#se dibuja la ventana de menu
		ventana.blit(Inicio,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			#Se define la funcion de cada tecla	
			elif event.type==pygame.KEYDOWN:
				if event.key==K_UP:
					Modo=1
					pyModos(Modo)
				elif event.key==K_DOWN:
					Modo=2
					pyModos(Modo)
		pygame.display.update()
# Se define la funcion de los modos de juego y sus pistas
def pyModos(Modo):

	global 	C, Puntuacion, PosX, PosY, Pos2X, Pos2Y, PosX_2, PosY_2, PosEX, PosEY, PosE1X, PosE1Y, PosE2X, PosE2Y, Velocidad, Velocidad2, Velocidad_2, VelocidadE, Pos, Pos2, Pos_2, PosE, PosEX_2, PosEY_2, PosE1X_2, PosE1Y_2,  PosE2X_2, PosE2Y_2
	#Se crea las listas de sprites
	Jugadores_lista1 = pygame.sprite.Group()
	Enemigos_lista1 = pygame.sprite.Group()
	Jugadores_lista2 = pygame.sprite.Group()
	Enemigos_lista2 = pygame.sprite.Group()

	#Se crea el jugador y se define su pocision

	Jugador.rect.x=PosX
	Jugador.rect.y=PosY
	Jugador2.rect.x=Pos2X
	Jugador2.rect.y=Pos2Y
	Jugador_2.rect.x=PosX_2
	Jugador_2.rect.y=PosY_2

	#Se crean los objetos Enemigos y se especifican sus cordenadas de inicio
	Enemigo = PyObj("Imagenes/Enemigos1.png",angle,PosEX,PosEY)
	Enemigo1 = PyObj("Imagenes/Enemigos1.png",angle,PosE1X,PosE1Y)
	Enemigo2 = PyObj("Imagenes/Enemigos1.png",angle,PosE2X,PosE2Y)
	Enemigo_2 = PyObj("Imagenes/Enemigos1.png",angle,PosEX_2,PosEY_2)
	Enemigo.rect.x = PosEX
	Enemigo.rect.y = PosEY
	Enemigo1.rect.x = PosE1X
	Enemigo1.rect.y = PosE1Y
	Enemigo2.rect.x = PosE2X
	Enemigo2.rect.y = PosE2Y
	Enemigo_2.rect.x = PosEX_2
	Enemigo_2.rect.y = PosEY_2

	"""Enemigo1_2 = PyObj("Imagenes/Enemigos1.png",angle,PosE1X_2,PosE1Y_2)
	Enemigo1.rect.x = PosE1X_2
	Enemigo1.rect.y = PosE1Y_2


	Enemigo2_2 = PyObj("Imagenes/Enemigos1.png",angle,PosE2X_2,PosE2Y_2)
	Enemigo2.rect.x = PosE2X_2
	Enemigo2.rect.y = PosE2Y_2"""

	# Se anaden tales objetos a las listas de sprites correspondientes
	Todos_sprites1.add([Enemigo])
	Todos_sprites1.add([Enemigo1])
	Todos_sprites1.add([Enemigo2])

	Todos_sprites2.add([Enemigo_2])
	"""Todos_sprites2.add([Enemigo1_2])
	Todos_sprites2.add([Enemigo2_2])"""
	

	#Se anaden a las listas correspondientes los objetos creados
	Jugadores_lista1.add([Jugador])
	Todos_sprites1.add([Jugador])
	Jugadores_lista1.add([Jugador2])
	Todos_sprites1.add([Jugador2])
	Jugadores_lista2.add([Jugador_2])
	Todos_sprites2.add([Jugador_2])


	#Se crea un loop infinito pero con un tope para poder cambiar de Modo de juego 
	while Modo==1:
		#Se dibujan los rectangulos para el primer nivel, los cuales son los limites de la pista

		pygame.draw.rect(ventana,Blanco,Rect2_1)
		pygame.draw.rect(ventana,Blanco,Rect2_2)
		pygame.draw.rect(ventana,Blanco,Rect2_3)
		pygame.draw.rect(ventana,Blanco,Rect2_4)
		pygame.draw.rect(ventana,Blanco,Rect2_5)
		pygame.draw.rect(ventana,Blanco,Rect2_6)
		pygame.draw.rect(ventana,Blanco,Rect2_7)
		pygame.draw.rect(ventana,Blanco,Rect2_8)
		pygame.draw.rect(ventana,Blanco,Rect2_9)
		#Se dibujan en pantalla las imagenes a utilizar anteriormente definidas
		ventana.fill([0,0,0])
		ventana.blit(Fondo,(0,0))
		ventana.blit(Pista1,(0,0))

		#Se dibujan los sprites anterimente difinidos y agregados a listas
		pygame.sprite.Group.draw (Todos_sprites2, ventana)

		#Se crea un loop infinito pero con un tope para poder cambiar de Modo de juego 
		if Pos_2==0:
			PosX_2+=Velocidad_2
		elif Pos_2==1:
			PosY_2-=Velocidad_2
		elif Pos_2==2:
			PosX_2-=Velocidad_2
		elif Pos_2==3:
			PosY_2+=Velocidad_2

		#Se crean las condiciones de choque con los rectangulos anteriormente definidos y las acciones a realizar en caso de verdadero
		if Rect2_1.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)
		
		elif Rect2_2.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)

		elif Rect2_3.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)

		elif Rect2_4.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)

		elif Rect2_5.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)
		elif Rect2_6.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)
		elif Rect2_7.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)
		elif Rect2_8.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)
		elif Rect2_9.colliderect(Jugador_2.rect):
			PosX_2, PosY_2= 135,310
			PosEX_2, PosEY_2= 60, 330
			PosE1X_2, PosE1Y_2= 60, 380
			PosE2X_2, PosE2Y_2= 130, 370
			Velocidad, Velocidad2, Velocidad_2, VelocidadE= 0, 0, 0, 5
			Pos, Pos2, Pos_2, PosE=1, 1, 1, 0
			pygame.sprite.Group.empty(Todos_sprites2)
			Jugador_2.rotarI(JP1)
			C=True
			pyGO(Modo)

		if PosEY_2==510 and PosEX_2==60:
			Enemigo_2.rotar(-angle)
			PosEY_2-=VelocidadE
		elif PosEY_2>100 and PosEX_2==60:
			PosEY_2-=VelocidadE
		elif PosEY_2 ==100 and PosEX_2==60:
			Enemigo_2.rotar(-angle)
			PosEX_2+=VelocidadE
		elif PosEY_2==100 and PosEX_2<1160:
			PosEX_2+=VelocidadE
		elif PosEY_2==100 and PosEX_2==1160:
			Enemigo_2.rotar(-angle)
			PosEY_2+=VelocidadE
		elif PosEY_2<510 and PosEX_2==1160:
			PosEY_2+=VelocidadE
		elif PosEY_2==510 and PosEX_2==1160:
			Enemigo_2.rotar(-angle)
			PosEX_2-=VelocidadE
		elif PosEY_2==510 and PosEX_2>60:
			PosEX_2-=VelocidadE

		#Se invoca el detector de eventos de pygame el cual va adetectar las acciones del jugador mientras se repita el loop de juego
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			#Se definen las pocisiones de el/los jugadores el cual se encarga de detectar el estado de orientacion del mismo
			if Pos_2==0:
				#Se definen las acciones de cada tecla segun la pocision
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador_2.rotarI(JP3)
						Pos_2=3
					elif event.key== K_LEFT:
						Jugador_2.rotarI(JP1)
						Pos_2=1
					elif event.key == K_UP:
						Velocidad_2 += Cambio
					elif event.key == K_DOWN:
						Velocidad_2 -= Cambio
					elif event.key == K_SPACE:
						x,y = Jugador_2.rect.center
						Jugador_2.disparo(x,y)
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()
			elif Pos_2==1:
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador_2.rotarI(JP0)
						Pos_2=0
					elif event.key== K_LEFT:
						Jugador_2.rotarI(JP2)
						Pos_2=2
					elif event.key == K_UP:
						Velocidad_2+= Cambio
					elif event.key == K_DOWN:
						Velocidad_2-= Cambio
					elif event.key == K_SPACE:
						x,y = Jugador_2.rect.center
						Jugador_2.disparo(x,y)
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()
			elif Pos_2==2:
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador_2.rotarI(JP1)
						Pos_2=1
					elif event.key== K_LEFT:
						Jugador_2.rotarI(JP3)
						Pos_2=3
					elif event.key == K_UP:
						Velocidad_2+= Cambio
					elif event.key == K_DOWN:
						Velocidad_2-= Cambio
					elif event.key == K_SPACE:
						x,y = Jugador_2.rect.center
						Jugador_2.disparo(x,y)
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()					
			elif Pos_2==3:
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador_2.rotarI(JP2)
						Pos_2=2
					elif event.key== K_LEFT:
						Jugador_2.rotarI(JP0)
						Pos_2=0
					elif event.key == K_UP:
						Velocidad_2+= Cambio
					elif event.key == K_DOWN:
						Velocidad_2-= Cambio
					elif event.key == K_SPACE:
						x,y = Jugador_2.rect.center
						Jugador_2.disparo(x,y)
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()
		# Se actualiza el objeto del jugador el cual va a mover el objeto en pantalla al actualizar su pocision constantemente
		Jugador_2.update(PosX_2,PosY_2)
		Enemigo_2.update(PosEX_2,PosEY_2)
		"""Enemigo1_2.update(PosE1X_2,PosE1Y_2)
		Enemigo2_2.update(PosE2X_2,PosE2Y_2)"""
		Lista_Disparos.update()
		Reloj.tick(200)
		#Se actualiza la pantalla en general
		pygame.display.flip()

	Jugador.image=JP1_2
	#Se define el loop de juego del segundo nivel
	while Modo==2:
		#Se dibujan los rectangulos de limite en  pantalla
		pygame.draw.rect(ventana,Blanco,Rect1)
		pygame.draw.rect(ventana,Blanco,Rect2)
		pygame.draw.rect(ventana,Blanco,Rect3)
		pygame.draw.rect(ventana,Blanco,Rect4)
		pygame.draw.rect(ventana,Blanco,Rect5)
		pygame.draw.rect(ventana,Blanco,Rect6)
		pygame.draw.rect(ventana,Blanco,Rect7)
		pygame.draw.rect(ventana,Blanco,Rect8)
		pygame.draw.rect(ventana,Blanco,Rect9)
		pygame.draw.rect(ventana,Blanco,Rect10)
		pygame.draw.rect(ventana,Blanco,Rect11)
		#Se rellena la pnatalla de color y se dibujan las imagenes de pantalla
		ventana.fill([0,0,0])
		ventana.blit(Fondo,(0,0))
		ventana.blit(Pista,(0,0))

		#Se dibujan los sprites anterimente difinidos y agregados a listas
		pygame.sprite.Group.draw (Todos_sprites1, ventana)
		#Se elimina el jugador 2 ya que este es el modo de un jugador
		Jugadores_lista1.remove(Jugador2)
		Todos_sprites1.remove(Jugador2)

		# Se detectan las colisiones del jugador con los limites de la pantalla
		if Rect1.colliderect(Jugador.rect):
			#Se definen las circunstancia sa realizar si hay algun tipo de colision con los limites
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)
		
		elif Rect2.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect3.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect4.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect5.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect6.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect7.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect8.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0,5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect9.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect10.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)

		elif Rect11.colliderect(Jugador.rect):
			PosX, PosY=80,220
			PosEX, PosEY= 110,210
			PosE1X, PosE1Y= 110,300
			PosE2X, PosE2Y= 70, 300
			Velocidad, VelocidadE= 0, 5
			Pos, PosE=1, 0
			pygame.sprite.Group.empty(Todos_sprites1)
			Jugador.rotarI(JP1_2)
			C=True
			pyGO(Modo)


		#Se define el loop de movimiento de los enemigos, el cual actualiza las variables de pocision asignadas a acada uno
		if PosEY==340 and PosEX==110:
			Enemigo.rotar(-angle)
			PosEY-=VelocidadE
		elif PosEY>80 and PosEX==110:
			PosEY-=VelocidadE
		elif PosEY ==80 and PosEX==110:
			Enemigo.rotar(-angle)
			PosEX+=VelocidadE
		elif PosEY==80 and PosEX<1140:
			PosEX+=VelocidadE
		elif PosEY==80 and PosEX==1140:
			Enemigo.rotar(-angle)
			PosEY+=VelocidadE
		elif PosEY<330 and PosEX==1140:
			PosEY+=VelocidadE
		elif PosEY==330 and PosEX==1140:
			Enemigo.rotar(-angle)
			PosEX-=VelocidadE
		elif PosEY==330 and PosEX>950:
			PosEX-=VelocidadE
		elif PosEY==330 and PosEX==950:
			Enemigo.rotar(angle)
			PosEY+=VelocidadE
		elif PosEY<530 and PosEX==950:
			PosEY+=VelocidadE
		elif PosEY==530 and PosEX==950:
			Enemigo.rotar(-angle)
			PosEX-=VelocidadE
		elif PosEY==530 and PosEX>740:
			PosEX-=VelocidadE
		elif PosEY==530 and PosEX==740:
			Enemigo.rotar(-angle)
			PosEY-=VelocidadE
		elif PosEY>180 and PosEX==740:
			PosEY-=VelocidadE
		elif PosEY==180 and PosEX==740:
			Enemigo.rotar(angle)
			PosEX-=VelocidadE
		elif PosEY==180 and PosEX>540:
			PosEX-=VelocidadE
		elif PosEY==180 and PosEX==540:
			Enemigo.rotar(angle)
			PosEY+=VelocidadE
		elif PosEY<510 and PosEX==540:
			PosEY+=VelocidadE
		elif PosEY==510 and PosEX==540:
			Enemigo.rotar(-angle)
			PosEX-=VelocidadE
		elif PosEY==510 and PosEX>300:
			PosEX-=VelocidadE
		elif PosEY==510 and PosEX==300:
			Enemigo.rotar(-angle)
			PosEY-=VelocidadE
		elif PosEY>340 and PosEX==300:
			PosEY-=VelocidadE
		elif PosEY==340 and PosEX==300:
			Enemigo.rotar(angle)
			PosEX-=VelocidadE
		elif PosEY==340 and PosEX>110:
			PosEX-=VelocidadE
			#Movimiento Enemigo 1
		if PosE1Y==340 and PosE1X==110:
			Enemigo1.rotar(-angle)
			PosE1Y-=VelocidadE
		elif PosE1Y>40 and PosE1X==110:
			PosE1Y-=VelocidadE
		elif PosE1Y ==40 and PosE1X==110:
			Enemigo1.rotar(-angle)
			PosE1X+=VelocidadE
		elif PosE1Y==40 and PosE1X<1160:
			PosE1X+=VelocidadE
		elif PosE1Y==40 and PosE1X==1160:
			Enemigo1.rotar(-angle)
			PosE1Y+=VelocidadE
		elif PosE1Y<330 and PosE1X==1160:
			PosE1Y+=VelocidadE
		elif PosE1Y==330 and PosE1X==1160:
			Enemigo1.rotar(-angle)
			PosE1X-=VelocidadE
		elif PosE1Y==330 and PosE1X>950:
			PosE1X-=VelocidadE
		elif PosE1Y==330 and PosE1X==950:
			Enemigo1.rotar(angle)
			PosE1Y+=VelocidadE
		elif PosE1Y<530 and PosE1X==950:
			PosE1Y+=VelocidadE
		elif PosE1Y==530 and PosE1X==950:
			Enemigo1.rotar(-angle)
			PosE1X-=VelocidadE
		elif PosE1Y==530 and PosE1X>740:
			PosE1X-=VelocidadE
		elif PosE1Y==530 and PosE1X==740:
			Enemigo1.rotar(-angle)
			PosE1Y-=VelocidadE
		elif PosE1Y>150 and PosE1X==740:
			PosE1Y-=VelocidadE
		elif PosE1Y==150 and PosE1X==740:
			Enemigo1.rotar(angle)
			PosE1X-=VelocidadE
		elif PosE1Y==150 and PosE1X>540:
			PosE1X-=VelocidadE
		elif PosE1Y==150 and PosE1X==540:
			Enemigo1.rotar(angle)
			PosE1Y+=VelocidadE
		elif PosE1Y<510 and PosE1X==540:
			PosE1Y+=VelocidadE
		elif PosE1Y==510 and PosE1X==540:
			Enemigo1.rotar(-angle)
			PosE1X-=VelocidadE
		elif PosE1Y==510 and PosE1X>300:
			PosE1X-=VelocidadE
		elif PosE1Y==510 and PosE1X==300:
			Enemigo1.rotar(-angle)
			PosE1Y-=VelocidadE
		elif PosE1Y>340 and PosE1X==300:
			PosE1Y-=VelocidadE
		elif PosE1Y==340 and PosE1X==300:
			Enemigo1.rotar(angle)
			PosE1X-=VelocidadE
		elif PosE1Y==340 and PosE1X>110:
			PosE1X-=VelocidadE
			#Movimiento Enemigo 2
		if PosE2Y==340 and PosE2X==70:
			Enemigo2.rotar(-angle)
			PosE2Y-=VelocidadE
		elif PosE2Y>80 and PosE2X==70:
			PosE2Y-=VelocidadE
		elif PosE2Y ==80 and PosE2X==70:
			Enemigo2.rotar(-angle)
			PosE2X+=VelocidadE
		elif PosE2Y==80 and PosE2X<1150:
			PosE2X+=VelocidadE
		elif PosE2Y==80 and PosE2X==1150:
			Enemigo2.rotar(-angle)
			PosE2Y+=VelocidadE
		elif PosE2Y<330 and PosE2X==1150:
			PosE2Y+=VelocidadE
		elif PosE2Y==330 and PosE2X==1150:
			Enemigo2.rotar(-angle)
			PosE2X-=VelocidadE
		elif PosE2Y==330 and PosE2X>950:
			PosE2X-=VelocidadE
		elif PosE2Y==330 and PosE2X==950:
			Enemigo2.rotar(angle)
			PosE2Y+=VelocidadE
		elif PosE2Y<530 and PosE2X==950:
			PosE2Y+=VelocidadE
		elif PosE2Y==530 and PosE2X==950:
			Enemigo2.rotar(-angle)
			PosE2X-=VelocidadE
		elif PosE2Y==530 and PosE2X>750:
			PosE2X-=VelocidadE
		elif PosE2Y==530 and PosE2X==750:
			Enemigo2.rotar(-angle)
			PosE2Y-=VelocidadE
		elif PosE2Y>180 and PosE2X==750:
			PosE2Y-=VelocidadE
		elif PosE2Y==180 and PosE2X==750:
			Enemigo2.rotar(angle)
			PosE2X-=VelocidadE
		elif PosE2Y==180 and PosE2X>500:
			PosE2X-=VelocidadE
		elif PosE2Y==180 and PosE2X==500:
			Enemigo2.rotar(angle)
			PosE2Y+=VelocidadE
		elif PosE2Y<510 and PosE2X==500:
			PosE2Y+=VelocidadE
		elif PosE2Y==510 and PosE2X==500:
			Enemigo2.rotar(-angle)
			PosE2X-=VelocidadE
		elif PosE2Y==510 and PosE2X>260:
			PosE2X-=VelocidadE
		elif PosE2Y==510 and PosE2X==260:
			Enemigo2.rotar(-angle)
			PosE2Y-=VelocidadE
		elif PosE2Y>340 and PosE2X==260:
			PosE2Y-=VelocidadE
		elif PosE2Y==340 and PosE2X==260:
			Enemigo2.rotar(angle)
			PosE2X-=VelocidadE
		elif PosE2Y==340 and PosE2X>70:
			PosE2X-=VelocidadE

		#Se definen las condiciones del movimiento continuo del jugador que depende de su pocision
		if Pos==0:
			PosX+=Velocidad
		if Pos==1:
			PosY-=Velocidad
		if Pos==2:
			PosX-=Velocidad
		if Pos==3:
			PosY+=Velocidad

		#Se llama al detector de eventos en pantalla de pygame
				#Se invoca el detector de eventos de pygame el cual va adetectar las acciones del jugador mientras se repita el loop de juego
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			#Se definen las pocisiones de el/los jugadores el cual se encarga de detectar el estado de orientacion del mismo
			if Pos==0:
				#Se definen las acciones de cada tecla segun la pocision
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador.rotarI(JP3_2)
						Pos=3
					elif event.key== K_LEFT:
						Jugador.rotarI(JP1_2)
						Pos=1
					elif event.key == K_UP:
						Velocidad += Cambio
					elif event.key == K_DOWN:
						Velocidad -= Cambio
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()
			elif Pos==1:
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador.rotarI(JP0_2)
						Pos=0
					elif event.key== K_LEFT:
						Jugador.rotarI(JP2_2)
						Pos=2
					elif event.key == K_UP:
						Velocidad+= Cambio
					elif event.key == K_DOWN:
						Velocidad-= Cambio
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()
			elif Pos==2:
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador.rotarI(JP1_2)
						Pos=1
					elif event.key== K_LEFT:
						Jugador.rotarI(JP3_2)
						Pos=3
					elif event.key == K_UP:
						Velocidad+= Cambio
					elif event.key == K_DOWN:
						Velocidad-= Cambio
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()					
			elif Pos==3:
				if event.type == pygame.KEYDOWN:
					if event.key==K_RIGHT:
						Jugador.rotarI(JP2_2)
						Pos=2
					elif event.key== K_LEFT:
						Jugador.rotarI(JP0_2)
						Pos=0
					elif event.key == K_UP:
						Velocidad+= Cambio
					elif event.key == K_DOWN:
						Velocidad-= Cambio
					elif event.key==K_ESCAPE:
						pygame.quit()
						quit()
		# Se actualiza al jugador en pantalla y a los enemigos presentes
		Jugador.update(PosX,PosY)
		Enemigo.update(PosEX,PosEY)
		Enemigo1.update(PosE1X,PosE1Y)
		Enemigo2.update(PosE2X,PosE2Y)
		Reloj.tick(200)
		#Se actualiza la pantalla en general
		pygame.display.flip()

#Se llama al menu para poder elegir
pymenu(Modo)