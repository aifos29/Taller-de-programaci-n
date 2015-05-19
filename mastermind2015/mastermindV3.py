
################################################################
#         Mastermind										   #
################################################################

#########Debe de haber una forma mas facil de hacerlo############
import pygame, sys,os
import random
from pygame.locals import * 


#Definir variables Globlales
imagen = 0 #Guardar imagenes
estadoJuego =0 #Guardar el estado del juego
idioma=0# Variable para saber el idioma
listaoriginal=[]#Lista que se usa para comparar el juego
listaintento=[]#lista que el usuario introduce
intento=0# Variable donde van la cantidad de intentos
pantalla=0
contador=0#Variabla para saber cuantos intentos se han heho
elemento=0#Variable donde se almacena los elementos para compararlo en una lista
listatemporal=[]
correctas=[]
estrella=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\estrella.png")
flor=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\lor.png")
hongo=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\hongo.png")


#######################################################################
#                  Generalidades del juego							#
#######################################################################
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
##########################################################################
#	                         Pantalla de Idioma							 #
##########################################################################	
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
				estadoJuego=6
				inicioCiclo()
			if (x >= 743) and (x <= 844) and (y >= 554) and (y <= 587):
				estadoJuego=1
				inicioCiclo()
################Un jugador###################
def listaaletoria():
	global estadoJuego,imagen,listaoriginal
	listaoriginal=[1,2,3]
	random.shuffle(listaoriginal)	
	un_jugador()
def un_jugador():
	global estadoJuego,imagen
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugar_espanol.png")
	pygame.display.flip()
	while True: 
		intento1(pygame.event.get())  
		pantalla.blit(imagen, (0,0))
		pygame.display.flip()

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
	global estadoJuego,listaoriginal,contador,listatemporal
	
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
			
			if (x >= 899) and (x <= 996) and (y >= 560) and (y <= 597):
				estadoJuego=2
				inicioCiclo()
			if contador<3:
				if (x >= 41) and (x <= 138) and (y >= 29) and (y <= 129):
					listatemporal.append(1)
					contador=contador+1
					print listatemporal
				if (x >= 165) and (x <= 262) and (y >= 29) and (y <= 126):
					listatemporal.append(2)
					contador=contador+1
					print listatemporal
				if (x >= 40) and (x <= 138) and (y >= 140) and (y <= 237):
					listatemporal.append(3)
					contador=contador+1
					print listatemporal
				if (x >= 167) and (x <= 262) and (y >= 137) and (y <= 237):
					listatemporal.append(4)
					contador=contador+1
					print listatemporal
			if (x >= 328) and (x <= 515) and (y >= 362) and (y <= 429):
				print "guardar"
				listaoriginal=listatemporal
				estadoJuego=3
				print listaoriginal
				contador=contador-3
				print contador
				inicioCiclo()
			if (x >= 569) and (x <= 766) and (y >= 367) and (y <= 421):
				print "borrar"
				listatemporal=[]
				print listatemporal
				contador=contador-3
			
				
				
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
def la():
	global estadoJuego,imagen,listaoriginal
	listaoriginal=[1,2,3]
	random.shuffle(listaoriginal)	
	one_player()
def one_player():
        
	global estadoJuego,imagen	
	imagen=pygame.image.load("C:\Users\LATITUDE\Desktop\mastermind\data\jugar_ingles.png")
	pygame.display.flip()
	while True: 
		intento1(pygame.event.get())  
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
	while estadoJuego==6:
		listaaletoria()

def starCiclo():
	global estadoJuego,idioma
	while estadoJuego==1:
		Menu_espanol()
	while estadoJuego==2:
		players()
	while estadoJuego==3:
        
		la()
	while estadoJuego==4:
		two_players()		

##########################################################
#					Comparar lista                       #
##########################################################
def intento1(events):	
	global pantalla,listaintento,intento,contador
	
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			if intento<=4:
				if contador<3:
					if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
						listaintento.append (1)
						contador=contador+1
						print listaintento
						print listaoriginal
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
				
				if contador==3:
					if (x >= 49) and (x <= 141)  and (y >= 120) and (y <= 152):
						contador=contador-3
						intento=intento+1
						comprobar()

def intento2(events):

	global pantalla,listaintento,intento,contador
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			if intento<4:
				if contador<3:
					if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
						listaintento.append (1)
						contador=contador+1
						print listaintento
						estrella_intento2()
					if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
						listaintento.append(2)
						print listaintento
						contador=contador+1
						hongo_intento2()
					if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
						listaintento.append(3)
						print listaintento
						contador=contador+1
						flor_intento2()
					
				if contador==3:
					if (x >= 49) and (x <= 141)  and (y >= 120) and (y <= 152):
						contador=contador-3
						intento=intento+1
						comprobar()
def intento3(events):

	global pantalla,listaintento,intento,contador
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			if intento<=4:
				if contador<3:
					if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
						listaintento.append (1)
						contador=contador+1
						print listaintento
						estrella_intento3()
					if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
						listaintento.append(2)
						print listaintento
						contador=contador+1
						hongo_intento3()
					if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
						listaintento.append(3)
						print listaintento
						contador=contador+1
						flor_intento3()
					
				if contador==3:
					if (x >= 49) and (x <= 141)  and (y >= 120) and (y <= 152):
						contador=contador-3
						intento=intento+1
						comprobar()

def intento4(events):

	global pantalla,listaintento,intento,contador
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			if intento<=4:
				if contador<3:
					if (x >= 129) and (x <= 225)  and (y >= 503) and (y <= 607):
						listaintento.append (1)
						contador=contador+1
						print listaintento
						estrella_intento4()
					if (x >= 13) and (x <= 109)  and (y >= 563) and (y <= 607):
						listaintento.append(2)
						print listaintento
						contador=contador+1
						hongo_intento4()
					if (x >= 254) and (x <= 350)  and (y >= 563) and (y <= 607):
						listaintento.append(3)
						print listaintento
						contador=contador+1
						flor_intento4()
					
				if contador==3:
					if (x >= 49) and (x <= 141)  and (y >= 120) and (y <= 152):
						contador=contador-3
						intento=intento+1
						comprobar()
			else:
				print "No haga nada"


def listaCiclo():
	global intento,contador,correctas
	if intento==1:
		print "intento2"
		correctas=[]
		while True:
			intento2(pygame.event.get()) 
	if intento==2:
		print "intento3"
		correctas=[]
		while True:
			intento3(pygame.event.get())  	
	if intento==3: 
		correctas=[]
		print "intento4"
		while True:
			intento4(pygame.event.get())  	
	if intento==4:
		dibujar_listaoriginal()

def comprobar():
	global correctas,listaoriginal,listaintento,elemento
	elemento=listaintento.pop()	
	if listaintento==listaoriginal:
		print "ganaste"
	if len(listaintento)>0 :
		if elemento in listaoriginal:
			print "bien"
			correctas.append(elemento)
			comprobar()
		else:
				comprobar()
			
	else:
		if elemento in listaoriginal:
			correctas.append(elemento)
			print "bien"
			print len(correctas)
			listaintento=[]
			listaCiclo()
###############################################################################
#Pintar las imagenes, si las imagenes, no se me ocurrio otra cosa para hacerlo#	
###############################################################################
#########Solo las del primer intento##########################################
def estrella_intento1():
	global contador,estrella
	
	while contador==1:
		pantalla.blit(estrella,(628,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(estrella,(758,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(estrella,(879,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
def flor_intento1():
	global contador,flor
	
	while contador==1:
		pantalla.blit(flor,(628,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(flor,(758,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(flor,(879,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
def hongo_intento1():
	global contador,hongo
	
	while contador==1:
		pantalla.blit(hongo,(628,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==2:
		pantalla.blit(hongo,(758,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 
	while contador==3:
		pantalla.blit(hongo,(879,494))
		pygame.display.flip()
		intento1(pygame.event.get()) 

##################Segundo intento, debe de haber otra forma###########################
def estrella_intento2():
	global contador,estrella
	
	while contador==1:
		pantalla.blit(estrella,(628,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
	while contador==2:
		pantalla.blit(estrella,(758,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
	while contador==3:
		pantalla.blit(estrella,(879,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
def flor_intento2():
	global contador,flor
	
	while contador==1:
		pantalla.blit(flor,(628,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
	while contador==2:
		pantalla.blit(flor,(758,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
	while contador==3:
		pantalla.blit(flor,(879,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
def hongo_intento2():
	global contador,hongo
	
	while contador==1:
		pantalla.blit(hongo,(628,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
	while contador==2:
		pantalla.blit(hongo,(750,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 
	while contador==3:
		pantalla.blit(hongo,(876,364))
		pygame.display.flip()
		intento2(pygame.event.get()) 

##############En serio, para el intento 3,si existe una forma de hacerlo mas facil, avisen##################
def estrella_intento3():
	global contador,estrella
	
	while contador==1:
		pantalla.blit(estrella,(628,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
	while contador==2:
		pantalla.blit(estrella,(758,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
	while contador==3:
		pantalla.blit(estrella,(879,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
def flor_intento3():
	global contador,flor
	
	while contador==1:
		pantalla.blit(flor,(628,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
	while contador==2:
		pantalla.blit(flor,(758,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
	while contador==3:
		pantalla.blit(flor,(879,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
def hongo_intento3():
	global contador,hongo
	
	while contador==1:
		pantalla.blit(hongo,(628,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
	while contador==2:
		pantalla.blit(hongo,(758,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
	while contador==3:
		pantalla.blit(hongo,(879,230))
		pygame.display.flip()
		intento3(pygame.event.get()) 
 
##################La parte buena, es que llegamos al 4 intento y no se cae#############
def estrella_intento4():
	global contador,estrella
	
	while contador==1:
		pantalla.blit(estrella,(628,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
	while contador==2:
		pantalla.blit(estrella,(758,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
	while contador==3:
		pantalla.blit(estrella,(879,103))
		pygame.display.flip()
		intento1(pygame.event.get()) 
def flor_intento4():
	global contador,flor
	
	while contador==1:
		pantalla.blit(flor,(628,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
	while contador==2:
		pantalla.blit(flor,(758,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
	while contador==3:
		pantalla.blit(flor,(879,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
def hongo_intento4():
	global contador,hongo
	
	while contador==1:
		pantalla.blit(hongo,(628,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
	while contador==2:
		pantalla.blit(hongo,(758,103))
		pygame.display.flip()
		intento4(pygame.event.get()) 
	while contador==3:
		pantalla.blit(hongo,(879,103))
		pygame.display.flip()
		intento1(pygame.event.get())
def dibujar_listaoriginal():
        global estrella,flor,hongo
        if listaoriginal[0]==1:
                pantalla.blit(estrella,(25,209))
                pygame.display.flip()
        if listaoriginal[0]==2:
                pantalla.blit(hongo,(25,209))
                pygame.display.flip()
        if listaoriginal[0]==3:
                pantalla.blit(flor,(25,209))
                pygame.display.flip()
        if listaoriginal[1]==1:
                pantalla.blit(estrella,(151,209))
                pygame.display.flip()
        if listaoriginal[1]==2:
                pantalla.blit(hongo,(151,209))
                pygame.display.flip()
        if listaoriginal[1]==3:
                pantalla.blit(flor,(151,209))
                pygame.display.flip()
        if listaoriginal[2]==1:
                pantalla.blit(estrella,(274,209))
                pygame.display.flip()
                descanso()
        if listaoriginal[2]==2:
                pantalla.blit(hongo,(274,209))
                pygame.display.flip()
                descanso()
        if listaoriginal[2]==3:
                pantalla.blit(flor,(274,209))
                pygame.display.flip()
                descanso()
def descanso():
        print "Perdiste"

##############################################################
#################Dibujar la lista original####################

juego()
pantall_idioma()		
