#Samuel CHARLIER
#Maxime DERAVET
#Christos PAPADOPOULOS

import math
import pygame
import sys




# Constantes

BLEUCLAIR = (127, 191, 255)
BLEU = (23, 58, 196)
ROUGE = (255,0,0)
NOIR = (0,0,0)
BLEU = (0,0,255)
GRIS = (100,100,100)
NOIR = (0,0,0)

angle_moteur = math.pi/4

#Fonctions

def AfficherAimant():
    pygame.draw.rect(fenetre, ROUGE,pygame.Rect( (200,200), (200, 200)))
    pygame.draw.rect(fenetre, BLEU, pygame.Rect((400, 200), (200, 200)))

def AfficherCercle():
    pygame.draw.circle(fenetre, BLEUCLAIR, (400, 300), 125)
    pygame.draw.circle(fenetre, GRIS, (400, 300), 100)

def AfficherPetitCercle():
    pygame.draw.circle(fenetre, NOIR, (PositionCercle()), 10)

def PositionCercle():
    global angle_moteur
    positionX = 400 + math.cos(-angle_moteur) * 80
    positionY = 300 + math.sin(-angle_moteur) * 80
    PositionCercle = (positionX,positionY)
    return ( PositionCercle)

# Paramètres

dimensions_fenetre = (800, 600)  # en pixels
images_par_seconde = 25

pygame.init()

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 1")

horloge = pygame.time.Clock()
couleur_fond = BLEUCLAIR

fenetre.fill(couleur_fond)
AfficherAimant()
AfficherCercle()
AfficherPetitCercle()



while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    horloge.tick(images_par_seconde)