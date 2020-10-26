import unittest
from class_baby_foot import Goal, Attaque, Defense, Milieu, Balle

class TestBarres(unittest.TestCase):
    def testInit(self):
        g=Goal('blue')
        self.assertEqual(g.joueur,[[-70,0]])

        a=Attaque('red')
        self.assertEqual(a.joueur[0], [-30, -30])

    def testMove(self):
        '''
        Méthode permettant de tester la méthode move_high de la classe barre


        @author Grillet Yanis
        '''

        m=Milieu('blue')
        m1=Milieu('blue')
        m.Move_high(2,0,0)
        self.assertEqual(m.joueur,m1.joueur)
        self.assertIsNot(m,m1)

        m.Move_high(2, -60, 60)
        self.assertEqual(m.joueur[-1],[-10,39.5])


class TestBalle(unittest.TestCase):
    def testinit(self):
        b=Balle()
        self.assertIsInstance(b.nb_but_bleu,int)
        self.assertEqual(b.rayon,4)

    def testvitesse(self):
        '''
        Méthode permettant de tester la méthode vitesse_balle de la classe balle


        @author Grillet Yanis
        '''

        b1=Balle()
        b1.vitesse_balle(4)
        self.assertEqual(b1.t,0.5)
        self.assertEqual(b1.pas,(5 / (b1.t + 1.5) + 4))

    def testjoueur(self):
        '''
        Méthode permettant de tester la méthode test_barres de la classe barre


        @author Grillet Yanis
        '''

        d=Defense('blue')
        d1=d.joueur
        b2=Balle(x=4,y=30)
        (x1,y1) = (8,37)
        res = b2.test_barres(x1, y1, [-30, 25], d1, [-10,10])
        self.assertEqual((x1,y1),res)
        (x2,y2) = (-50,-25)
        res2 = b2.test_barres(x2, y2, [-30, 25], d1, [-10, 10])
        self.assertNotEqual((x2, y2), res2)


if __name__ == "__main__":
    unittest.main()