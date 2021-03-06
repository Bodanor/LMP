# ------------------------------------------------------------------------
# Laboratoires de programmation mathématique et physique 2
# ------------------------------------------------------------------------
#
# Programme : 7 segments.
#
# ------------------------------------------------------------------------

import math
import pygame
import sys
import numpy as np

### Constante(s)

NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
ROUGE = (255, 0, 0)


### Variables Globales


def dessiner_arduino(sortie_arduino, sortie_CD4511, sortie_bouton):
    fenetre.blit(image_arduino, pos_arduino)
    fenetre.blit(image_CD4511, pos_CD4511)
    fenetre.blit(image_bouton, pos_bouton)


    off_ard = 194
    off_cd = 15
    for i in range(0, 4):
        if sortie_arduino[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE

        pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 280, pos_arduino[1] + off_ard),
                        (pos_CD4511[0] + 7, pos_CD4511[1] + off_cd), 5)
        off_ard = off_ard + 14
        off_cd = off_cd + 19


    off_cd = 15
    off_aff = 27
    for i in range(0, 7):
        if sortie_CD4511[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_afficheur[0], pos_afficheur[1] + off_aff),
                        (pos_CD4511[0] + 102, pos_CD4511[1] + off_cd), 5)
        off_aff = off_aff + 19
        off_cd = off_cd + 19

    connexion_bouton(sortie_bouton)



def dessiner_afficheur(sortie_CD4511):
    positions_barres = [[32, 14], [89, 20], [87, 88], [28, 150],
                        [17, 88], [19, 20], [30, 82]]
    fenetre.blit(image_afficheur, pos_afficheur)

    i = 0
    for barre in positions_barres:
        if sortie_CD4511[i] == 0:
            i = i + 1
            continue
        x_b = pos_afficheur[0] + int(round(barre[0]*(image_afficheur.get_width()/133)))
        y_b = pos_afficheur[1] + int(round(barre[1]*(image_afficheur.get_height()/192)))
        if i == 0 or i == 3 or i == 6:
            fenetre.blit(barre_horizontale, (x_b, y_b))
        else:
            fenetre.blit(barre_verticale, (x_b, y_b))
        i = i + 1
    return

def composant_CD4511(entree):

    decimal = 0
    power = 0
    for i in range(len(entree)-1 ,-1, -1):
        decimal += entree[i]*2**power
        power+=1
    decimal = int(decimal)



    tdv = np.array([[1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1],
                   [1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1],
                   [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 0, 1, 1]])


    return tdv[decimal]



def sortie_memorisee():

    size_array = 4
    arr = np.zeros(size_array)
    global valeur_memorisee

    valeur_temp = valeur_memorisee

    while valeur_temp !=0:
        reste = valeur_temp %2
        arr[size_array-1] = reste
        valeur_temp = valeur_temp//2
        size_array -= 1

    return arr

def gerer_click():
    return 0


def connexion_bouton(sortie_bouton):
    if sortie_bouton == 1:
        pygame.draw.line(fenetre, ROUGE, pin_arduino, pin_bouton, 5)

    else:
        pygame.draw.line(fenetre, NOIR, pin_arduino, pin_bouton, 5)
    return


### Paramètre(s)

dimensions_fenetre = (1100, 600)  # en pixels
images_par_seconde = 25

pos_arduino = (65, 84)
pos_CD4511 = (537, 263)
pos_afficheur = (818, 251)
pos_bouton = (537, 486)
pos_centre_bouton = (589, 521)
rayon_bouton = 18
pin_arduino = (pos_arduino[0] + 279, pos_arduino[1] + 353)
pin_bouton = (pos_bouton[0] + 13, pos_bouton[1] + 13)


### Programme

# Initialisation

pygame.init()

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 7 segments")

pygame.time.set_timer(pygame.USEREVENT, 500)
horloge = pygame.time.Clock()

image_afficheur_s = pygame.image.load('images/7_seg_s.png').convert_alpha(fenetre)
barre_verticale_s = pygame.image.load('images/vertical_s.png').convert_alpha(fenetre)
barre_horizontale_s = pygame.image.load('images/horizontal_s.png').convert_alpha(fenetre)
image_afficheur = pygame.image.load('images/7_seg.png').convert_alpha(fenetre)
barre_verticale = pygame.image.load('images/vertical.png').convert_alpha(fenetre)
barre_horizontale = pygame.image.load('images/horizontal.png').convert_alpha(fenetre)
image_arduino = pygame.image.load('images/arduino.png').convert_alpha(fenetre)
image_CD4511 = pygame.image.load('images/CD4511.png').convert_alpha(fenetre)
image_CD4028 = pygame.image.load('images/CD4028.png').convert_alpha(fenetre)
image_bouton = pygame.image.load('images/bouton.png').convert_alpha(fenetre)
couleur_fond = GRIS

#Variables
valeur_memorisee = 0
sortie_memorisee()

# Boucle principale


while True:
    sig_horloge = 0
    sortie_bouton = 0
    temps_maintenant = pygame.time.get_ticks()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evenement.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x<pos_centre_bouton[0] + rayon_bouton and mouse_x > pos_centre_bouton[0] - rayon_bouton:
                if mouse_y < pos_centre_bouton[1] + rayon_bouton and mouse_y > pos_centre_bouton[1] - rayon_bouton:
                    sortie_bouton = 1

        if evenement.type == pygame.USEREVENT:
            sig_horloge = 1


    fenetre.fill(couleur_fond)

    sortie_CD4511 = composant_CD4511(sortie_memorisee())
    dessiner_afficheur(sortie_CD4511)
    if sortie_bouton == 1:
        valeur_memorisee +=1
    if sig_horloge == 1:
        valeur_memorisee +=1
        pygame.draw.circle(fenetre, ROUGE, pos_afficheur, 10)
    else:
        pygame.draw.circle(fenetre, NOIR, pos_afficheur, 10)
    if valeur_memorisee >=10:
        valeur_memorisee = 0
    dessiner_arduino(sortie_memorisee(), sortie_CD4511, sortie_bouton)

    pygame.display.flip()
    horloge.tick(images_par_seconde)
