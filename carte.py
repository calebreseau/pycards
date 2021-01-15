from gameconfig import GameConfig

class Carte:



    def __init__(self,valeur,signe):
        self.valeur=valeur
        self.signe=signe

    def toString(self):
        return GameConfig.cartes[self.valeur]+' de '+GameConfig.signes[self.signe]

    def getTx(self):
        return 'card'+GameConfig.en_signes[self.signe]+GameConfig.en_cartes[self.valeur]+'.png'
        
