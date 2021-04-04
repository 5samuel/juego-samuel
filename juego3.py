import pygame
import sys

#constatnte
ancho= 800
alto= 600
color_rojo=(255,0,0)

#jugador
jugador_pos =[400,400]
jugador_size=50

#crear ventana 
ventana = pygame.display.set_mode((ancho, alto))

game_over = False
#cerrar ventana

while not game_over:
    for event  in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            X= jugador_pos[0]
            if event.hey == pygame.K_LEFT: 
                X -=jugador_size
        if event.type== pygame.K_RIGHT:

            x +=jugador_size
        jugador_pos [0] = x   
   
    #Crear pensonaje
    pygame.draw.rect(ventana, color_rojo, (jugador_pos[0],jugador_pos[1], jugador_size,jugador_size))
    pygame.display.update()