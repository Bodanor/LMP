#Samuel CHARLIER
#Maxime DERAVET
#Christos PAPADOPOULOS


import math
import pygame
import sys



def ajouter_objet(x,y, q):
    objects.append((x,y,q))

def dessiner_objets():
    for objet in objects:
        if objet[2] > 0:
            pygame.draw.circle(fenetre,ROUGE, (objet[0], objet[1]), 10)
        else:
            pygame.draw.circle(fenetre,NOIR, (objet[0], objet[1]), 10)

def dessiner_champ():
    for x in range(-50, dimensions_fenetre[0] + 100, 50):
        for y in range(-50, dimensions_fenetre[1] + 100, 50):
            vecteur = calculer_champ(x,y)

            if vecteur != None:

                norme = math.sqrt(vecteur[0]**2+vecteur[1]**2)

                if norme >= 10**(-10):
                    composante = [0, 0]

                    if vecteur[0] == 0:
                        composante = [0,40*(vecteur[1])/norme]
                    elif vecteur[1] == 0:
                        composante = [40*(vecteur[0])/norme,0]
                    else:
                        composante = [40*(vecteur[0])/norme,40*(vecteur[1])/norme]

                    x1 = x - (composante[0]/2)
                    y1 = y - (composante[1]/2)





                    v = math.sqrt(1000 * (abs(vecteur[0])+abs(vecteur[1])))
                    couleur = (0,0,0)
                    if v <= 8 and v>=0:
                        couleur = (255, 255*v/8, 0)
                    elif v <= 16 and v>8:
                        tmp = 255 * (v-8) / 8
                        couleur = (255-tmp, 255, tmp)

                    elif v <= 24 and v>16:
                        tmp = 255 * (v - 16) / 8
                        couleur = (0 , 255-tmp, 255)

                    elif v <= 32 and v>24:
                        tmp = 255 * (v-24) / 8
                        couleur = (tmp, 0, 255)
                    elif v>32:
                        couleur = (255,0,255)
                    dessiner_vecteur(fenetre,couleur,(x1,y1),composante)



def calculer_champ(x,y):
    k = 8.9876 * (10 ** 9)
    somme_champ = [0,0]

    for objet in objects:

        distance_objet = math.sqrt((objet[0] - x)**2+(objet[1] - y)**2)
        if distance_objet < 20:
            return None

        else:

            composante_vecteur = [x - objet[0], y - objet[1]]

            composante_vecteur[0] = composante_vecteur[0] * (k*objet[2])/ (distance_objet**3)
            composante_vecteur[1] = composante_vecteur[1] * (k*objet[2])/ (distance_objet**3)

            somme_champ[0] += composante_vecteur[0]
            somme_champ[1] += composante_vecteur[1]


    if somme_champ != 0:
        return somme_champ



def deplacer_pol(point, distance, orientation):
    (x, y) = point
    xf = x+(math.cos(orientation)*distance)
    yf = y+(math.sin(orientation)*distance)

    return (xf, yf)



def dessiner_vecteur(fenetre, couleur, origine, vecteur):


    if math.sqrt((vecteur[0]**2)+(vecteur[1]**2)) >= 0:
        p4 = (origine[0]+vecteur[0],origine[1]+vecteur[1])
        alpha = math.atan2(vecteur[1],vecteur[0])
        p1 = deplacer_pol(origine,A,alpha-(math.pi/2))
        p7 = deplacer_pol(origine,A,alpha+(math.pi/2))
        p2 = deplacer_pol(p1,math.sqrt((vecteur[0]**2)+(vecteur[1]**2)) - C,alpha )
        p6 = deplacer_pol(p7, math.sqrt((vecteur[0]**2)+(vecteur[1]**2)) - C, alpha)
        p3 = deplacer_pol(p2,B,alpha-(math.pi/2))
        p5 = deplacer_pol(p6, B, alpha+(math.pi/2))

        polygone = [origine,p1, p2, p3, p4, p5, p6, p7]
        pygame.draw.polygon(fenetre, couleur, polygone)

        return (p4, alpha, p1, p7, p2, p6, p3, p5)
    else :
        alpha = math.atan2(A + B, C)
        p1 = deplacer_pol(origine, C, alpha + math.pi)
        p2 = deplacer_pol(p1, A + B, alpha - (math.pi / 2))
        p3 = deplacer_pol(origine, C - math.sqrt((p1 ** 2) + (p2 ** 2)), alpha)
        p4 = deplacer_pol(p1,A+B, alpha+math.pi)

        polygone = [ p2, p3, p4]
        pygame.draw.polygon(fenetre, couleur, polygone)

        return  (alpha,p1,p2,p3,p4)

# Constantes

BLEUCLAIR = (127, 191, 255)
ROUGE = (255,0,0)
NOIR = (0,0,0)
BLEU = (0,0,255)

A = 2
B = 5
C = 20

# Paramètres

dimensions_fenetre = (1600, 900)  # en pixels
images_par_seconde = 25

# Initialisation

pygame.init()

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 1")

horloge = pygame.time.Clock()
couleur_fond = BLEUCLAIR

# Dessin

fenetre.fill(couleur_fond)

objects = []
ajouter_objet(800, 200, 10**-6)
ajouter_objet(800, 700, -10**-6)
dessiner_objets()
dessiner_champ()
while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    horloge.tick(images_par_seconde)