# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:50:06 2019

@author: Julien Piranda
"""
#========================================================
# Fichier permettant de définir toutes les images
#========================================================

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import random as rd

###############################################################################

def création_des_labels(nom, nbr, liste, photo):  # fonction permettant un set up des images automatisé
    '''
    fonction permettant d'écrire le code d'initialisation des labels pour les images "meme" automatiquement dans un fichier .txt

    parameters
    ----------

    nom : str
    nbr : float
    liste : str
    photo : str

    @author Piranda Julien
    '''

    f = open('Ecriture des labels.txt', 'w')

    for k in range(nbr):
        f.write('label_' + nom + str(k) + ' = QLabel(self) \n')
        f.write('pixmap_' + nom + str(k) + " = QPixmap(\'IHM/" + photo + str(k) + '.GIF\')\n')
        f.write('label_' + nom + str(k) + '.setPixmap(pixmap_' + nom + str(k) + ') \n')
        f.write('label_' + nom + str(k) + '.resize(pixmap_' + nom + str(k) + '.width(),pixmap_' + nom + str(
            k) + '.height())\n')
        f.write('label_' + nom + str(k) + '.move(-500,-500)\n')
        f.write('self.' + liste + '.append(label_' + nom + str(k) + ')\n')
        f.write('\n')
        f.write('\n')

    f.close()


#création_des_labels('Meme',22,'Memes_label','Meme')
###############################################################################

def définition_des_images(self,AI_2,terrain_choisi,balle_choisie):
    '''
    fonction initialisant l'affichage des images sur une fenêtre ouvert avec PyQt5

    parameters
    ----------

    AI_2 : bool
    terrain_choisi : int entre 0 et 5
    balle_choisi : int entre 0 et 4

    @author Piranda Julien
    '''

    label_1 = QLabel(self)
    pixmap_1 = QPixmap('IHM/1.GIF')
    label_1.setPixmap(pixmap_1)
    label_1.move(-500, -500)
    self.ini_label.append(label_1)
    
    label_2 = QLabel(self)
    pixmap_2 = QPixmap('IHM/2.GIF')
    label_2.setPixmap(pixmap_2)
    label_2.move(-500, -500)
    self.ini_label.append(label_2)
    
    label_3 = QLabel(self)
    pixmap_3 = QPixmap('IHM/3.GIF')
    label_3.setPixmap(pixmap_3)
    label_3.move(-500, -500)
    self.ini_label.append(label_3)
    
    # ============================================================
    label_But_1 = QLabel(self)
    pixmap_But_1 = QPixmap('IHM/goal.GIF')
    label_But_1.setPixmap(pixmap_But_1)
    label_But_1.resize(pixmap_But_1.width(), pixmap_But_1.height())
    label_But_1.move(-500, -500)
    self.but_label.append(label_But_1)
    
    label_But_2 = QLabel(self)
    pixmap_But_2 = QPixmap('IHM/goal.GIF')
    label_But_2.setPixmap(pixmap_But_2)
    label_But_2.resize(pixmap_But_2.width(), pixmap_But_2.height())
    label_But_2.move(-500, -500)
    self.but_label.append(label_But_2)
    
    label_But_3 = QLabel(self)
    pixmap_But_3 = QPixmap('IHM/goal.GIF')
    label_But_3.setPixmap(pixmap_But_3)
    label_But_3.resize(pixmap_But_3.width(), pixmap_But_3.height())
    label_But_3.move(-500, -500)
    self.but_label.append(label_But_3)
    
    label_But_4 = QLabel(self)
    pixmap_But_4 = QPixmap('IHM/goal.GIF')
    label_But_4.setPixmap(pixmap_But_4)
    label_But_4.resize(pixmap_But_4.width(), pixmap_But_4.height())
    label_But_4.move(-500, -500)
    self.but_label.append(label_But_4)
    
    label_But_5 = QLabel(self)
    pixmap_But_5 = QPixmap('IHM/goal.GIF')
    label_But_5.setPixmap(pixmap_But_5)
    label_But_5.resize(pixmap_But_5.width(), pixmap_But_5.height())
    label_But_5.move(-500, -500)
    self.but_label.append(label_But_5)
    
    label_But_6 = QLabel(self)
    pixmap_But_6 = QPixmap('IHM/goal.GIF')
    label_But_6.setPixmap(pixmap_But_6)
    label_But_6.resize(pixmap_But_6.width(), pixmap_But_6.height())
    label_But_6.move(-500, -500)
    self.but_label.append(label_But_6)
    
    # ============================================================
    # faire attention a l'ordre d'appartition des images


    label_terrain = QLabel(self)
    pixmap_terrain = QPixmap(self.liste_terrain[terrain_choisi])
    label_terrain.setPixmap(pixmap_terrain)
    self.taille_terrain = [pixmap_terrain.width(), pixmap_terrain.height()]
    label_terrain.resize(self.taille_terrain[0],self.taille_terrain[1])
    label_terrain.move(80, 190 - 15)
        
    # ============================================================
    
    label_barre_att_R_1 = QLabel(self)
    pixmap_barre_att_R_1 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_att_R_1.setPixmap(pixmap_barre_att_R_1)
    label_barre_att_R_1.resize(pixmap_barre_att_R_1.width(),pixmap_barre_att_R_1.height())
    self.barre_att_R.label.append(label_barre_att_R_1)
    
    label_barre_att_R_2 = QLabel(self)
    pixmap_barre_att_R_2 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_att_R_2.setPixmap(pixmap_barre_att_R_2)
    label_barre_att_R_2.resize(pixmap_barre_att_R_2.width(),pixmap_barre_att_R_2.height())
    self.barre_att_R.label.append(label_barre_att_R_2)
    
    label_barre_att_R_3 = QLabel(self)
    pixmap_barre_att_R_3 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_att_R_3.setPixmap(pixmap_barre_att_R_3)
    label_barre_att_R_3.resize(pixmap_barre_att_R_3.width(),pixmap_barre_att_R_3.height())
    self.barre_att_R.label.append(label_barre_att_R_3)
      
    # == = == = == == = == = == = == = == = == = == =
    
    label_barre_mil_R_1 = QLabel(self)
    pixmap_barre_mil_R_1 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_mil_R_1.setPixmap(pixmap_barre_mil_R_1)
    label_barre_mil_R_1.resize(pixmap_barre_mil_R_1.width(),pixmap_barre_mil_R_1.height())
    self.barre_mil_R.label.append(label_barre_mil_R_1)
    
    label_barre_mil_R_2 = QLabel(self)
    pixmap_barre_mil_R_2 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_mil_R_2.setPixmap(pixmap_barre_mil_R_2)
    label_barre_mil_R_2.resize(pixmap_barre_mil_R_2.width(),pixmap_barre_mil_R_2.height())
    self.barre_mil_R.label.append(label_barre_mil_R_2)
    
    label_barre_mil_R_3 = QLabel(self)
    pixmap_barre_mil_R_3 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_mil_R_3.setPixmap(pixmap_barre_mil_R_3)
    label_barre_mil_R_3.resize(pixmap_barre_mil_R_3.width(),pixmap_barre_mil_R_3.height())
    self.barre_mil_R.label.append(label_barre_mil_R_3)
    
    label_barre_mil_R_4 = QLabel(self)
    pixmap_barre_mil_R_4 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_mil_R_4.setPixmap(pixmap_barre_mil_R_4)
    label_barre_mil_R_4.resize(pixmap_barre_mil_R_4.width(),pixmap_barre_mil_R_4.height())
    self.barre_mil_R.label.append(label_barre_mil_R_4)  
    
    # == = == = == == = == = == = == = == = == = == =
    
    label_barre_def_R_1 = QLabel(self)
    pixmap_barre_def_R_1 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_def_R_1.setPixmap(pixmap_barre_def_R_1)
    label_barre_def_R_1.resize(pixmap_barre_def_R_1.width(),pixmap_barre_def_R_1.height())
    self.barre_def_R.label.append(label_barre_def_R_1)
    
    label_barre_def_R_2 = QLabel(self)
    pixmap_barre_def_R_2 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_def_R_2.setPixmap(pixmap_barre_def_R_2)
    label_barre_def_R_2.resize(pixmap_barre_def_R_2.width(),pixmap_barre_def_R_2.height())
    self.barre_def_R.label.append(label_barre_def_R_2)   
    
    # == = == = == == = == = == = == = == = == = == =
    
    label_barre_goal_R_1 = QLabel(self)
    pixmap_barre_goal_R_1 = QPixmap('IHM/joueur rouge.GIF')
    label_barre_goal_R_1.setPixmap(pixmap_barre_goal_R_1)
    label_barre_goal_R_1.resize(pixmap_barre_goal_R_1.width(),pixmap_barre_goal_R_1.height())
    self.barre_goal_R.label.append(label_barre_goal_R_1)   
    
    # ============================================================
    
    label_barre_att_B_1 = QLabel(self)
    pixmap_barre_att_B_1 = QPixmap('IHM/joueur bleu.GIF')
    label_barre_att_B_1.setPixmap(pixmap_barre_att_B_1)
    label_barre_att_B_1.resize(pixmap_barre_att_B_1.width(),pixmap_barre_att_B_1.height())
    self.barre_att_B.label.append(label_barre_att_B_1)
    
    label_barre_att_B_2 = QLabel(self)
    pixmap_barre_att_B_2 = QPixmap('IHM/joueur bleu.GIF')
    label_barre_att_B_2.setPixmap(pixmap_barre_att_B_2)
    label_barre_att_B_2.resize(pixmap_barre_att_B_2.width(),pixmap_barre_att_B_2.height())
    self.barre_att_B.label.append(label_barre_att_B_2)
    
    label_barre_att_B_3 = QLabel(self)
    pixmap_barre_att_B_3 = QPixmap('IHM/joueur bleu.GIF')
    label_barre_att_B_3.setPixmap(pixmap_barre_att_B_3)
    label_barre_att_B_3.resize(pixmap_barre_att_B_3.width(),pixmap_barre_att_B_3.height())
    self.barre_att_B.label.append(label_barre_att_B_3)  
    
    # == = == = == == = == = == = == = == = == = == =
    
    label_mil_B_1 = QLabel(self)
    pixmap_mil_B_1 = QPixmap('IHM/joueur bleu.GIF')
    label_mil_B_1.setPixmap(pixmap_mil_B_1)
    label_mil_B_1.resize(pixmap_mil_B_1.width(),pixmap_mil_B_1.height())
    self.barre_mil_B.label.append(label_mil_B_1)
    
    label_mil_B_2 = QLabel(self)
    pixmap_mil_B_2 = QPixmap('IHM/joueur bleu.GIF')
    label_mil_B_2.setPixmap(pixmap_mil_B_2)
    label_mil_B_2.resize(pixmap_mil_B_2.width(),pixmap_mil_B_2.height())
    self.barre_mil_B.label.append(label_mil_B_2)
    
    label_mil_B_3 = QLabel(self)
    pixmap_mil_B_3 = QPixmap('IHM/joueur bleu.GIF')
    label_mil_B_3.setPixmap(pixmap_mil_B_3)
    label_mil_B_3.resize(pixmap_mil_B_3.width(),pixmap_mil_B_3.height())
    self.barre_mil_B.label.append(label_mil_B_3)
    
    label_mil_B_4 = QLabel(self)
    pixmap_mil_B_4 = QPixmap('IHM/joueur bleu.GIF')
    label_mil_B_4.setPixmap(pixmap_mil_B_4)
    label_mil_B_4.resize(pixmap_mil_B_4.width(),pixmap_mil_B_4.height())
    self.barre_mil_B.label.append(label_mil_B_4)
    
    # == = == = == == = == = == = == = == = == = == =
    
    label_def_B_1 = QLabel(self)
    pixmap_def_B_1 = QPixmap('IHM/joueur bleu.GIF')
    label_def_B_1.setPixmap(pixmap_def_B_1)
    label_def_B_1.resize(pixmap_def_B_1.width(),pixmap_def_B_1.height())
    self.barre_def_B.label.append(label_def_B_1)
    
    label_def_B_2 = QLabel(self)
    pixmap_def_B_2 = QPixmap('IHM/joueur bleu.GIF')
    label_def_B_2.setPixmap(pixmap_def_B_2)
    label_def_B_2.resize(pixmap_def_B_2.width(),pixmap_def_B_2.height())
    self.barre_def_B.label.append(label_def_B_2)   
    
    # == = == = == == = == = == = == = == = == = == =
    
    label_goal_B_1 = QLabel(self)
    pixmap_goal_B_1 = QPixmap('IHM/joueur bleu.GIF')
    label_goal_B_1.setPixmap(pixmap_goal_B_1)
    label_goal_B_1.resize(pixmap_goal_B_1.width(),pixmap_goal_B_1.height())
    self.taille_image_joueur = [pixmap_goal_B_1.width(), pixmap_goal_B_1.height()] # pour pouvoir recentrer limage
    self.barre_goal_B.label.append(label_goal_B_1)
   
    # ============================================================
    
    label_balleu = QLabel(self)
    pixmap_balleu = QPixmap(self.liste_ballon[balle_choisie])
    label_balleu.setPixmap(pixmap_balleu)
    label_balleu.resize(pixmap_balleu.width(),pixmap_balleu.height())
    self.taille_image_balle = [pixmap_balleu.width(), pixmap_balleu.height()]
    self.balle_label.append(label_balleu)
    
    # ============================================================
    
    if AI_2 == True:
        label_robots = QLabel(self)
        pixmap_robots = QPixmap('IHM/robot_vs_robot2.GIF')
        label_robots.setPixmap(pixmap_robots)
        label_robots.resize(pixmap_robots.width(),pixmap_robots.height())
        label_robots.move( 80 + self.taille_terrain[0]/2  - pixmap_robots.width()/2 , 190 + self.taille_terrain[1] - 8)            

    # ============================================================
    
    label_StickMan0 = QLabel(self)
    pixmap_StickMan0 = QPixmap(self.liste_StickMan[0])
    label_StickMan0.setPixmap(pixmap_StickMan0)
    label_StickMan0.resize(pixmap_StickMan0.width(),pixmap_StickMan0.height())
    self.StickMan_label.append(label_StickMan0)
    
    label_StickMan1 = QLabel(self)
    pixmap_StickMan1 = QPixmap(self.liste_StickMan[1])
    label_StickMan1.setPixmap(pixmap_StickMan1)
    label_StickMan1.resize(pixmap_StickMan1.width(),pixmap_StickMan1.height())
    self.StickMan_label.append(label_StickMan1)
    
    label_StickMan2 = QLabel(self)
    pixmap_StickMan2 = QPixmap(self.liste_StickMan[2])
    label_StickMan2.setPixmap(pixmap_StickMan2)
    label_StickMan2.resize(pixmap_StickMan2.width(),pixmap_StickMan2.height())
    self.StickMan_label.append(label_StickMan2)
    
    label_StickMan3 = QLabel(self)
    pixmap_StickMan3 = QPixmap(self.liste_StickMan[3])
    label_StickMan3.setPixmap(pixmap_StickMan3)
    label_StickMan3.resize(pixmap_StickMan3.width(),pixmap_StickMan3.height())
    self.StickMan_label.append(label_StickMan3)
    
    label_StickMan4 = QLabel(self)
    pixmap_StickMan4 = QPixmap(self.liste_StickMan[4])
    label_StickMan4.setPixmap(pixmap_StickMan4)
    label_StickMan4.resize(pixmap_StickMan4.width(),pixmap_StickMan4.height())
    self.StickMan_label.append(label_StickMan4)
    
    label_StickMan5 = QLabel(self)
    pixmap_StickMan5 = QPixmap(self.liste_StickMan[5])
    label_StickMan5.setPixmap(pixmap_StickMan5)
    label_StickMan5.resize(pixmap_StickMan5.width(),pixmap_StickMan5.height())
    self.StickMan_label.append(label_StickMan5)
    
    label_StickMan6 = QLabel(self)
    pixmap_StickMan6 = QPixmap(self.liste_StickMan[6])
    label_StickMan6.setPixmap(pixmap_StickMan6)
    label_StickMan6.resize(pixmap_StickMan6.width(),pixmap_StickMan6.height())
    self.StickMan_label.append(label_StickMan6)
    
    label_StickMan7 = QLabel(self)
    pixmap_StickMan7 = QPixmap(self.liste_StickMan[7])
    label_StickMan7.setPixmap(pixmap_StickMan7)
    label_StickMan7.resize(pixmap_StickMan7.width(),pixmap_StickMan7.height())
    self.StickMan_label.append(label_StickMan7)
    
    for k in self.StickMan_label:
        k.move(-500,-500) 
    
    #============================================================
    
    label_Meme0 = QLabel(self) 
    pixmap_Meme0 = QPixmap('IHM/Meme0.GIF')
    label_Meme0.setPixmap(pixmap_Meme0) 
    label_Meme0.resize(pixmap_Meme0.width(),pixmap_Meme0.height())
    label_Meme0.move(-500,-500)
    self.Memes_label.append(label_Meme0)    
    
    label_Meme1 = QLabel(self) 
    pixmap_Meme1 = QPixmap('IHM/Meme1.GIF')
    label_Meme1.setPixmap(pixmap_Meme1) 
    label_Meme1.resize(pixmap_Meme1.width(),pixmap_Meme1.height())
    label_Meme1.move(-500,-500)
    self.Memes_label.append(label_Meme1)    
    
    label_Meme2 = QLabel(self) 
    pixmap_Meme2 = QPixmap('IHM/Meme2.GIF')
    label_Meme2.setPixmap(pixmap_Meme2) 
    label_Meme2.resize(pixmap_Meme2.width(),pixmap_Meme2.height())
    label_Meme2.move(-500,-500)
    self.Memes_label.append(label_Meme2)    
    
    label_Meme3 = QLabel(self) 
    pixmap_Meme3 = QPixmap('IHM/Meme3.GIF')
    label_Meme3.setPixmap(pixmap_Meme3) 
    label_Meme3.resize(pixmap_Meme3.width(),pixmap_Meme3.height())
    label_Meme3.move(-500,-500)
    self.Memes_label.append(label_Meme3)    
    
    label_Meme4 = QLabel(self) 
    pixmap_Meme4 = QPixmap('IHM/Meme4.GIF')
    label_Meme4.setPixmap(pixmap_Meme4) 
    label_Meme4.resize(pixmap_Meme4.width(),pixmap_Meme4.height())
    label_Meme4.move(-500,-500)
    self.Memes_label.append(label_Meme4)    
    
    label_Meme5 = QLabel(self) 
    pixmap_Meme5 = QPixmap('IHM/Meme5.GIF')
    label_Meme5.setPixmap(pixmap_Meme5) 
    label_Meme5.resize(pixmap_Meme5.width(),pixmap_Meme5.height())
    label_Meme5.move(-500,-500)
    self.Memes_label.append(label_Meme5)
        
    label_Meme6 = QLabel(self) 
    pixmap_Meme6 = QPixmap('IHM/Meme6.GIF')
    label_Meme6.setPixmap(pixmap_Meme6) 
    label_Meme6.resize(pixmap_Meme6.width(),pixmap_Meme6.height())
    label_Meme6.move(-500,-500)
    self.Memes_label.append(label_Meme6)    
    
    label_Meme7 = QLabel(self) 
    pixmap_Meme7 = QPixmap('IHM/Meme7.GIF')
    label_Meme7.setPixmap(pixmap_Meme7) 
    label_Meme7.resize(pixmap_Meme7.width(),pixmap_Meme7.height())
    label_Meme7.move(-500,-500)
    self.Memes_label.append(label_Meme7)
        
    label_Meme8 = QLabel(self) 
    pixmap_Meme8 = QPixmap('IHM/Meme8.GIF')
    label_Meme8.setPixmap(pixmap_Meme8) 
    label_Meme8.resize(pixmap_Meme8.width(),pixmap_Meme8.height())
    label_Meme8.move(-500,-500)
    self.Memes_label.append(label_Meme8)    
    
    label_Meme9 = QLabel(self) 
    pixmap_Meme9 = QPixmap('IHM/Meme9.GIF')
    label_Meme9.setPixmap(pixmap_Meme9) 
    label_Meme9.resize(pixmap_Meme9.width(),pixmap_Meme9.height())
    label_Meme9.move(-500,-500)
    self.Memes_label.append(label_Meme9)    
    
    label_Meme10 = QLabel(self) 
    pixmap_Meme10 = QPixmap('IHM/Meme10.GIF')
    label_Meme10.setPixmap(pixmap_Meme10) 
    label_Meme10.resize(pixmap_Meme10.width(),pixmap_Meme10.height())
    label_Meme10.move(-500,-500)
    self.Memes_label.append(label_Meme10)    
    
    label_Meme11 = QLabel(self) 
    pixmap_Meme11 = QPixmap('IHM/Meme11.GIF')
    label_Meme11.setPixmap(pixmap_Meme11) 
    label_Meme11.resize(pixmap_Meme11.width(),pixmap_Meme11.height())
    label_Meme11.move(-500,-500)
    self.Memes_label.append(label_Meme11)
        
    label_Meme12 = QLabel(self) 
    pixmap_Meme12 = QPixmap('IHM/Meme12.GIF')
    label_Meme12.setPixmap(pixmap_Meme12) 
    label_Meme12.resize(pixmap_Meme12.width(),pixmap_Meme12.height())
    label_Meme12.move(-500,-500)
    self.Memes_label.append(label_Meme12)
        
    label_Meme13 = QLabel(self) 
    pixmap_Meme13 = QPixmap('IHM/Meme13.GIF')
    label_Meme13.setPixmap(pixmap_Meme13) 
    label_Meme13.resize(pixmap_Meme13.width(),pixmap_Meme13.height())
    label_Meme13.move(-500,-500)
    self.Memes_label.append(label_Meme13)
        
    label_Meme14 = QLabel(self) 
    pixmap_Meme14 = QPixmap('IHM/Meme14.GIF')
    label_Meme14.setPixmap(pixmap_Meme14) 
    label_Meme14.resize(pixmap_Meme14.width(),pixmap_Meme14.height())
    label_Meme14.move(-500,-500)
    self.Memes_label.append(label_Meme14)
        
    label_Meme15 = QLabel(self) 
    pixmap_Meme15 = QPixmap('IHM/Meme15.GIF')
    label_Meme15.setPixmap(pixmap_Meme15) 
    label_Meme15.resize(pixmap_Meme15.width(),pixmap_Meme15.height())
    label_Meme15.move(-500,-500)
    self.Memes_label.append(label_Meme15)    
    
    label_Meme16 = QLabel(self) 
    pixmap_Meme16 = QPixmap('IHM/Meme16.GIF')
    label_Meme16.setPixmap(pixmap_Meme16) 
    label_Meme16.resize(pixmap_Meme16.width(),pixmap_Meme16.height())
    label_Meme16.move(-500,-500)
    self.Memes_label.append(label_Meme16)
        
    label_Meme17 = QLabel(self) 
    pixmap_Meme17 = QPixmap('IHM/Meme17.GIF')
    label_Meme17.setPixmap(pixmap_Meme17) 
    label_Meme17.resize(pixmap_Meme17.width(),pixmap_Meme17.height())
    label_Meme17.move(-500,-500)
    self.Memes_label.append(label_Meme17)
        
    label_Meme18 = QLabel(self) 
    pixmap_Meme18 = QPixmap('IHM/Meme18.GIF')
    label_Meme18.setPixmap(pixmap_Meme18) 
    label_Meme18.resize(pixmap_Meme18.width(),pixmap_Meme18.height())
    label_Meme18.move(-500,-500)
    self.Memes_label.append(label_Meme18)    
    
    label_Meme19 = QLabel(self) 
    pixmap_Meme19 = QPixmap('IHM/Meme19.GIF')
    label_Meme19.setPixmap(pixmap_Meme19) 
    label_Meme19.resize(pixmap_Meme19.width(),pixmap_Meme19.height())
    label_Meme19.move(-500,-500)
    self.Memes_label.append(label_Meme19)    
    
    label_Meme20 = QLabel(self) 
    pixmap_Meme20 = QPixmap('IHM/Meme20.GIF')
    label_Meme20.setPixmap(pixmap_Meme20) 
    label_Meme20.resize(pixmap_Meme20.width(),pixmap_Meme20.height())
    label_Meme20.move(-500,-500)
    self.Memes_label.append(label_Meme20)    
    
    label_Meme21 = QLabel(self) 
    pixmap_Meme21 = QPixmap('IHM/Meme21.GIF')
    label_Meme21.setPixmap(pixmap_Meme21) 
    label_Meme21.resize(pixmap_Meme21.width(),pixmap_Meme21.height())
    label_Meme21.move(-500,-500)
    self.Memes_label.append(label_Meme21)
        
    label_Meme22 = QLabel(self) 
    pixmap_Meme22 = QPixmap('IHM/Meme22.GIF')
    label_Meme22.setPixmap(pixmap_Meme22) 
    label_Meme22.resize(pixmap_Meme22.width(),pixmap_Meme22.height())
    label_Meme22.move(-500,-500)
    self.Memes_label.append(label_Meme22)
    
    
###############################################################################     

def selection_memes(self): #au numero 16 on passe à des memes plus agressifs
    # dans cette fct on va utiliser la liste self.liste_Memes_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
    # Sachant qu'il y a plusieurs 0 afin d'avoir une plus grande chance de tirer le meme n°0 correspondant au cas d'égalité
    '''
    fonction permettant de choisir le meme à afficher lors d'un but


    @author Piranda Julien
    '''

    self.meme_aff = rd.randint( 1 + 8 , 16 + 8) # du meme1 au meme16 ( célébrations classiques )
    
    if (self.diff_buts_entre_équipe > 5) and (self.equipe_vient_marquer == 'rouge'): # cas d'un but rouge lorsque les rouges mènent de + de 5 buts
        self.meme_aff = rd.randint(17 + 8 ,30) # du meme17 au meme 22 ( memes plus agressifs et moqueurs)
        
    if (self.diff_buts_entre_équipe < -5) and (self.equipe_vient_marquer == 'bleu'): # cas d'un but bleu lorsque les rouges mènent de + de 5 buts
        self.meme_aff = rd.randint(16 + 8 ,30) # du meme17 au meme 22 ( memes plus agressifs et moqueurs)
        
    if self.balle.nb_but_rouge == self.balle.nb_but_bleu: # cas d'une égalité
        self.meme_aff = rd.randint(0,16 + 8) # du meme0 au meme16 avec plus de chance que le meme0 tombe (car il corespond au cette situation)
    
    affichage_memes(self)

###############################################################################

def affichage_memes(self):
    '''
    fonction affichant le meme sélectionné lors d'un but


    @author Piranda Julien
    '''

    for k in range(len(self.Memes_label)): # vérifie bien que tout les autres images ne sont pas visibles
        if k != self.liste_Memes_number[self.meme_aff]:
            self.Memes_label[k].move(-500,-500)

    if self.equipe_vient_marquer == 'bleu': # si but bleu affiche dans la zone bleu
        self.Memes_label[self.liste_Memes_number[self.meme_aff]].move(150,190 + self.taille_terrain[1] - 5)

    if self.equipe_vient_marquer == 'rouge': # si but rouge affiche dans la zone rouge
        self.Memes_label[self.liste_Memes_number[self.meme_aff]].move(150+ self.taille_terrain[0]/2,190 + self.taille_terrain[1] - 5)

###############################################################################
  
def affichage_StickMan(self):
    '''
    fonction affichant 7 images successives créant l'illusion que le stickman court, en le déplacant selon les x croissants pour le faire avancer


    @author Piranda Julien
    '''

    l = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
    if self.StickMan_x < 800:  # tant que le StickMan n'a pas traversé toute la fenêtre
        self.StickMan_label[l[self.StickMan_Compteur]].move(self.StickMan_x,190 + self.taille_terrain[1] + 15)
        self.StickMan_label[l[self.StickMan_Compteur-3]].move(-500,-500)

        self.StickMan_x += 4 # avance de 4 en 4
        self.StickMan_Compteur += 1
        
###############################################################################
        
def affichage_joueurs(self, objet): # fonction qui affiche tout les joueurs d'une barre à leur postion (x,y), objet.joueur la liste des positions ( cf class_baby_foot.py )
    '''
    fonction permettant d'afficher tous les joueurs d'une barre à leur position

    parameters
    ----------

    objet : liste de listes de deux float

    @author Piranda Julien
    '''

    for k in range(len(objet.joueur)): # parcours toute les coordonnées des joueurs d'une barre
        objet.label[k].move(573 * objet.joueur[k][0] / 150 + 80 + self.taille_terrain[0]/ 2  - self.taille_image_joueur[0]/2,
                                360 * objet.joueur[k][1] / 90 + 190 + self.taille_terrain[1] / 2 - 15 - self.taille_image_joueur[1]/2)

###############################################################################

def affichage_balle(self, objet, objet_label): # fonction qui affiche la balle à sa position (x,y)
    '''
    fonction permettant d'afficher la balle à sa position

    parameters
    ----------

    objet : classe Balle

    objet_label : liste

    @author Piranda Julien
    '''

    objet_label[0].move(573 * objet.x / 150 + 80 + self.taille_terrain[0] / 2 - self.taille_image_balle[0]/2 , 360 * objet.y / 90 + 190 + self.taille_terrain[1] / 2 - 15 - self.taille_image_balle[0]/2) 
