import pygame, sys,os
from pygame.locals import * 
listaoriginal=[2,1,3]
listaintento=[]
intento=0
pantalla=0
contador=0
opcion=0
estrella=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\estrella.png")
flor=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\lor.png")
hongo=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\hongo.png")
moneda=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\moneda.png")
def jugar():
#Definir variables Globlales
	global pantalla
	imagen = 0 #Guardar imagenes
	estadoJuego =0 #Guardar el estado del juego
	idioma=0

	#Arrancar el motor
	pygame.init() 
    #Crear ventana
	ventana = pygame.display.set_mode((1021,626)) 
	#cambiar titulo
	pygame.display.set_caption('Mastermind') 
	#Asignar superficie
	pantalla = pygame.display.get_surface()

	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugar_espanol.png")

	while True: 
		intento1(pygame.event.get()) 
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()

				
def intento1(events):	
	global pantalla,listaintento,intento,contador
	estrella=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\estrella.png")
	
	for event in events:
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			print x,y
			if contador<3:
				if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
					listaintento.append (1)
					contador=contador+1
					print listaintento
					estrella_intento1()
				if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
					listaintento.append(2)
					print listaintento
					contador=contador+1
					hongo_intento1()
				if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
					listaintento.append(3)
					print listaintento
					contador=contador+1
					flor_intento1()
				if (x >= 387) and (x <= 483)  and (y >= 563) and (y <= 607):
					listaintento.append(4)
					contador=contador+1
					print listaintento
					moneda_intento1()
					
			else:
				print contador
				intento=intento+1
				contador=contador-3
				comparar(listaintento,intento)

def intento2(events):

	global pantalla,listaintento,intento,contador
	for event in events:
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			
			if contador<3:
				if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
					listaintento.append (1)
					contador=contador+1
					print listaintento
				if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
					listaintento.append(2)
					print listaintento
					contador=contador+1
				if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
					listaintento.append(3)
					print listaintento
					contador=contador+1
				if (x >= 387) and (x <= 483)  and (y >= 563) and (y <= 607):
					listaintento.append(4)
					contador=contador+1
					print listaintento
					
			else:
				intento=intento+1
				contador=contador-3
				print contador
				print intento
				comparar(listaintento,intento)
def intento3(events):

	global pantalla,listaintento,intento,contador
	for event in events:
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			
			if contador<3:
				if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
					listaintento.append (1)
					contador=contador+1
					print listaintento
					
				if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
					listaintento.append(2)
					print listaintento
					contador=contador+1
				if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
					listaintento.append(3)
					print listaintento
					contador=contador+1
				if (x >= 387) and (x <= 483)  and (y >= 563) and (y <= 607):
					listaintento.append(4)
					contador=contador+1
					print listaintento
					
			else:
				intento=intento+1
				contador=contador-3
				print contador
				print intento
				comparar(listaintento,intento)

def intento4(events):

	global pantalla,listaintento,intento,contador
	for event in events:
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			
			if contador<3:
				if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
					listaintento.append (1)
					contador=contador+1
					print listaintento
					
				if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
					listaintento.append(2)
					print listaintento
					contador=contador+1
				if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
					listaintento.append(3)
					print listaintento
					contador=contador+1
				if (x >= 387) and (x <= 483)  and (y >= 563) and (y <= 607):
					listaintento.append(4)
					contador=contador+1
					print listaintento
					
			else:
				intento=intento+1
				contador=contador-3
				print contador
				print intento
				comparar(listaintento,intento)
				
def comparar(listas,inten):
	global listaoriginal,listaintento,intento
	
	if listaintento==listaoriginal:
		print "ganaste"
	else:
		
		listaCiclo(intento,listaintento)

def listaCiclo(inten,lista):
	global intento,listaintento
	
	if intento==1:
		listaintento=[]
		print "intento2"
		while True:
			intento2(pygame.event.get()) 
	if intento==2:
		listaintento=[]
		print "intento3"
		
		while True:
			intento3(pygame.event.get())  	
	if intento==3: 
		listaintento=[]
		print "intento4"
		while True:
			intento4(pygame.event.get())  	
	if intento==4:
		print listaoriginal
		print "perdiste"

def estrella_intento1():
	global contador,estrella
	
	while contador==1:
		pantalla.blit(estrella,(630,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(estrella,(750,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(estrella,(876,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
def flor_intento1():
	global contador,flor
	
	while contador==1:
		pantalla.blit(flor,(630,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(flor,(750,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(flor,(876,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
def hongo_intento1():
	global contador,hongo
	
	while contador==1:
		pantalla.blit(hongo,(630,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(hongo,(750,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(hongo,(876,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
def moneda_intento1():
	global contador,moneda
	
	while contador==1:
		pantalla.blit(moneda,(630,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(moneda,(750,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(moneda,(876,489))
		pygame.display.flip()
		intento1(pygame.event.get()) 
		
def dibujar_listaoriginal():
	global listaoriginal,hongo,estrella,flor,moneda
	if listaoriginal[0]==1:
		pantalla.blit(estrella,(0,0))
		pygame.display.flip()
	if listaoriginal[1]==2:
		pantalla.blit
jugar()
