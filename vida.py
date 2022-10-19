#vida.py
import pygame
import numpy as np
import time
import sys
import datetime

pygame.init()

print ('El Juego de la Vida, de John Horton Conway')
print ('Devta Singh © 2022')
print ('https://github.com/devta-singh/el-juego-de-la-vida/')
print ('basado en el codigo de dotCSV en el siguiente video:')
print ('https://www.youtube.com/watch?v=qPtKv9fSHZY&t=4s')
print ('-----------------------------')
print ('Menu:')
print ('Cualquier tecla detiene o reinicia el juego')
print ('Con el juego parado, usa el ratón para activar o desactivar una celda')
print ('X -  Grabar estado')
print ('Q - Salir')

#damos ancho y alto a la pantalla
width, height = 1000, 1000

#creamos la pantalla con ancho y alto en pixeles
screen = pygame.display.set_mode((height, width))


bg = 25, 25, 25

#pintamos el fondo de la pantalla
screen.fill(bg)


#determinamos cuantas celdas en cada dirección

#nxC, nyC = 25, 25
nxC_por_defecto = 25
nyC_por_defecto = 25
print ('Dimension X -por defecto: ',nxC_por_defecto,'-')
try:
	nxC = int(input())
except:
	nxC=nxC_por_defecto

print('Dimension Y -por defecto: ',nyC_por_defecto,'-')
try:
	nyC = int(input())
except:
	nyC=nyC_por_defecto	

#establecemos las dimensiones de las celdas
dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0;
gameState = np.zeros((nxC, nyC))


# Inicializamos algunos datos

#creamos algunas figuras, marcando en el x,y el valor 1 (viva)

# Automata palo 
gameState[5, 3] = 1;
gameState[5, 4] = 1;
gameState[5, 5] = 1;


# Automata movil
gameState[21, 21] = 1;
gameState[22, 22] = 1;
gameState[22, 23] = 1;
gameState[21, 23] = 1;
gameState[20, 23] = 1;


# Control de ejecución.
pauseExect = False

#bucle de ejecución
while True:

	newGameState = np.copy(gameState)

	# repintamos el fondo (borramos la pantalla)
	screen.fill(bg)
	time.sleep(0.1)


	# Registramos eventos de teclado y ratón.
	ev = pygame.event.get()

	for event in ev:
		if event.type == pygame.KEYDOWN:

			#ante cualquier tecla, cambiamos el estado de la ejecución
			#del programa, es un togle on/off o un off/on
			pauseExect = not pauseExect
			# if event.key == pygame.K_LEFT:
			# 	print ("tecla izquierda")
			# if event.key == pygame.K_RIGHT:
			# 	print ("tecla derecha")
			if event.key == pygame.K_q:
				print ("Salimos del programa (tecla Q)")	
				pygame.quit()
				sys.exit(0)
			if event.key == pygame.K_x:
				print ("Exportamos el estado del juego")
				# fichero_exportacion='./exportado.txt'	
				# try:
				# 	fichero=input('fichero de exportacion: '+fichero_exportacion)
				# except:
				# 	fichero=fichero_exportacion
				#fichero='~/Documents/python3/juego_de_la_vida/exportado.txt'
				#fichero='/~/Documents/python3/juego_de_la_vida/exportado.txt'
				fichero_base='/Users/devtasingh/Documents/python3/juego_de_la_vida/partida_'
				fichero_ext='.txt'

				# using now() to get current time
				current_time = datetime.datetime.now()
				 
				# Printing attributes of now().
				ano=str(current_time.year)				 
				mes=str(current_time.month)				 
				dia=str(current_time.day)				 
				hora=str(current_time.hour)
				minuto=str(current_time.minute)
				segundo=str(current_time.second)
				 
				ahora=''+ano+mes+dia+'-'+hora+minuto+segundo

				fichero= fichero_base + ahora + fichero_ext

				#grabamos el contenido del juego en el fichero
				with open(fichero, "w") as file:
					#data = string.join(gameState)

					#print GameState[]
					print('Empezamos a grabar datos')
					datos='#El Juego de la Vida - de John Horton Conway\n'
					datos+='#por Devta Singh\n'
					datos+='#©2022 devtas@gmail.com\n'
					datos+='#Devta Singh © 2022'
					datos+='#https://github.com/devta-singh/el-juego-de-la-vida/'
					datos+='#basado en el codigo de dotCSV en el siguiente video:'
					datos+='#https://www.youtube.com/watch?v=qPtKv9fSHZY&t=4s'
					datos+='#-----------------------------'
					datos+='#'+ahora+'\n'
					datos+='#fichero exportacion: '+fichero+'\n'
					datos+='#dimensiones: '+str(nxC)+' x '+ str(nyC) +'\n'
					datos+='#estado de juego:\n'

					for __y in range(0, nyC):
						linea=''
						for __x in range(0,nxC):
							linea += str(int(gameState[__x,__y]))

						datos += linea
						datos += "\n"
					
					try:	
						file.write(datos)
						print('fichero '+fichero+' grabado')
					except:
						print('Error al grabar el fichero', fichero )

				print('tras grabar, seguimos')

		mouseClick = pygame.mouse.get_pressed()
		#print(mouseClick) #obtiene el vector de botones del raton (no pulsado = 0; pulsados = 1)

		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			#newGameState[celX, celY] = 1 #cambia a 1 activo el estado de la celda
			newGameState[celX, celY] = not mouseClick[2] #toma la lectura del boton izquierdo del raton y la niega


	#hacemos dos bucles for anidados para recorrer filas y columnas
	for y in range(0, nxC):
		for x in range(0,nyC):

			#controlamos si se han de actualizar las reglas
			if not pauseExect:

				# Calculamos el número de vecinos cercanos.
				n_neigh = gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
				          gameState[(x)     % nxC, (y - 1)  % nyC] + \
				          gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
				          gameState[(x - 1) % nxC, (y)      % nyC] + \
				          gameState[(x + 1) % nxC, (y)      % nyC] + \
				          gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
				          gameState[(x)     % nxC, (y + 1)  % nyC] + \
				          gameState[(x + 1) % nxC, (y + 1)  % nyC]


				# Regla #1 : Una célula muerta con exactamente 3 vecinas vivas, "revive".

				if gameState[x, y] == 0 and n_neigh == 3:
					newGameState[x, y] = 1

				# Regla #2 : Una célula viva con menos de 2  o más de 3 vecinas vivas, "muere"
				elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
					newGameState[x, y] = 0

			#creamos el polígono para esta celda de fila y columna
			poly = [((x)   * dimCW, y * dimCH),
					((x+1) * dimCW, y * dimCH),
					((x+1) * dimCW, (y+1) * dimCH),
					((x)   * dimCW, (y+1) * dimCH)]

			#dibujamos polígonos para cada celda, creando la cuadrícula
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128,128,128), poly, 1)#solo los bordes
			else:
				pygame.draw.polygon(screen, (255,255,255), poly, 0)#relleno solido

	
	# Actualizamos el estado del juego
	gameState = np.copy(newGameState)

	pygame.display.flip()

	pass
