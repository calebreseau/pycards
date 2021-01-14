from jeu import Jeu

class jeuPurple(Jeu):

    def __init__(self):
        super().__init__()
        self.script='purple.js'
        self.score=0
        self.controls=[
        ['rouge','/static/cards/PNG/Cards/cardBack_red5.png','tirer','1'],
        ['noir','/static/cards/PNG/Cards/cardBack_blue5.png','tirer','2'],
        ['purple','/static/cards/PNG/Cards/cardBack_green5.png','tirer','1,2'],
        ['score','/static/cards/PNG/Cards/cardBack_blue1.png','vider']]

    def update(self,moves):
        for move in moves:
            super().update(moves)
            card=self.terrain.defausse[-1].signe/2
            print(self.terrain.defausse[-1].toString())
            print(str(card)+','+move)
            if round(card)>int(move):
                ret=len(self.terrain.defausse)
            else:
                self.terrain.viderDefausse()
                ret=0

        return [str(ret),self.terrain.getDefausse()]


