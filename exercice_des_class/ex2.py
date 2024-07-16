import random

class Domino:
    def __init__(self, cote1=1, cote2=1):
        self._cote1 = cote1
        self._cote2 = cote2
        self.jouer()
        print(f'\n{self.affiche_points()}\n')
        print(f'\n{self.somme_points()}\n')
        
    def jouer(self):
        self._cote1 = random.randrange(1,7)
        self._cote2 = random.randrange(1,7)
        
    def affiche_points(self):
        return f'Premier domino : {self._cote1} points\nDeuxieme domino : {self._cote2} points'
    
    def somme_points(self):
        return f'Votre score est {self._cote1 + self._cote2} points'

a = Domino()
