import pygame, sys
from random import randint
from pygame.locals import *

pygame.init()


#------------------------------------------------------------------
# Variabelen en scherminstellingen
#------------------------------------------------------------------

#lijst met alle rectangles, voor collide check
rects = []    

#define total number of houses
total_Houses = 20

#define total number of each house type
total_Maisons = int(total_Houses * 0.15) 
total_Bungalows = int(total_Houses * 0.25)
total_Eensgezins = int(total_Houses * 0.60)

#kleurtjes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)  # = bungalow
GREEN = (  0, 255,   0) # = maison
BLUE = (  0,   0, 255) # = eensgezins

# De window size (= oppervlakte huizen gedeeld door 5 for now)
# Dan hebben we even een realistische representatie, we moeten de echte afmetingen op een andere manier zien te krijgen, met die pixels werkt zo niet...
WIDTH = 320
HEIGHT = 240
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)

#------------------------------------------------------------------
# Main program loop                                                
#------------------------------------------------------------------
while True:

    random_pos = (randint(0,WIDTH), randint(0,HEIGHT))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
           
            if event.key == K_q: #quit 
                pygame.quit()
                sys.exit()
            
            if event.key == K_g: #go 

                    #Plaatsing Maisons
                    for y in range (total_Maisons):
                        plaatsing = False
                        while plaatsing == False:

                            newhouse = pygame.draw.rect(screen, GREEN, (randint(33,WIDTH-33),randint(31,HEIGHT-31), 33, 45))
                            
                            if newhouse.collidelist(rects) == -1:
                                #add newhouse to [rects]
                                rects.append(newhouse)
                                plaatsing = True
                                # pygame.display.update(rects)


                    #Plaatsing Bungalows
                    for y in range (total_Bungalows):
                        plaatsing = False
                        while plaatsing == False:

                            newhouse = pygame.draw.rect(screen, RED, (randint(30,WIDTH-30),randint(22,HEIGHT-22), 30, 22))
                            
                            if newhouse.collidelist(rects) == -1:
                                #add newhouse to [rects]
                                rects.append(newhouse)
                                plaatsing = True
                                # pygame.display.update(rects)

                  
                    #Plaatsing Eengezinswoningen
                    for y in range (total_Eensgezins):
                        plaatsing = False
                        while plaatsing == False:

                            newhouse = pygame.draw.rect(screen, BLUE, (randint(24,WIDTH-24),randint(24,HEIGHT-24), 24, 24))
                            
                            if newhouse.collidelist(rects) == -1:
                                #add newhouse to [rects]
                                rects.append(newhouse)
                                plaatsing = True
                          
                    pygame.display.update(rects)
                    break