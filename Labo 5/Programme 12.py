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

def AfficherTDB(fenetre):
    courant_font = pygame.font.SysFont('Comic Sans MS', 18)
    courantSurface = courant_font.render(f"Courant : {courant_moteur} A", False, NOIR)
    fenetre.blit(courantSurface, (10,10))

def mettre_a_jour_moteur(t):
    global angle_moteur, vitesse_angulaire
    K = 1000
    R = 0.02
    L = 0.06
    B = 0.5
    J = 1
    Phi = 2 * K * R * L * courant_moteur * B * math.cos(angle_moteur)

    acceleration_angulaire = (Phi / J) - (vitesse_angulaire*0.2)


    vitesse_angulaire += acceleration_angulaire * temps
    angle = vitesse_angulaire * temps

    angle_moteur += angle








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
vitesse_angulaire = 0


pygame.key.set_repeat(10, 10)

while True:

    temps_maintenant = pygame.time.get_ticks()/1000
    temps = temps_maintenant - temps_precedent

    evenement = pygame.event.get()
    for event in evenement:
        if event.type == pygame.QUIT:
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