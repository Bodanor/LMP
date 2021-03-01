#Samuel CHARLIER
#Maxime DERAVET
#Christos Papadopoulos


import math
import pygame
import sys



#Fonctions

def retirer_objet(x,y):
    for objet in objects:
        if (objet[0] - x <= 10 and objet[0] - x > 0)and (objet[1] - y <=10 and objet[1] - y > -10):
            objects.remove(objet)

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



def dessiner_mobile(x,y,charge):
    if charge >0:
        pygame.draw.circle(fenetre, ROUGE, (x, y), 10, 4)
    if charge <0:
        pygame.draw.circle(fenetre, NOIR, (x, y), 10, 4)

def mettre_a_jour_mobile(t):
    global mobile_vx
    global mobile_vy

    force = calculer_champ(mobile_x, mobile_y)

    if force != None:
        champX, champY = force[0], force[1]

        force_coulomb_X = mobile_charge * champX
        force_coulomb_Y = mobile_charge * champY

        masse = 10**-10

        acceleration_X = force_coulomb_X / masse
        acceleration_Y = force_coulomb_Y / masse

        mobile_vx = mobile_vx + acceleration_X * t
        mobile_vy = mobile_vy + acceleration_Y * t
        print(f"Vitesse mobile : {mobile_vx} {mobile_vy}")

        position_x = mobile_x + mobile_vx * t + (acceleration_X * t **2)/2
        position_y = mobile_y + mobile_vy * t + (acceleration_Y * t ** 2) / 2
        print(f"posotions : {position_x} {position_y}")
        print("---------FIN de boucle !---------")

        return (position_x,position_y)
    else:
        mobile_est_present = False







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
pygame.display.set_caption("Programme 2")

horloge = pygame.time.Clock()
couleur_fond = BLEUCLAIR

# Dessin


objects = []
ajouter_objet(800, 200, 10**-6)
ajouter_objet(800, 700, -10**-6)


mobile_est_present = False
mobile_x = 0
mobile_y = 0

mobile_vx = 0
mobile_vy = 0



mobile_charge = 0


temps_precedent = pygame.time.get_ticks() - 10
temps_maintenant = pygame.time.get_ticks()

while True:
    temps_maintenant = pygame.time.get_ticks()
    fenetre.fill(couleur_fond)
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:

            pos = evenement.pos
            button = evenement.button

            if button == 1:
                ajouter_objet(pos[0], pos[1], 10**-7)


            if button == 3:
                ajouter_objet(pos[0], pos[1], -10**-7)

            if button == 2:
                retirer_objet(pos[0], pos[1])

        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_p:

                mobile_charge = 10**-7
                x_souris, y_souris = pygame.mouse.get_pos()

                mobile_x = x_souris
                mobile_y = y_souris

                mobile_vy = 0
                mobile_vx = 0

                mobile_est_present = True

            if evenement.key == pygame.K_n:
                mobile_charge = -(10**-7)
                x_souris, y_souris = pygame.mouse.get_pos()

                mobile_x = x_souris
                mobile_y = y_souris

                mobile_vy = 0
                mobile_vx = 0

                mobile_est_present = True

    while temps_precedent < temps_maintenant:
        t_secondes = temps_precedent / 1000
        if mobile_est_present:
            position = mettre_a_jour_mobile(t_secondes)
            if position != None:

                mobile_x, mobile_y = position[0], position[1]
            dessiner_mobile(mobile_x,mobile_y,mobile_charge)

            #dessiner_tableau()
        temps_precedent += 1

    dessiner_objets()
    dessiner_champ()
    pygame.display.flip()
    horloge.tick(images_par_seconde)
    #t = (pygame.time.get_ticks() - temps_maintenant)
    t_secondes = temps_maintenant/1000

