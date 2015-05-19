
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

######Pantalla donde se escoge el idioma##############
def pantalla_idioma():
	global imagen,pantalla
	#Cargar imagen
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\idioma.png")
	
	while True: #Ciclo del menu en espanol
		evento_idioma(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()
	
def evento_idioma(event):
	global estadoJuego,idioma
	for event in event:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
		
			if (x >= 155) and (x <= 406) and (y >= 391) and (y <= 532):
				estadoJuego=2
				idioma=2
				inicioCiclo()
			if (x >= 450) and (x <= 729) and (y >= 393) and (y <= 532):
				estadoJuego=1
				idioma=1
				inicioCiclo()
#####Pantalla para el menu##############	
def idioma_menu():
	if idioma==1:
		Menu_espanol()
	if idioma==2:
		Menu_ingles()
def Menu_espanol():
	global imagen,pantalla
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\menu_espanol.png")
	
	while True: #Ciclo del menu en espanol
		eventos_Menu(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()
	

def Menu_ingles():
	global imagen,pantalla
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\menu_ingles.png")
	
	while True: #Ciclo del menu en espanol
		eventos_Menu(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()

def eventos_Menu(events):	
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
			if (x >= 363) and (x <= 505) and (y >= 310) and (y <= 342):
				estadoJuego=3
				inicioCiclo()
			if (x >= 364) and (x <= 610) and (y >= 407) and (y <= 439):
				print "ranking y puntuaciones"
			if (x >= 53) and (x <= 253) and (y >= 508) and (y <= 609):
				print "creditos"
			if (x >= 662) and (x <= 776) and (y >= 580) and (y <= 608):
				print "salir"				
			
#######Pantalla jugadores y sus eventos

####Un solo jugador#####
def jugador_espanol():
	global imagen,pantalla
	#Cargar imagen
	imagen = pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugadores_espanol.png")
	
	while True: #Ciclo del menu en espanol
		eventos_jugadores(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()

def jugador_ingles():
	global imagen,pantalla
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jingles.png")
	
	while True: #Ciclo del menu en espanol
		eventos_jugadores(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		
		#Actualizar pantalla
		pygame.display.flip()	
		
def eventos_jugadores(events):
	global estadoJuego
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			

		
#####Pantalla de Juego y sus eventos##############		

#####def jugadores ingles####
def jugadores():
	global idioma
	if idioma==1:
		p_jugador()
	if idioma==2:
		p_player()


def p_jugador():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugadores_espanol.png")
	
	while True: #Ciclo del menu en espanol
		eventos_p_jugador(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def p_player():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jingles.png")
	
	while True: #Ciclo del menu en espanol
		eventos_p_jugador(pygame.event.get())  
		pantalla.blit(imagen, (0,0))		
		pygame.display.flip()	

def eventos_p_jugador(events):
	
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
			if (x >= 359) and (x <= 794) and (y >= 47) and (y <= 177):
				estadoJuego=4
				inicioCiclo()
			if (x >= 236) and (x <= 671) and (y >= 235) and (y <= 599):	
				estadoJuego=5
				inicioCiclo()


#########Pantalla de Idioma

def un_jugador_ingles():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugar_ingles.png")
	
	while True: 
		eventos_jugar(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()
def dos_jugadores_ingles():
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\dosjugadores_ingles.png")
	
	while True: #Ciclo del menu en espanol
		eventos_jugar(pygame.event.get())  
		pantalla.blit(imagen, (0,0))		
		#Actualizar pantalla	
		pygame.display.flip()	

def eventos_jugar(events):
	
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
#####Pantalla para jugadores espanoles#######		



	





				
		
		
			
#####################Eventos Generales################		
		
def consumirEvento(events):  
	global estadoJuego,idioma
	for event in events: 
		
		#Si el evento es de tipo QUIT, salimos.
		if event.type == QUIT: 
			sys.exit(0)
			 
		else:
			inicioCiclo()
		
			
			
			

def inicioCiclo():
	global estadoJuego,idioma
	
	while estadoJuego==0 and idioma==0:
		pantalla_idioma()
	while estadoJuego==1 and idioma==1: 
		Menu_espanol()
	while estadoJuego==2 and idioma==2:
		Menu_ingles()
	while estadoJuego == 3:
		jugadores()
	while estadoJuego==4:
		dos_jugadores_ingles()
	while estadoJuego==5:
		un_jugador_ingles()
		
		 
juego()
pantalla_idioma()

