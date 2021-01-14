from terrain import Terrain

class Jeu:
    def __init__(self):
        self.terrain = Terrain()
        self.end=False
        #self.script='refresh.js'
        self.controls=[
        ['paquet','/static/cards/PNG/Cards/cardBack_red5.png','tirer',''],
        ['trash','/static/cards/PNG/Cards/cardBack_blue5.png','vider']]
        self.msg=''

    def update(self,moves):
        if len(self.terrain.paquet)>0:
            #print('Defausse: \r\n')
            for carte in self.terrain.defausse:
                pass#print('\t\t'+carte.toString())
            #input('')
            self.terrain.tirer()
            self.end=False
        else:
            self.__init__()
        return [self.msg,self.terrain.getDefausse()]

    def stop(self):
        self.end=True
        print('Fin de la partie !')