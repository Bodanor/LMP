# ------------------------------------------------------------------------
# Laboratoires de programmation mathématique et physique 2
# ------------------------------------------------------------------------
#
# Programme : 7 segments.
#
# ------------------------------------------------------------------------

#Samuel CHARLIER
#Maxime DERAVET
#Christos PAPADOPOULOS

import math
import pygame
import sys
import numpy as np
import datetime as dt


### Constante(s)

NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
ROUGE = (255, 0, 0)


### Variables Globales


def dessiner_arduino(sortie_arduino, sortie_CD4511, sortie_CD4028, sortie_bouton):
    fenetre.blit(image_arduino, pos_arduino)
    fenetre.blit(image_CD4511, pos_CD4511)
    fenetre.blit(image_bouton, pos_bouton)
    fenetre.blit(image_CD4028, pos_CD4028)


    for j in range(0, 2):
        if j == 0:
            off_ard = 285
            off_cd = 15
            pos_carte = pos_CD4511
            r = range(0, 4)

        if j == 1:
            off_ard = 194
            off_cd = 91
            pos_carte = pos_CD4028
            r = range(4, 8)

        for i in r:
            if sortie_arduino[i] == 0:
                couleur = NOIR
            else:
                couleur = ROUGE

            pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 280, pos_arduino[1] + off_ard),
                            (pos_carte[0] + 7, pos_carte[1] + off_cd), 5)
            off_ard = off_ard + 14
            off_cd = off_cd + 19



    off_cd = 15
    off_aff = 5
    i = 0
    for i in range(0, 7):
        if sortie_CD4511[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_afficheur[0] + 591, pos_afficheur[1] + off_aff),
                        (pos_CD4511[0] + 102, pos_CD4511[1] + off_cd), 5)
        off_aff = off_aff + 19
        off_cd = off_cd + 19


    if sortie_bouton == 0:
        couleur = NOIR
    else:
        couleur = ROUGE
    pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 279, pos_arduino[1] + 353),
                        (pos_bouton[0] + 13, pos_bouton[1] + 13), 5)

    i = 0
    off_cd = (102, 111)
    off_aff = 44
    for i in range(0, 6):
        if sortie_CD4028[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_CD4028[0] + off_cd[0], pos_CD4028[1] + off_cd[1]),
                        (pos_afficheur[0] + off_aff, pos_CD4028[1] + off_cd[1]), 5)

        pygame.draw.line(fenetre, couleur, (pos_afficheur[0] + off_aff, pos_afficheur[1]),
                        (pos_afficheur[0] + off_aff, pos_CD4028[1] + off_cd[1] - 2), 5)
        off_cd = (off_cd[0], off_cd[1] - 20)
        off_aff = off_aff + 101



def dessiner_afficheur(sortie_CD4511, sortie_CD4028):

    global latence_mat

    positions_barres = [[32, 14], [89, 20], [87, 88], [28, 150],
                        [17, 88], [19, 20], [30, 82]]



    for j in range(0, 6):
        fenetre.blit(image_afficheur_s, (pos_afficheur[0] + j*101, pos_afficheur[1]))

        i = 0
        for barre in positions_barres:
            if latence_mat[j][i] == 0:
                i = i + 1
                continue
            x_b = j*101 + pos_afficheur[0] + int(round(barre[0]*(image_afficheur_s.get_width()/133)))
            y_b = pos_afficheur[1] + int(round(barre[1]*(image_afficheur_s.get_height()/192)))
            if i == 0 or i == 3 or i == 6:
                fenetre.blit(barre_horizontale_s, (x_b, y_b))
            else:
                fenetre.blit(barre_verticale_s, (x_b, y_b))
            i = i + 1
    return

def composant_CD4511(entree):

    decimal = 0
    power = 0
    for i in range(len(entree)-5 ,-1, -1):
        decimal += entree[i]*2**power
        power+=1
    decimal = int(decimal)


    tdv = np.array([[0,0,1,0,1,1,1], [1,0,0,1,1,1,1],[0,0,0,1,1,1,0],[0,0,1,1,1,0,1],[0,1,1,1,1,1,1],[0,0,0,0,1,0,1],[0,1,1,1,1,0,1],[0,0,0,0,0,0,0]])


    return tdv[decimal]

def composant_CD4028(entree):

    decimal = 0
    power = 0
    for i in range(len(entree) - 1, 4, -1):
        decimal += entree[i] * 2 ** power
        power += 1
    decimal = int(decimal)
    afficheur_allume = [0,0,0,0,0,0]
    afficheur_allume[decimal-1]=1


    return afficheur_allume



def sortie_memorisee():

    size_array = 4
    arr_bin = np.zeros(size_array)
    arr_num = np.zeros(size_array)
    global valeur_memorisee
    global num_afficheur

    valeur_temp = valeur_memorisee
    temp_afficheur = num_afficheur

    while valeur_temp !=0: #Transformation en binbaire du nombre à afficher
        reste = valeur_temp %2
        arr_bin[size_array-1] = reste
        valeur_temp = valeur_temp//2
        size_array -= 1

    size_array = 4

    while temp_afficheur !=0: #Transformation en binaire du numéro de l'afficheur
        reste = temp_afficheur %2
        arr_num[size_array-1] = reste
        temp_afficheur = temp_afficheur//2
        size_array -= 1


    arr = np.append(arr_bin, arr_num)

    return arr

def gerer_click():
    return 0


def connexion_bouton(sortie_bouton):
    if sortie_bouton == 1:
        pygame.draw.line(fenetre, ROUGE, pin_arduino, pin_bouton, 5)

    else:
        pygame.draw.line(fenetre, NOIR, pin_arduino, pin_bouton, 5)
    return


def deplacer_hello(hello):
    pos_0  = hello[0]
    pos_1 = hello[1]
    pos_2 = hello[2]
    pos_3 = hello[3]
    pos_4= hello[4]
    pos_5= hello[5]
    pos_6= hello[6]
    pos_7= hello[7]
    pos_8= hello[8]
    pos_9= hello[9]
    pos_10= hello[10]
    pos_11 = hello[11]

    hello[0] = pos_1
    hello[1] = pos_2
    hello[2] = pos_3
    hello[3] = pos_4
    hello[4] = pos_5
    hello[5] = pos_6
    hello[6] = pos_7
    hello[7] = pos_8
    hello[8] = pos_9
    hello[9] = pos_10
    hello[10] = pos_11
    hello[11] = pos_0

    return hello






### Paramètre(s)

dimensions_fenetre = (1100, 600)  # en pixels
images_par_seconde = 25

pos_arduino = (0, 70)
pos_CD4511 = (333, 340)
pos_CD4028 = (333, 128)
pos_afficheur = (500, 350)
pos_bouton = (333, 524)
pos_centre_bouton = (pos_bouton[0] + 51, pos_bouton[1] + 34)
rayon_bouton = 18
pin_arduino = (pos_arduino[0] + 279, pos_arduino[1] + 353)
pin_bouton = (pos_bouton[0] + 13, pos_bouton[1] + 13)


### Programme

# Initialisation

pygame.init()

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 7 segments")

pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.time.set_timer(pygame.USEREVENT +1, 40)
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
num_afficheur = 1
sortie_memorisee()
latence_mat = np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])

hello = np.array([0,1,2,2,3,7,4,3,5,2,6,7])
# Boucle principale

a = 0

while True:
    try:


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
                        deplacer_hello(hello)

            if evenement.type == pygame.USEREVENT:
                sig_horloge = 1

                hello = deplacer_hello(hello)

            if evenement.type == pygame.USEREVENT+1:
                 latence_mat[num_afficheur - 1] = composant_CD4511(sortie_memorisee())

                 num_afficheur += 1
                 if num_afficheur > 6:
                    num_afficheur = 1
                 valeur_memorisee = hello[num_afficheur - 1]



        fenetre.fill(couleur_fond)

        sortie_CD4511 = composant_CD4511(sortie_memorisee())





        afficheur_allume = (composant_CD4028(sortie_memorisee()))

        dessiner_arduino(sortie_memorisee(), sortie_CD4511,
                        afficheur_allume, sortie_bouton)

        dessiner_afficheur(sortie_CD4511, afficheur_allume)
        pygame.display.flip()
        horloge.tick(images_par_seconde)

    except IndexError:
        pass