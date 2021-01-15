from jeu import Jeu
from gameconfig import GameConfig

class jeuPurple(Jeu):

    def __init__(self):
        super().__init__()
        self.score=0
        self.controls=[
        ['rouge','/static/cards/PNG/Cards/cardBack_red5.png','tirer','0'],
        ['noir','/static/cards/PNG/Cards/cardBack_blue5.png','tirer','1'],
        #['purple','/static/cards/PNG/Cards/cardBack_green5.png','tirer','0,1'],
        ['score','/static/cards/PNG/Cards/cardBack_blue1.png','vider']]

    def update(self,moves):
        for move in moves:
            super().update(moves)
            card=self.terrain.defausse[-1].signe
            if GameConfig.signes[card] in GameConfig.couleurs[int(move)]:
                self.score+=1
            else:
                self.score=0
                break

        return [str(self.score),''.join(self.terrain.getDefausse())]