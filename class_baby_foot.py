# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:40:25 2019

@author: Grillet Yanis
"""
import random as rd
import math as m


# ============================================================================

class Barre():

    def __init__(self, equipe):
        self.equipe = equipe
        self.joueur = []
        self.label = []

    # =======================

    def Move_high(self, pas, ymin, ymax):
        '''
        Méthode permettant de déplacer les barres vers les y croissants d'une distance "pas", en respectant les limites ymin et ymax de déplacement des barres

        Parameters
        ----------
        pas : float

        ymin : float

        ymax : float

        @author Grillet Yanis
        '''

        for k in self.joueur:

            if (self.joueur[-1][1] + pas) < ymax:
                k[1] = k[1] + pas
                # ne pas oublier de changer l'affichage apres

    def Move_low(self, pas, ymin, ymax):
        '''
        Méthode permettant de déplacer les barres vers les y décroissants d'une distance "pas", en respectant les limites ymin et ymax de déplacement des barres

        Parameters
        ----------
        pas : float

        ymin : float

        ymax : float

        @author Grillet Yanis
        '''

        for k in self.joueur[::-1]:

            if (self.joueur[0][1] - pas) > ymin:
                k[1] = k[1] - pas

########################################################################################### #barriere entre les class
class Goal(Barre):

    def __init__(self, equipe):

        # Les coordonnées sont écrites selon le format (x,y)

        super().__init__(equipe)

        if self.equipe == 'blue':

            self.joueur = [[-70, 0]]

        elif self.equipe == 'red':

            self.joueur = [[70, 0]]


###########################################################################################        
class Defense(Barre):
    def __init__(self, equipe):

        super().__init__(equipe)

        if self.equipe == 'blue':

            self.joueur = [[-50, -25], [-50, 25]]

        elif self.equipe == 'red':

            self.joueur = [[50, -25], [50, 25]]


###########################################################################################
class Milieu(Barre):
    def __init__(self, equipe):

        super().__init__(equipe)
                                            
        if self.equipe == 'blue': 
            self.joueur = [[-10, -37.5], [-10, -12.5], [-10, 12.5], [-10, 37.5]]

        elif self.equipe == 'red':
            self.joueur = [[10, -37.5], [10, -12.5], [10, 12.5], [10, 37.5]]


###########################################################################################
class Attaque(Barre):
    def __init__(self, equipe):

        super().__init__(equipe)

        if self.equipe == 'red':
            self.joueur = [[-30, -30], [-30, 0], [-30, 30]]


        elif self.equipe == 'blue':
            self.joueur = [[30, -30], [30, 0], [30, 30]]


###########################################################################################        
class Plateau():
    def __init__(self, xmin=-75, xmax=75, ymin=-45, ymax=45):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.cage = [-10, 10]
        self.centre_des_buts_R = [70, 0]
        self.centre_des_buts_B = [-70, 0]


###########################################################################################        
class Balle():
    def __init__(self, rayon= 4, x = 0, y = 43, but_r=0,but_b=0): 
        self.rayon = rayon
        self.x = x
        self.y = y
        self.nb_but_rouge = but_r
        self.nb_but_bleu = but_b
        c = rd.randint(0, 1)
        a = rd.uniform(0.5, 1) * (-1) ** c
        b = rd.uniform(2, 3)
        u = normaliser(a, b)
        self.direction = (u[0], u[1])
        self.t = 0  # variable qui prend en compte le temps de jeux
        self.pas = 3  # on peut pas mettre une vrai valeur car on n'a pas acces au mode de difficulté
        self.compteur = 0 # pour éviter un bug du rebond
        # on ne définit pas le self.label = [] ici car sinon à chaque but, la liste redevient vide


    def vitesse_balle(self, aui):
        '''
        Méthode déterminant l'évolution de la vitesse de la balle en fonction du temps

        Parameters
        ----------
        aui : float

        @author Grillet Yanis
        '''

        self.t += 0.5  # arbitraire mais sinon l'évolution est trop rapide
        self.pas = (5 / (self.t + 1.5) + aui)



    def avancer(self, aoui):

        '''
        Méthode déterminant l'évolution de la direction de la balle, et modifiant sa vitesse

        Parameters
        ----------
        aoui : float

        @author Grillet Yanis
        '''
        self.vitesse_balle(aoui)  # qui va modifier le pas avant de calculer le potentiel prochain point

        y1 = self.direction[1] * self.pas + self.y
        x1 = self.direction[0] * self.pas + self.x

        return (x1, y1)


    def test_terrain(self, x1, y1, xmin, xmax, ymin, ymax, cage):  # Remarque tres importante: je suis obligé de faire les tests dans la class balle car sinon je ne peux pas modifier ses instances de type direction.
        '''
        Méthode déterminant l'évolution de la direction de la balle, en fonction de ses rebonds contre les limites du terrain

        Parameters
        ----------
        x1 : float

        y1 : float

        xmin : float

        xmax : float

        ymin : float

        ymax : float

        cage : liste de deux float

        @author Grillet Yanis
        '''
        if (ymin + self.rayon) > y1 or (ymax - self.rayon) < y1:  # car c'est le centre de la balle qui doit sortir d'une zone a peine plus petite
            self.direction = (self.direction[0], - self.direction[1])
            y1 = self.direction[1] * self.pas + self.y
            x1 = self.direction[0] * self.pas + self.x
            self.compteur = 0

        if (xmin + self.rayon) > x1 or (xmax - self.rayon) < x1: 
            if (cage[1] - self.rayon) < y1 and self.compteur == 0:    # cas ou la balle ne veut rentrer dans les buts
                self.direction = (- self.direction[0], self.direction[1])
                y1 = self.direction[1] * self.pas + self.y
                x1 = self.direction[0] * self.pas + self.x
                self.compteur += 1 # permet d'être sûr que la balle ne bug pas 
                
            if (cage[0] + self.rayon) > y1 and self.compteur == 0:  # cas ou la balle ne veut rentrer dans les buts
                self.direction = (- self.direction[0], self.direction[1])
                y1 = self.direction[1] * self.pas + self.y
                x1 = self.direction[0] * self.pas + self.x
                self.compteur += 1

        return (x1, y1)

    # ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == ==
    def test_barres(self, x1, y1, centredesbuts, L, cage,d = 0):
        '''
         Méthode déterminant l'évolution de la direction de la balle, en fonction de ses rebonds contre les joueurs

         Parameters
         ----------
         x1 : float

         y1 : float

         centredesbuts : liste de deux float

         L : liste de float

         cage : liste de deux float

         d : int 0 ou 2

        @author Grillet Yanis
        '''
        self.compteur = 0 
        for k in L:

            if distance(x1, y1, k[0], k[1]) < self.rayon:  # faudra changer les self.rayon et mettre une valeur en fonction de la grosseur du joueur
                l = rd.randint(0,1)
                u = rd.uniform(0, cage[1]+d)*(-1)**l
                self.direction = normaliser(centredesbuts[0] - k[0], centredesbuts[1] - k[1]+ u)
                self.t = 0  # effectue un boost de vitesse
                y1 = self.direction[1] * self.pas + self.y
                x1 = self.direction[0] * self.pas + self.x

        return (x1, y1)

    
    def détection_but(self, xmin, xmax):
        '''
        Méthode ajoutant 1 au score de l'équipe ayant marqué, et réinitialisant la position, vitesse et direction de la balle

        Parameters
        ----------
        xmin : float

        xmax : float

        @author Grillet Yanis
        '''

        if (self.x) < xmin:  # pas en fct de y car le seul cas ou la balle va si loin est le cas ou la balle n'a pas rebondi contre les murs
           # print("buuuuuuuuuuuuuuuuuuut red")
            self.nb_but_rouge += 1
            self.__init__(but_r=self.nb_but_rouge, but_b=self.nb_but_bleu) # permettra l'affichage des scores sur l'IHM

        if (self.x) > xmax:
            #print("buuuuuuuuuuuuuuuuuuut blue")
            self.nb_but_bleu += 1
            self.__init__(but_b = self.nb_but_bleu, but_r = self.nb_but_rouge)


###########################################################################################
class intelligence_Arti():

    def __init__(self, equipe='red'):
        self.equipe = equipe
        self.Nbr2coup = 0
        self.liste = ['high', 'low']



###########################################################################################            

def distance(x1, y1, x, y):
    '''Fonction calculant la distance entre deux points de coordonnées (x1,y1) et (x,y)

    parameters
    ---------

    x1 : float

    y1 : float

    x : float

    y : float

    @author Piranda Julien
    '''
    return m.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)  # pythagore quoi


# =======================z

def normaliser(x, y):
    '''Fonction calculant la distance entre deux points de coordonnées (x1,y1) et (x,y)

    parameters
    ---------

    x : float

    y : float

    @author Piranda Julien
    '''
    a = m.sqrt(x ** 2 + y ** 2)
    return (x / a, y / a)

