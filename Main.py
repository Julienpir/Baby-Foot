# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:40:46 2019

@author: HP
"""

import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLCDNumber
from PyQt5.QtGui import QIcon, QPixmap, QKeyEvent
import random as rd
from class_baby_foot import Attaque, Milieu, Defense, Goal, Balle, Plateau, intelligence_Arti 
import Set_up_pictures as Sup


# from Window import Ui_FirstWindow, Ui_ParaTouchesMutli, Ui_ParaTouchesSolo



# ==========================================================================
# ==========================================================================


class ControleWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.fond = 0
        self.balle=2

        self.ui = uic.loadUi('IHM/fen_1.ui', self)
        
        self.ui.Boutton_Solo.clicked.connect(self.solo)
        self.ui.Boutton_Multi.clicked.connect(self.multi)
        self.ui.Bouton_simuler_robots.clicked.connect(self.robots)

        self.ui.radioButton_0.clicked.connect(self.radio0)
        self.ui.radioButton_1.clicked.connect(self.radio1)
        self.ui.radioButton_2.clicked.connect(self.radio2)
        self.ui.radioButton_3.clicked.connect(self.radio3)
        self.ui.radioButton_4.clicked.connect(self.radio4)
        self.ui.radioButton_5.clicked.connect(self.radio5)
              
        self.ui.Ballon_1.clicked.connect(self.ballon1)
        self.ui.Ballon_2.clicked.connect(self.ballon2)
        self.ui.Ballon_3.clicked.connect(self.ballon3)
        self.ui.Ballon_4.clicked.connect(self.ballon4)
        self.ui.Ballon_5.clicked.connect(self.ballon5)
        
    #== == == == == == == == == == ==
    
    def ballon1(self):
        '''
        Méthode permettant de choisir la balle utilisée


        @author Grillet Yanis
        '''
        self.balle = 0

    def ballon2(self):
        '''
        Méthode permettant de choisir la balle utilisée


        @author Grillet Yanis
        '''
        self.balle = 1

    def ballon3(self):
        '''
        Méthode permettant de choisir la balle utilisée


        @author Grillet Yanis
        '''
        self.balle = 2

    def ballon4(self):
        '''
        Méthode permettant de choisir la balle utilisée


        @author Grillet Yanis
        '''
        self.balle = 3

    def ballon5(self):
        '''
        Méthode permettant de choisir la balle utilisée


        @author Grillet Yanis
        '''
        self.balle = 4
        
    #== == == == == == == == == == ==
    
    def radio0(self):
        '''
        Méthode permettant de choisir le terrain utilisée


        @author Grillet Yanis
        '''
        self.fond = 0
        
    def radio1(self):
        '''
        Méthode permettant de choisir le terrain utilisée


        @author Grillet Yanis
        '''
        self.fond = 1
       
    def radio2(self):
        '''
        Méthode permettant de choisir le terrain utilisée


        @author Grillet Yanis
        '''
        self.fond = 2     

    def radio3(self):
        '''
        Méthode permettant de choisir le terrain utilisée


        @author Grillet Yanis
        '''
        self.fond = 3
    
    def radio4(self):
        '''
        Méthode permettant de choisir le terrain utilisée


        @author Grillet Yanis
        '''
        self.fond = 4

    def radio5(self):
        '''
        Méthode permettant de choisir le terrain utilisée


        @author Grillet Yanis
        '''
        self.fond = 5

    #==========================================================================

    def solo(self):
        '''
        Méthode permettant de transmettre l'information de la balle et du terrain choisi à une variable globale, puis d'ouvrir la fenêtre des touches en Solo, et de fermer la fenêtre actuelle


        @author Grillet Yanis
        '''
        
        global terrain_choisi # choix du terrain
        terrain_choisi = self.fond # communique son choix (entre les class)
        
        global balle_choisie #choix de la balle
        balle_choisie = self.balle # communique son choix
        
        global AI_1 # une IA controle les joueurs rouges
        AI_1 = True
        
        global AI_2 # les joueurs bleus sont controlés par l'utilisateur
        AI_2 = False

        self.close()
        self.new = SoloWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()

    #==========================================================================
    
    def multi(self):
        '''
        Méthode permettant de transmettre l'information de la balle et du terrain choisi à une variable globale, puis d'ouvrir la fenêtre des touches en Multi, et de fermer la fenêtre actuelle


        @author Grillet Yanis
        '''
        
        global terrain_choisi # choix du terrain
        terrain_choisi = self.fond # communique son choix (entre les class)
        
        global balle_choisie # choix de la balle
        balle_choisie = self.balle # communique son choix
        
        global AI_1 # les joueurs bleus sont controlés par l'utilisateur n°1
        AI_1 = False
        
        global AI_2 # les joueurs bleus sont controlés par l'utilisateur n°2
        AI_2 = False

        self.close()
        self.new = MultiWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()
        
    #==========================================================================
    
    def robots(self):
        '''
        Méthode permettant de transmettre l'information de la balle et du terrain choisi à une variable globale, puis d'ouvrir la fenêtre de terrain, et de fermer la fenêtre actuelle


        @author Piranda Julien
        '''
        
        global terrain_choisi # choix du terrain
        terrain_choisi = self.fond # communique son choix (entre les class)
        
        global balle_choisie # choix de la balle
        balle_choisie = self.balle # communique son choix
        
        global AI_1 # l'IA n°1 controle les joueurs rouges
        AI_1 = True
        
        global AI_2 # l'IA n°2 controle les joueurs bleus
        AI_2 = True
        
        self.close()
        self.new = TerrainWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()
        
        
###############################################################################        

class MultiWindow(QtWidgets.QMainWindow): # fenetre des touches pour le 1 VS 1
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('IHM/fen_Touches.ui', self)
        self.ui.Bouton_Jouer.clicked.connect(self.jouer)
        self.ui.Bouton_Retour.clicked.connect(self.retour)

    def jouer(self):
        '''
        Méthode permettant d'ouvrir la fenêtre de terrain, et de fermer la fenêtre actuelle


        @author Grillet Yanis
        '''
        self.close()
        self.new = TerrainWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()

    def retour(self):
        '''
        Méthode permettant d'ouvrir la fenêtre de départ, et de fermer la fenêtre actuelle


        @author Grillet Yanis
        '''
        self.close()
        self.new = ControleWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()

###############################################################################

class SoloWindow(QtWidgets.QMainWindow): # fenetre des touches pour le 1 VS IA
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('IHM/fen_Touches2.ui', self)
        self.ui.Bouton_Jouer.clicked.connect(self.jouer)
        self.ui.Bouton_Retour.clicked.connect(self.retour)

    def jouer(self):
        '''
        Méthode permettant d'ouvrir la fenêtre de terrain, et de fermer la fenêtre actuelle


        @author Grillet Yanis
        '''
        self.close()
        self.new = TerrainWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()

    def retour(self):
        '''
        Méthode permettant d'ouvrir la fenêtre de départ, et de fermer la fenêtre actuelle


        @author Grillet Yanis
        '''
        self.close()
        self.new = ControleWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()

###############################################################################
        
class TerrainWindow(QtWidgets.QMainWindow): # fenetre principale
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('IHM/fen_terrain.ui', self)
        
        self.liste_terrain = ["IHM/terrain0.GIF", "IHM/terrain1.GIF", "IHM/terrain2.GIF", "IHM/terrain3.GIF",  "IHM/terrain4.GIF",  "IHM/terrain5.GIF"]
        self.liste_ballon = ["IHM/volley.GIF","IHM/basket.GIF","IHM/ballon.GIF","IHM/baseball.GIF","IHM/billard.GIF"]
        self.liste_StickMan = ['IHM/StickMan0','IHM/StickMan1', 'IHM/StickMan2', 'IHM/StickMan3', 'IHM/StickMan4', 'IHM/StickMan5','IHM/StickMan6','IHM/StickMan7']
                
        self.balle_label = []  # obliger de définir la liste de label ici à cause de la remise à zéro apres chaque but
        self.but_label = [] #listes des différents labels 
        self.StickMan_label = []
        self.Memes_label = []
        self.ini_label = [] # pour le 3,2,1
       
        self.liste_rayon_balle = [4,5.5,4,3,2] #le rayon n'est pas le même en fonction de la balle choisit        
        self.liste_Memes_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
        # il y a plusieurs 0 pour quil y ait pus de chance que le meme qui corresponde à l'égalité tombe face aux memes de célébration (voir Set_up_pictures)
        self.equipe_vient_marquer = 'rouge' 
        self.diff_buts_entre_équipe = 0 # initialisation de la différence des buts rouges - buts bleus
        self.meme_aff = 0 # désigne le meme à afficher ( liste_Memes_number[meme_aff] )
        
        self.StickMan_x = 755 # position en x initiale du StickMan
        self.StickMan_Compteur = 0 # variable qui désigne le StickMan à afficher (pour faire son roulement)
             
        self.clock = 0 # permet davoir une notion de temps dans ce loop
        
        self.var_but_B = 1 # variable pour détecter un but (pour pouvoir lancer l'animation)
        self.var_but_R = 1 # meme chose mais pour un but rouge
        
        self.barre_att_R = Attaque('red') #définition des objets
        self.barre_mil_R = Milieu('red')
        self.barre_def_R = Defense('red')
        self.barre_goal_R = Goal('red')
        
        self.barre_att_B = Attaque('blue')
        self.barre_mil_B = Milieu('blue')
        self.barre_def_B = Defense('blue')
        self.barre_goal_B = Goal('blue')
        
        self.plateau = Plateau()
        
        self.robot_1 = intelligence_Arti('red')
        self.robot_2 = intelligence_Arti('blue')
        
        self.balle = Balle(self.liste_rayon_balle[balle_choisie])

        self.vitesse_pas_balle = 2  # variable qui permet de gérer le pas d'avancement de la balle
        self.vitesse_joueurs = 3  # variable qui permet de gérer le pas d'avancement des joueurs
        self.défaut_tirs = 5 # variable qui permet de gérer la précision des tirs
        
        Sup.définition_des_images(self,AI_2,terrain_choisi,balle_choisie) # définit toute les images
        
        self.affichage_global_R() # affichage des joueurs Rouges dans leur position ini
        self.affichage_global_B() # affichage des joueurs Bleus dans leur position ini
        
        Sup.affichage_balle(self, self.balle, self.balle_label) # affichage de la balle
        
        self.pause = False  # variable pour mettre la simulation en pause
        self.Un_coup = True  # variable qui permet que si on appui une fois sur pause -> ca met pause, une 2eme fois -> ca remet en marche

        self.ui.Bouton_Retour.clicked.connect(self.retour)
        self.Bouton_Difficile.clicked.connect(self.niveau_de_jeu_Difficile)  # Prend en compte le niveau de jeu souhaité
        self.Bouton_Facile.clicked.connect(self.niveau_de_jeu_Facile)
        self.Bouton_Start.clicked.connect(self.Simulation)
        self.Bouton_Pause.clicked.connect(self.Simulation_Pause)
         
    #==========================================================================

    def retour(self): # reviens à la fenetre des touches
        '''
        Méthode permettant d'ouvrir la fenêtre de départ, et de fermer la fenêtre actuelle


        @author Piranda Julien
        '''
        self.close()
        self.new = ControleWindow()
        self.new.setWindowFlags(QtCore.Qt.Window)
        self.new.show()

    def niveau_de_jeu_Difficile(self):  # Mode de difficulté
        '''
        Méthode permettant de chosir la vitesse de la balle et des joueurs pour le mode de jeu difficile, et d'introduire un facteur aléatoire dans la direction des tirs


        @author Piranda Julien
        '''
        self.vitesse_pas_balle = 2.5
        self.vitesse_joueurs = 0.9
        self.défaut_tirs = 2

    def niveau_de_jeu_Facile(self):  # Mode de difficulté Facile
        '''
        Méthode permettant de chosir la vitesse de la balle et des joueurs pour le mode de jeu facile, et de supprimer le facteur aléatoire dans la direction des tirs


        @author Piranda Julien
        '''
        self.vitesse_pas_balle = 2
        self.vitesse_joueurs = 0.6
        self.défaut_tirs = 0

    def Simulation_Pause(self):
        '''
        Méthode permettant de stopper la balle pendant le jeu


        @author Piranda Julien
        '''

        if self.Un_coup == True:  # la 1ere fois ca met en pause
            self.pause = True
            self.Un_coup = False
            return ()  # court circuit

        if self.Un_coup == False:  # la 2eme fois ca eleve la pause
            self.pause = False
            self.Un_coup = True
            return ()

    def Simulation(self):
        '''
        Méthode permettant d'appeler la méthode Confirmation_Prochain_Tour automatiquement toutes les 25 ms


        @author Piranda Julien
        '''


        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Confirmation_Prochain_Tour)
        timer.start(25)
        
    #==========================================================================

    def Confirmation_Prochain_Tour(self):
        '''
        Méthode mettant à jour l'affichage des memes et des 3,2,1 de départ, et appelant la méthode Prochain_tour


        @author Piranda Julien
        '''

        
        if self.clock == 0: # Animation du 3,2,1
            self.ini_label[0].resize(300, 300)
            self.ini_label[0].move(230, -50)

        if self.clock == 20:
            self.ini_label[0].move(-500, -500)
            self.ini_label[1].resize(300, 300)
            self.ini_label[1].move(340, -50)
                       
        if self.clock == 40:
            self.ini_label[1].move(-500, -500)
            self.ini_label[2].resize(300, 300)
            self.ini_label[2].move(440, -50)

        if self.clock == 60:
            self.ini_label[2].move(-500, -500)
            

        if self.clock > 60: # commence la parti apres l'initialisation
            if self.pause == False:  # Si  on n'appui pas sur le bouton pause
                self.Prochain_Tour()
                 
        #== == == == == == == == == == 
        
        if self.clock == 1000000001: # cas ou il y a eu but
           
            self.but_label[0].move(673, 75 - 75/2 + self.taille_terrain[1]/2)     
            self.but_label[1].move(0,75 - 75/2 + self.taille_terrain[1]/2)
            self.but_label[2].move(-500, -500)     
            self.but_label[3].move(-500, -500)
            self.but_label[4].move(-500, -500)     
            self.but_label[5].move(-500, -500)
            
            if AI_2 == False: # si on est pas dans le cas robot VS robot
                Sup.affichage_memes(self) # affiche un meme
        
        if self.clock == 1000000020: 

            self.but_label[3].move(673, 175 - 75/2 + self.taille_terrain[1]/2)     
            self.but_label[2].move(0,175 - 75/2 + self.taille_terrain[1]/2)
            
            self.but_label[0].move(-500, -500)     
            self.but_label[1].move(-500, -500)
            
        if self.clock == 1000000040:
                                  
            self.but_label[4].move(673, 275 - 75/2 + self.taille_terrain[1]/2)     
            self.but_label[5].move(0, 275 - 75/2 + self.taille_terrain[1]/2)
            
            self.but_label[2].move(-500, -500)     
            self.but_label[3].move(-500, -500)
            
            
        if self.clock == 1000000060:
            
            self.but_label[4].move(-500, -500)     
            self.but_label[5].move(-500, -500)
            self.Memes_label[self.liste_Memes_number[self.meme_aff]].move(-500,-500) #enleve le meme  

        self.clock += 1
    
    #==========================================================================
    
    def Prochain_Tour(self):  # Fonction qui met à jour l'affichage de toutes les images
        '''
        Méthode mettant à jour l'affichage du stickamn, et des joueurs de chaque équipe, puis appelant la méthode avancer_la_balle, et si il y a lieu, les méthodes de fonctionnement des IA


        @author Piranda Julien
        '''
        
        Sup.affichage_StickMan(self) # affichage du StickMan à chaque tour
        
        self.affichage_global_R() # affiche des joueurs rouges à chaque tour
        self.affichage_global_B() # affiche des joueurs bleus à chaque tour
        
        if AI_1 == True:
            self.fonctionnement_robot(self.robot_1)  # met en marche l'AI
        
        
        if AI_2 == True:
            self.fonctionnement_robot(self.robot_2)  # met en marche l'AI
        
        self.avancer_la_balle()
        
    #==========================================================================    
    
    def affichage_global_R(self): # affiche toutes les barres rouges
        '''
        Méthode mettant à jour l'affichage des joueurs rouges


        @author Piranda Julien
        '''

        Sup.affichage_joueurs(self, self.barre_goal_R)
        Sup.affichage_joueurs(self, self.barre_att_R)
        Sup.affichage_joueurs(self, self.barre_mil_R)
        Sup.affichage_joueurs(self, self.barre_def_R)
        
    #== == == == == == == == == == == == == == == == == == == == == == == == ==
    
    def affichage_global_B(self): # affiche toutes les barres bleus
        '''
        Méthode mettant à jour l'affichage des joueurs bleus


        @author Piranda Julien
        '''

        Sup.affichage_joueurs(self, self.barre_goal_B)
        Sup.affichage_joueurs(self, self.barre_att_B)
        Sup.affichage_joueurs(self, self.barre_mil_B)
        Sup.affichage_joueurs(self, self.barre_def_B)
        
    #==========================================================================
    
    def fonctionnement_robot(self, objet):
        '''
        Méthode faisant bouger automatiquement les barres de l'équipe concernée

        parameters
        ----------

        objet : classe intelligence_Arti

        @author Piranda Julien
        '''

        if rd.randint(1, 3) == 3:  # une chance sur 3 de changer directement de direction

            if objet.Nbr2coup == 0:  # initialise
                objet.Nbr2coup = rd.randint(4, 8)
                objet.direction = objet.liste[rd.randint(0, 1)]  # choisit la direction

        if objet.Nbr2coup > 0:
            self.Move_the_rods(objet.equipe, objet.direction,self.vitesse_joueurs / 1.8)  # /1.8 Pour équilibrer car les evenements automatiques ont une plus grosse frq que la détection de touche
            objet.Nbr2coup -= 1
    
    #==========================================================================
    
    def avancer_la_balle(self):
        '''
        Méthode mettant à jour la position et l'affichage de la balle, en testant sa position par rapport aux limites du terrain, aux cages et aux joueurs.
        Cette méthode appelle la méthode compteurPoints


        @author Piranda Julien
        '''

        x1, y1 = self.balle.avancer(self.vitesse_pas_balle)  # on calcule le potentiel prochain point

        x1, y1 = self.balle.test_terrain(x1, y1, self.plateau.xmin, self.plateau.xmax, self.plateau.ymin,self.plateau.ymax, self.plateau.cage)  # série de test, la en fonction des limites du terrain
        
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_B, self.barre_att_R.joueur,self.plateau.cage,self.défaut_tirs)  # centre_des_buts_B car tu ties dans les buts adverses
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_B, self.barre_mil_R.joueur,self.plateau.cage,self.défaut_tirs)
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_B, self.barre_def_R.joueur,self.plateau.cage,self.défaut_tirs)
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_B, self.barre_goal_R.joueur,self.plateau.cage,self.défaut_tirs)
        
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_R, self.barre_att_B.joueur,self.plateau.cage,self.défaut_tirs)
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_R, self.barre_mil_B.joueur,self.plateau.cage,self.défaut_tirs)
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_R, self.barre_def_B.joueur,self.plateau.cage,self.défaut_tirs)
        x1, y1 = self.balle.test_barres(x1, y1, self.plateau.centre_des_buts_R, self.barre_goal_B.joueur,self.plateau.cage,self.défaut_tirs)

        self.balle.x = x1  # on change les coordonnées
        self.balle.y = y1

        self.balle.détection_but(self.plateau.xmin, self.plateau.xmax) # on regarde si il y a pas but
        self.CompteurPoints() # on met à jour l'affichage des scores

        Sup.affichage_balle(self, self.balle, self.balle_label) # repositionne l'image de la balle
        
    #==========================================================================
    
    def CompteurPoints(self):
        '''
        Méthode mettant à jour le score et la variable equipe_vient_marquer, ainsi que l'affichage du score sur l'IHM.
        Cette méthode appelle aussi la méthode selection_memes


        @author Piranda Julien
        '''
        self.diff_buts_entre_équipe = self.balle.nb_but_rouge-self.balle.nb_but_bleu 
       
        if self.balle.nb_but_rouge == self.var_but_R: #on a détecté un but rouge
            self.clock = 1000000000 # on se met en mode but dans lq fct Confirmation_Prochain_Tour
            self.var_but_R += 1 # on met a jour le prochain but rouge
            self.equipe_vient_marquer = 'rouge' # on prend en mémoire l'équipe marquante pour les memes
                
            if AI_2 == False: # pas d'affichage de meme si Robot VS Robot
                Sup.selection_memes(self)
                
        if self.balle.nb_but_bleu == self.var_but_B: #on a détecté un but bleu
            self.clock = 1000000000 # on se met en mode but dans lq fct Confirmation_Prochain_Tour
            self.var_but_B += 1 # on met a jour le prochain but bleu
            self.equipe_vient_marquer = 'bleu' # on met a jour le prochain but
            
            if AI_2 == False: # pas d'affichage de meme si Robot VS Robot
                Sup.selection_memes(self)
                
        self.Score_rouge.display(self.balle.nb_but_rouge) # Met a jour le LDC Number du score rouge
        self.Score_bleu.display(self.balle.nb_but_bleu) # Met a jour le LDC Number du score bleu

    #==========================================================================
    
    def Move_the_rods(self, Couleur, direction, a=3): #fct pour bouger la position des barres ( cf class_baby_foot.py )
        '''
        Méthode mettant à jour la position et l'affichage des joueurs


        @author Piranda Julien
        '''

        if Couleur == 'red': # bouge toutes les barres rouges
            if direction == 'high': # vers le haut

                self.barre_att_R.Move_high(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_mil_R.Move_high(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_def_R.Move_high(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_goal_R.Move_high(a, self.plateau.cage[0], self.plateau.cage[1])

            else: # vers le bas

                self.barre_att_R.Move_low(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_mil_R.Move_low(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_def_R.Move_low(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_goal_R.Move_low(a, self.plateau.cage[0], self.plateau.cage[1])

            self.affichage_global_R() # met a jour l'affichage aux nouvelles positions des barres rouges

        if Couleur == 'blue': # bouge toutes les barres bleus
            if direction == 'high': #vers le haut

                self.barre_att_B.Move_high(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_mil_B.Move_high(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_def_B.Move_high(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_goal_B.Move_high(a, self.plateau.cage[0], self.plateau.cage[1])

            else: # vers le bas

                self.barre_att_B.Move_low(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_mil_B.Move_low(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_def_B.Move_low(a, self.plateau.ymin, self.plateau.ymax)
                self.barre_goal_B.Move_low(a, self.plateau.cage[0], self.plateau.cage[1])

            self.affichage_global_B() # met a jour l'affichage aux nouvelles positions des barres bleus

    #==========================================================================    
    
    def keyPressEvent(self, event: QKeyEvent): # détection des touches du clavier
        '''
        Méthode détectant l'appui sur les touches Z,S,I,K ou V et déplaçant les joueurs, ou lançant le stickman en fonction de l'appui


        @author Grillet Yanis
        '''

        if AI_2 == False: # dans le cas ou les joueurs rouges sont controllés par l'utilisateur
            if event.key() == QtCore.Qt.Key_Z:
                self.Move_the_rods('blue', 'low', self.vitesse_joueurs)
            
            if event.key() == QtCore.Qt.Key_S:
                self.Move_the_rods('blue', 'high', self.vitesse_joueurs)

            if event.key() == QtCore.Qt.Key_V: # affiche l'animation du StickMan (Purement inutile)
                self.StickMan_x = 0
                self.StickMan_Compteur = 0
                    
        if AI_1 == False: # dans le cas ou les joueurs bleus sont controllés par l'utilisateur
            if event.key() == QtCore.Qt.Key_I:
                self.Move_the_rods('red', 'low', self.vitesse_joueurs)
                
            if event.key() == QtCore.Qt.Key_K:
                self.Move_the_rods('red', 'high', self.vitesse_joueurs)
                
           
            


# =============================================================================
if __name__ == '__main__':
# =============================================================================

    app = QtWidgets.QApplication(sys.argv) # lance pyQt
    window = ControleWindow()
    window.show()
    app.exec_()
