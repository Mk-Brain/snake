import pygame
import time
import random
import sys


clock = pygame.time.Clock()

class couleur:
    Blanc = (255, 255, 255)
    Noir = (0, 0, 0)
    Rouge = (255, 0, 0)
    Vert = (0, 255, 0)
    Bleu =(0, 0, 255)
    Jaune = (255, 255, 0)
    
color = couleur
class rectangle:
    def __init__(self, dimension = tuple(), couleur = tuple, epaisseur = int ):
        self.dimension = dimension
        self.couleur = couleur
        self.epaisseur = epaisseur
        
    def construire(self):
        pygame.draw.rect(fenetre, self.couleur, self.dimension, self.epaisseur)

class grille:
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        
    def construire(self):
        dxh, fxh = 0, self.largeur
        dyh, fyh = 0, 0
        dxv, fxv = 0, 0
        dyv, fyv = 0, self.hauteur
        
        while dyh <= self.hauteur:
            pygame.draw.line(fenetre, color.Blanc, (dxh, dyh), (fxh, fyh), 1)
            dyh += 20
            fyh += 20
        while dxv <= self.largeur :
            pygame.draw.line(fenetre, color.Blanc, (dxv, dyv), (fxv, fyv), 1)
            dxv += 20
            fxv += 20
            
class serpen:
    manger = False
    drapeau = True
    taille = [(0, 0, 20, 20)]
    rec = None
    score_actuel = int(0)
    
    def renaitre(self):
        self.taille = [(0, 0, 20, 20)]
        self.rec = None
        self.manger = False
        self.score_actuel = 0
    
    def calcul_score(self):
        if self.manger:
            self.score_actuel += 1
    
    def construire_tete(self):
        for i in range(len(self.taille)):
            if i == 0:
                self.rec = rectangle(self.taille[i], color.Vert, 0)
                self.rec.construire()
            else:
                if i % 2 == 0:
                    self.rec = rectangle(self.taille[i], color.Rouge, 0)
                    self.rec.construire()
                else:
                    self.rec = rectangle(self.taille[i], color.Bleu, 0)
                    self.rec.construire()
                
    def niveu(i):
        niv = range(10)
        return niv(i)
    
    def aller_a_gauche(self):
        
            clone = list(self.taille[0])
            clone[0] = clone[0] - 20
            clone = tuple(clone)
            #self.taille.insert(0, clone)
            if self.manger == False:
                self.taille.pop()
            self.taille.insert(0, clone)
            self.construire_tete()
                 
    def aller_a_droite(self):
        clone = list(self.taille[0])
        clone[0] = clone[0] + 20
        clone = tuple(clone)
        #self.taille.insert(0, clone)
        if self.manger == False:
            self.taille.pop()
        self.taille.insert(0, clone)
        self.construire_tete()
        
        
    def descendre(self):
        clone = list(self.taille[0])
        clone[1] = clone[1] + 20
        clone = tuple(clone)
        #self.taille.insert(0, clone)
        if self.manger == False:
            self.taille.pop()
        self.taille.insert(0, clone)
        self.construire_tete()
        
        
        
    def monter(self):
        clone = list(self.taille[0])
        clone[1] = clone[1] - 20
        clone = tuple(clone)
        #self.taille.insert(0, clone)
        if self.manger == False:
            self.taille.pop()
        self.taille.insert(0, clone)
        self.construire_tete()
        
                            
                    
class pomme:
    couleur = color.Jaune
    def __init__(self, px, py):
        self.px = px
        self.py = py
    
    def construire(self):
        pygame.draw.circle(fenetre, self.couleur, (self.px, self.py), 10)    
       
def initialiser():
    v1 = (random.randint(0, 30) * 2 + 1) * 10
    v2 = (random.randint(0, 20) * 2 + 1) * 10
    px = v1 if v1 < 600 else 590
    py = v2 if v2 < 400 else 390
    return [px, py]    
                
        
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("snake")
fenetre = pygame.display.set_mode((600,600))
font = pygame.font.SysFont("Arial", 24)
img = pygame.image.load('melidas.jpg')
drapeau = True
direction = ["gauche", "droite", "haut", "bas"]
d = str()
coordonnee_pomme = []
pomme_mangee = True
apple = pomme(0, 0)

#etats de jeu
acceuil = 0
jeu = 1
fin = 2
pause = 3
recommencer = 4

etat_present = acceuil
snake = serpen()
niv = 4
attente = 1
score = 0
while drapeau:
    evn = pygame.event.get()

    #creation de la pomme
    if pomme_mangee:
        coordonnee_pomme = initialiser()
        apple = pomme(coordonnee_pomme[0], coordonnee_pomme[1])
        pomme_mangee = False
        
    if not attente:
        score = snake.score_actuel
    
    #condition de sortie
    for evenement in evn:
        if evenement.type == pygame.QUIT:
            drapeau = False
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_HOME:
                etat_present = acceuil
            if evenement.key == pygame.K_SPACE:
                etat_present = jeu
            if evenement.key == pygame.K_BACKSPACE:
                etat_present = pause
            if evenement.key == pygame.K_RETURN:
                etat_present = recommencer    
        #choix du niveau
            if evenement.key == pygame.K_KP1:
                niv = 4
            if evenement.key == pygame.K_KP2:
                niv = 5
            if evenement.key == pygame.K_KP3:
                niv = 6
            if evenement.key == pygame.K_KP4:
                niv = 7
            if evenement.key == pygame.K_KP5:
                niv = 8
            if evenement.key == pygame.K_KP6:
                niv = 9
    #fonctionnement
            
    if etat_present == acceuil:
        fenetre.fill(color.Noir)
        pygame.mixer_music.load('deb.mp3')
        pygame.mixer_music.play(2)
        fenetre.blit(img, (0, 0))
        
        texte1 = font.render("BIENVENUE DANS SNACKE", True, color.Blanc)
        fenetre.blit(texte1, (130, 200))
        texte2 = font.render("APPUYEZ SUR ESPACE POUR CONTINUER", True, color.Blanc)
        fenetre.blit(texte2, (55, 250))
        texte3 = font.render("Appuyez sur un chiffre pour choisir le niveau de jeu", True, color.Blanc)
        fenetre.blit(texte3, (10, 300))
        texte4 = font.render("les niveaux vont de 1 à 6 ", True, color.Blanc)
        fenetre.blit(texte4, (10, 350))
        
                
    elif etat_present == jeu:
        pygame.mixer_music.load('jeu.mp3')
        pygame.mixer_music.play(2)
        fenetre.fill(color.Noir)
        grid = grille(420, 620)
        grid.construire()
        texte1 = font.render(f"Score : {score}", True, color.Blanc)
        fenetre.blit(texte1, (0, 500))
        texte2 = font.render(f"Niveau : {niv}", True, color.Blanc)
        fenetre.blit(texte2, (300, 500))
        apple.construire()
        if attente:
            snake.construire_tete()
            
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                if d == "droite":
                    etat_present = fin
                else:
                    d = direction[0]
                
            if evenement.key == pygame.K_RIGHT:
                if d == "gauche":
                    etat_present = fin
                else:
                    d = direction[1]

            if evenement.key == pygame.K_DOWN:
                if d == "haut":
                    etat_present = fin
                else:
                    d = direction[3]

            if evenement.key == pygame.K_UP:
                if d == "bas":
                    etat_present = fin
                else:
                    d = direction[2]


        tmp = snake.taille[0]
        if d == "gauche":
            attente = 0   
            if tmp[0] == (apple.px + 10) and tmp[1] == (apple.py - 10):
                snake.manger = True
                snake.calcul_score()
                pomme_mangee = True
            snake.aller_a_gauche()
            snake.manger = False
            if tmp[0] <= 0 or tmp in snake.taille[2:]:
                etat_present = fin
                
        elif d == "droite":
            attente = 0    
            if tmp[0] + 20 == (apple.px - 10) and tmp[1] == (apple.py - 10):
                snake.manger = True
                snake.calcul_score()
                pomme_mangee = True
            snake.aller_a_droite()
            snake.manger = False
            if tmp[0] >= 600 or tmp in snake.taille[2:]:
                etat_present = fin
                
        elif d == "bas":
            attente = 0   
            if tmp[0] == (apple.px - 10) and tmp[1] + 20 == (apple.py - 10):
                snake.manger = True
                snake.calcul_score()
                
                pomme_mangee = True
            snake.descendre()
            snake.manger = False
            if tmp[1] >= 400 or tmp in snake.taille[2:]:
                etat_present = fin
            
        elif d == "haut":
            attente = 0
            if tmp[0] == (apple.px - 10) and tmp[1] == (apple.py + 10):
                snake.manger = True
                snake.calcul_score()
            
                pomme_mangee = True
            snake.monter()
            snake.manger = False
            if tmp[1] <= 0 or tmp in snake.taille[2:]:
                etat_present = fin
    
    elif etat_present == fin:
        pygame.mixer_music.load('fin.mp3')
        pygame.mixer_music.play(2)
        fenetre.fill(color.Noir)
        texte1 = font.render("YOU LOSE : ", True, color.Blanc)
        fenetre.blit(texte1, (150, 200))
        texte3 = font.render(f"SCORE : {score}", True, color.Blanc)
        fenetre.blit(texte3, (110, 250))
        texte2 = font.render("APPUYEZ SUR ESPACE POUR RECOMMENCER ", True, color.Blanc)
        fenetre.blit(texte2, (40, 300))
        d = "stop"
        attente = 1 
        snake.renaitre()
        
    elif etat_present == pause:
        #d = "stop"
        fenetre.fill(color.Noir)
        texte1 = font.render("APPUYEZ SUR ESPACE POUR CONTINUER", True, color.Blanc)
        texte2 = font.render("APPUYEZ SUR ENTRER POUR RECOMMENCER", True, color.Blanc)
        fenetre.blit(texte1, (43, 230))
        fenetre.blit(texte2, (35, 290))
        texte3 = font.render(f"SCORE ACTUEL : {score}", True, color.Blanc)
        fenetre.blit(texte3, (90, 330))
        
    elif etat_present == recommencer:
        fenetre.fill(color.Noir)
        d = "stop"
        snake.renaitre()
        etat_present = jeu 
        attente = 1 

    pygame.display.flip()
    clock.tick(niv) 
pygame.quit() 
        





