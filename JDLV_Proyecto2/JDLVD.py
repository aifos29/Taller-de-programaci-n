import pygame,sys,os
from pygame.locals import *
import pickle
####variables de la Parte grafica################
imagen=0 #varible para cargar image

pantalla=0#pantalla
ventana=0#ventana
idioma=0#idoma

#####Variables de la parte logica############
#crear matriz
FIL=100
COL=100
matriz=[]
#asignar tiempo3
tiempo=0
#cambio de regla
mavom=0
mivom=0
mavos=0
mivos=0
nvov=0
#calcular vecinos
vecinos=0
#cargar imagenes
muerto=pygame.image.load("muerto.png")
vivo=pygame.image.load("vivo.png")
#estado del juego
estado=0
#cambio de reglas
reglas=0
contador_1=0
contador_2=0
contador_3=0
contador_4=0
contador_5=0
#definir jugar#
jugar=False

########Creacion de la ventana########

#$$$$$$$$$$$$$$	PARTE GRAFICA EN TODO SU ESPLENDOR$$$$$$$$$$$$$$$$$#	
#.........Pantalla Idioma........#
#Pantalla donde el usuario escoge el idioma con el que desea empezar###
def pantalla_idioma():
	global pantalla,ventana,ancho,alto,imagen,idioma
	pygame.init()
	ventana=pygame.display.set_mode((500,600))
	pygame.display.set_caption("Idioma")
	pantalla=pygame.display.get_surface()
	imagen=pygame.image.load("Idioma.png")
	while True:
		Epantalla_idioma(pygame.event.get())
		pantalla.blit(imagen,(0,0))
		pygame.display.flip()
def Epantalla_idioma(events):
	global idioma
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x,y=event.pos
			if x>180 and x<320 and y>227 and y<279:
				idioma=1
				menu()
			if x>180 and x<320 and y>327 and y<383:
				idioma=2
				menu()
			if x>432 and x<470 and y>526 and y<578:
				sys.exit(0)
#.......Menu......#
#pantalla del menu, contiene tres opciones: vecinos, instrucciones,comenzar
def menu():
	
	global idioma
	
	pygame.init()
	ventana=pygame.display.set_mode((500,600))
	pygame.display.set_caption("Menu")
	pantalla=pygame.display.get_surface()
	if idioma==1:
		imagen=pygame.image.load("menu_e.png")
	if idioma==2:
		imagen=pygame.image.load("menu_i.png")
	while True:
		Emenu(pygame.event.get())
		pantalla.blit(imagen,(0,0))
		pygame.display.flip()
def Emenu(events):
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x,y=event.pos
			if x>166 and x<335 and y>157 and y<201:
				pantalla_vecinos()
			if x>161 and x<347 and y>348 and y<398:
				instrucciones()
			if x>200 and x<302 and y>258 and y<300:
				pantalla_1()
			if x>17 and x<160 and y>529 and y<570:
				pantalla_idioma()
			if 373<x<467 and 530<y<569:
				sys.exit(0)

	

#....Instrucciones......#
#carga una pantalla con instrucciones y para ir vecinos y volver al 
#
def instrucciones():
	
	global pantalla,ventana,imagen,i_idioma,idioma
	
	pygame.init()
	ventana=pygame.display.set_mode((705,396))
	if idioma==1:
		pygame.display.set_caption("Instrucciones")
	if idioma==2:
		pygame.display.set_caption("Instructions")
	pantalla=pygame.display.get_surface()
	if idioma==1:
		imagen=pygame.image.load("In_es.png")
	if idioma==2:
		imagen=pygame.image.load("In_in.png")
	while True:
		Einstrucciones(pygame.event.get())
		pantalla.blit(imagen,(0,0))
		pygame.display.flip()
def Einstrucciones(events):
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x,y=event.pos
			if x>192 and x<318 and y>351 and y<376:
				pantalla_vecinos()
			if x>363 and x<464 and y>351 and y<376:
				pantalla_1()
#...........Vecinos........#
def pantalla_vecinos():

	#El usuario puede cambiar la cantidad de vecinos que desea en su juego, de no hacerlo
	#lo hara por defecto
	global pantalla,ventana,imagen,i_idioma,idioma,numero1,numero2,numero
	
	pygame.init()
	ventana=pygame.display.set_mode((633,584))
	if idioma==1:
		pygame.display.set_caption("Vecinos")
	if idioma==2:
		pygame.display.set_caption("Neighbors")
	pantalla=pygame.display.get_surface()
	if idioma==1:
		imagen=pygame.image.load("vec_esp.png")
	if idioma==2:
		imagen=pygame.image.load("vec_ing.png")
	while True:
		Evecinos(pygame.event.get())
		pantalla.blit(imagen,(0,0))
		pygame.display.flip()
def Evecinos(events):
###Cambiar los valores de una variable global siguiendo los requerimientos del usuario##
###	
	global reglas,mavom,mavos,mivom,mivos,nvov,contador_1,contador_2,contador_3,contador_4,contador_5
	
	
	for event in events:
		if event.type == QUIT: 
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			x,y=event.pos
                        print x,y
			if contador_1==0:
				if x>14 and x<54 and y>55 and y<98:
					mivom=1
					contador_1=1	
				if x>73 and x<113 and y>55 and y<98:
					mivom=4
					contador_1=+1
				if x>140 and x<185 and y>55 and y<98:
					mivom=5
					contador_1=+1
				if x>203 and x<242 and y>55 and y<98:
					mivom=6
					contador_1=+1
				if x>265 and x<299 and y>55 and y<98:
					mivom=7
					contador_1=+1
				if x>331 and x<376 and y>55 and y<98:
					mivom=8
					contador_1=+1
			print mivom		
			if contador_2==0:
				if x>14 and x<54 and y>156 and y<190:
					mavom=1
					contador_2=1
				if x>73 and x<113 and y>156 and y<190:
					mavom=4
					contador_2=1
				if x>140 and x<185 and y>156 and y<190:
					mavom=5
					contador_2=1
				if x>203 and x<242 and y>156 and y<190:
					mavom=6
					contador_2=1	
				if x>265 and x<299 and y>156 and y<190:
					mavom=7
					contador_2=1	
				if x>331 and x<376 and y>156 and y<190:
					mavom=8
					contador_2=1
			if contador_3==0:
				if x>14 and x<54 and y>260 and y<303:
					mivos=1
					contador_3=1
				if x>73 and x<113 and y>260 and y<303:
					mivos=4
					contador_3=1	
				if x>140 and x<185 and y>260 and y<303:
					mivos=5
					contador_3=1
				if x>203 and x<242 and y>260 and y<303:
					mivos=6
					contador_3=1
				if x>265 and x<299 and y>260 and y<303:
					mivos=7
					contador_3=1
				if x>331 and x<376 and y>260 and y<303:
					mivos=8
					contador_3=1
			if contador_4==0:
				if x>14 and x<54 and y>348 and y<398:
					mavos=1
					contador_4=1
				if x>73 and x<113 and y>348 and y<398:
					mavos=4
					contador_4=1	
				if x>140 and x<185 and y>348 and y<398:
					mavos=5
					contador_4=1
				if x>203 and x<242 and y>348 and y<398:
					mavos=6
					contador_4=1
				if x>265 and x<299 and y>348 and y<398:
					mavos=7
					contador_4=1
				if x>331 and x<376 and y>348 and y<398:
					mavos=8
					contador_4=1
			if contador_5==0:
				if x>14 and x<54 and y>474 and y<520:
					nvov=1
					contador_5=1
				if x>73 and x<113 and y>474 and y<520:
					nvov=4
					contador_5=1
				if x>140 and x<185 and y>474 and y<520:
					nvov=5
					contador_5=1
				if x>203 and x<242 and y>474 and y<520:
					nvov=6
					contador_5=1
				if x>265 and x<299 and y>474 and y<520:
					nvov=7
					contador_5=1
				if x>331 and x<376 and y>474 and y<520:
					nvov=8
					contador_5=1	
			if x>97 and x<289 and y>495 and y<538:
				reglas=1
				estadoj(1)
			if x>368 and x<551 and y>498 and y<543:
				menu()

			

def pantalla_1():
###Crear la pantalla de juego, cambiando el set caption segun el idioma#######333	
	pygame.init()
	ventana=pygame.display.set_mode((500,600))	
	if idioma==1:
		pygame.display.set_caption("Juego de la vida")
	if idioma==2:
		pygame.display.set_caption("Game of the life")
	pantalla=pygame.display.get_surface()
	if idioma==1:
		imagen=pygame.image.load("Fondo.jpg")
	if idioma==2:
		imagen=pygame.image.load("Fondo2.jpg")	
	while True:
		pantalla.blit(imagen,(0,0))
		pygame.display.flip()
		
		pintar_vivos()
def pintar_vivos():
	crear_matriz()
	while True: 
		Consumir(pygame.event.get())
		for e in range(0, len(matriz)):
			for i in range(0, len(matriz)):
				if(matriz[e][i] == 1):
					pantalla.blit(vivo, (e*5,i*5))
					
				else:
					pantalla.blit(muerto, (e*5,i*5))
		pygame.display.flip()
		if jugar==True:
			logica()
			pygame.time.wait(tiempo)
def Consumir(events):
	global matriz,tiempo,reglas,jugar
	for event in events:
		if event.type == QUIT: 
			
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			#obtener coordenadas
			x, y = event.pos
			print x,y
			if(0<x<500 and 0<y<495):
				matriz[x/5][y/5]=1
			if(191<x<303 and 551<y<581):
				jugar=True
				regla()
			if(197<x<298 and 514<y<543):
				archivo=open("Matriz.txt","r")
				matriz=pickle.load(archivo)
				archivo.close()
				if(6<x<118 and 506<y<554):
					archivo=open("Matriz.txt ","w")
					pickle.dump(matriz, archivo)
					archivo.close()
			if (428<x<460 and 544<y<569):
				tiempo=tiempo+100
				print tiempo
			if (55<x<95 and 359<y<567):
				tiempo=tiempo-100
				print tiempo
				
	
                                
                                        
##########Parte logica############
def crear_matriz():###Crear la matriz
	global FIL,COL,matriz
	for i in range(FIL):
		lista=[]
		for e in range(COL):
			lista.append(0)
		matriz.append(lista)
	
#####Reglas####
def regla():	
	global reglas
	if reglas==0:
		logica()
	if reglas==1:
		logica_1()
####.....Parte logica con las reglas originales....#
####"""Basicamente crea una matriz auxiliar para no afectar la primera, luego mediante
##conjunto de listas agrega los vecinos alredor de cada casilla, crea una matriz donde guarda dicho
###y despues vuelve a recorrer la nueva lista creada, para agregar unos o ceros, segun corresponda
#busca los vecinos siguiendo las primeras reglas###


def logica():
	
	global matriz, tiempo
	#Hacer matriz auxiliar
	temporal = []
		
	for j in range(0,len(matriz)):
		lista=[]
		for i in range(0,len(matriz)):
			lista.append(0)
		temporal.append(lista)
		
	#Recorrer matriz
	for e in range(1, len(matriz)-1):
		for i in range(1, len(matriz)-1):
			#Obtener numero de vecinos
			lista1=[matriz[e-1][i-1],matriz[e][i-1],matriz[e+1][i-1]]
			lista2=[matriz[e-1][i],matriz[e][i],matriz[e+1][i]]
			lista3=[matriz[e-1][i+1],matriz[e][i+1],matriz[e+1][i+1]]
			
			vivo=0
			muerto=0
			
			matriz2=[]
			matriz2.append(lista1)
			matriz2.append(lista2)
			matriz2.append(lista3)
			
			for j in range(3):
				for k in range(3):
					if not (j==1 and k ==1):
						if matriz2[j][k]==1:
							vivo+=1
						else:
							muerto+=1
			
			#Determinar vivo o muerto
			if matriz[e][i]==1:	
				if vivo<2:#Condicion de muerte
					temporal[e][i]=0
				elif vivo>3:
					temporal[e][i]=0
				elif vivo==2 or vivo==3:#Condicion de supervivencia
					temporal[e][i]=1
					
			elif matriz[e][i]==0:
				if vivo==3:#Condicion de vida
					temporal[e][i]=1
			
	matriz=temporal		
	pygame.time.wait(tiempo)
####.....Parte logica con las reglas cambiadas....#
####"""Basicamente crea una matriz auxiliar para no afectar la primera, luego mediante
##conjunto de listas agrega los vecinos alredor de cada casilla, crea una matriz donde guarda dicho
###y despues vuelve a recorrer la nueva lista creada, para agregar unos o ceros, segun corresponda
#busca los vecinos siguiendo las reglas del usuario###


def logica_1():
	
	global matriz,mavom,mavos,mivom,mivos,nvov
	#Hacer matriz auxiliar
	temporal = []
		
	for j in range(0,len(matriz)):
		lista=[]
		for i in range(0,len(matriz)):
			lista.append(0)
		temporal.append(lista)
		
	#Recorrer matriz
	for e in range(1, len(matriz)-1):
		for i in range(1, len(matriz)-1):
			#Obtener numero de vecinos
			lista1=[matriz[e-1][i-1],matriz[e][i-1],matriz[e+1][i-1]]
			lista2=[matriz[e-1][i],matriz[e][i],matriz[e+1][i]]
			lista3=[matriz[e-1][i+1],matriz[e][i+1],matriz[e+1][i+1]]
			
			vivo=0
			muerto=0
			
			matriz2=[]
			matriz2.append(lista1)
			matriz2.append(lista2)
			matriz2.append(lista3)
			
			for j in range(3):
				for k in range(3):
					if not (j==1 and k ==1):
						if matriz2[j][k]==1:
							vivo+=1
						else:
							muerto+=1
			
			#Determinar vivo o muerto
			if matriz[e][i]==1:	
				if vivo<mivom:#Condicion de muerte
					temporal[e][i]=0
				elif vivo>mavom:
					temporal[e][i]=0
				elif vivo==mivos or vecinos==mavos:#Condicion de supervivencia
					temporal[e][i]=1
					
			elif matriz[e][i]==0:
				if nvov==3:#Condicion de vida
					temporal[e][i]=1
			
	matriz=temporal			
def estadoj(estado):
	if(estado==1):
		pintar_vivos()
	
pantalla_idioma()

		
	
