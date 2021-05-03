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

GRIS = (100,100,100)


pygame.font.init()

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



angle_moteur = 0
compteur = 0
courant_moteur = 0
vitesse_moteur = 0
temps_precedent = 0
temps = 0


pygame.key.set_repeat(10, 10)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                compteur = 5


    if compteur == 0:
        courant_moteur = 0
    else:
        courant_moteur = 1

    fenetre.fill(couleur_fond)
    AfficherAimant()
    AfficherCercle()
    AfficherPetitCercle()
    AfficherTDB(fenetre)

    mettre_a_jour_moteur(temps)

    temps_precedent = temps_maintenant

    if compteur != 0:
        compteur -= 1


    pygame.display.flip()
    horloge.tick(images_par_seconde)