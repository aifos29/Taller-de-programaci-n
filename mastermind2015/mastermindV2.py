import pygame, sys,os
from pygame.locals import * 


#Definir variables Globlales
imagen = 0 #Guardar imagenes
estadoJuego =0 #Guardar el estado del juego
idioma=0

def  juego():
	global pantalla, imagen, ventana, estadoJuego,idioma
	#Arrancar el motor
	pygame.init() 
    #Crear ventana
	ventana = pygame.display.set_mode((1021,626)) 
	#cambiar titulo
	pygame.display.set_caption('Mastermind') 
	#Asignar superficie
	pantalla = pygame.display.get_surface()
	
def pantall_idioma():

	global imagen,pantalla
	#Cargar imagen
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\idioma.png")
	
	while True: #Ciclo del menu en espanol
		evento_idioma(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()
########Idioma##################	
def evento_idioma(event):
	global estadoJuego,idioma
	for event in event:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			
			if (x >= 155) and (x <= 406)  and (y >= 391) and (y <= 532):
				idioma=2
				idioma_ciclo()
				
			if (x >= 450) and (x <= 729)  and (y >= 391) and (y <= 532):
				idioma=1
				idioma_ciclo()

####################################################
#				Interfaz Espanol                   #
####################################################

######################Menu#########################################
def Menu_espanol():
	global imagen,pantalla,estadoJuego
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\menu_espanol.png")
	
	while True: #Ciclo del menu en espanol
		eventos_Menu_espanol(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()

def eventos_Menu_espanol(events):	
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			
			if (x >= 363) and (x <= 510) and (y >= 313) and (y <= 339):
				estadoJuego=2
				inicioCiclo()
			if (x >= 364) and (x <= 735) and (y >= 394) and (y <= 428):
				print "ranking y puntuaciones"
			if (x >= 51) and (x <= 291) and (y >= 563) and (y <= 596):
				estadoJuego=5
				inicioCiclo()
			if (x >= 663) and (x <= 801) and (y >= 562) and (y <= 598):
				sys.exit(0)	

#################Creditos#############################################
def Creditos():
	global imagen,pantalla,estadoJuego
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\creditos.png")
	
	while True: #Ciclo del menu en espanol
		eventos_creditos(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()

def eventos_creditos(events):	
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos

#####################Jugar############################################
################Escoger jugadores####################################
def jugadores():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugadores_espanol.png")
	
	while True: #Ciclo del menu en espanol
		eventos_jugadores (pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def eventos_jugadores(events):
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
			if (x >= 361) and (x <= 797) and (y >= 46) and (y <= 177):
				estadoJuego=4
				inicioCiclo()
			if (x >= 237) and (x <= 671) and (y >= 469) and (y <= 599):	
				estadoJuego=3
				inicioCiclo()
			if (x >= 743) and (x <= 844) and (y >= 554) and (y <= 587):
				estadoJuego=1
				inicioCiclo()
################Un jugador###################
def un_jugador():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugar_espanol.png")
	pygame.display.flip()
	while True: 
		eventos_jugar(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def eventos_jugar(events):
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y	
			
##############dos jugadores##############
def dos_jugadores():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\dosjugadores.png")
	pygame.display.flip()
	while True: 
		eventos_dosjugadores(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def eventos_dosjugadores(events):
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			if (x >= 743) and (x <= 844) and (y >= 554) and (y <= 587):
				print "hola"
			if (x >= 330) and (x <= 515) and (y >= 364) and (y <= 422):
				estadoJuego=3
				inicioCiclo()
			if (x >= 887) and (x <= 992) and (y >= 560) and (y <= 601):
				estadoJuego=2
				inicioCiclo()
				
				
				
###################################################
#				Interfaz Ingles				      #
###################################################
#####################Menu#########################################
def Menu_ingles():
	global imagen,pantalla,estadoJuego
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\menu_ingles.png")
	
	while True: #Ciclo del menu en espanol
		eventos_Menu_ingles(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()

def eventos_Menu_ingles(events):	
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			
			if (x >= 363) and (x <= 510) and (y >= 313) and (y <= 339):
				estadoJuego=2
				starCiclo()
			if (x >= 364) and (x <= 735) and (y >= 394) and (y <= 428):
				print "ranking y puntuaciones"
			if (x >= 51) and (x <= 291) and (y >= 563) and (y <= 596):
				print "creditos"
			if (x >= 663) and (x <= 801) and (y >= 562) and (y <= 598):
				sys.exit(0)	
#####################Play############################################
################Choose Players####################################
def players():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jingles.png")
	
	while True: #Ciclo del menu en ingles
		eventos_players (pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def eventos_players(events):
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
			if (x >= 361) and (x <= 797) and (y >= 46) and (y <= 177):
				estadoJuego=4
				starCiclo()
			if (x >= 237) and (x <= 671) and (y >= 469) and (y <= 599):	
				estadoJuego=3
				starCiclo()
			if (x >= 743) and (x <= 844) and (y >= 554) and (y <= 587):
				estadoJuego=1
				starCiclo()
################One player###################
def one_player():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugar_ingles.png")
	pygame.display.flip()
	while True: 
		eventos_play(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def eventos_play(events):
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y	
			
##############dos jugadores##############
def two_players():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\players.png")
	pygame.display.flip()
	while True: 
		eventos_twoplayers(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def eventos_twoplayers(events):
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			if (x >= 743) and (x <= 844) and (y >= 554) and (y <= 587):
				print "hola"
			if (x >= 330) and (x <= 515) and (y >= 364) and (y <= 422):
				estadoJuego=3
				starCiclo()
			if (x >= 887) and (x <= 992) and (y >= 560) and (y <= 601):
				estadoJuego=2
				starCiclo()

			
###############Ciclos##################
def idioma_ciclo():
	global idioma
	while idioma==1:
		Menu_espanol()
	while idioma==2:
		Menu_ingles()

def inicioCiclo():
	global estadoJuego,idioma
	while estadoJuego==1:
		Menu_espanol()
	while estadoJuego==2:
		jugadores()
	while estadoJuego==3:
		un_jugador()
	while estadoJuego==4:
		dos_jugadores()
	while estadoJuego==5:
		Creditos()
def starCiclo():
	global estadoJuego,idioma
	while estadoJuego==1:
		Menu_espanol()
	while estadoJuego==2:
		players()
	while estadoJuego==3:
		one_player()
	while estadoJuego==4:
		two_players()		
juego()
pantall_idioma()		
