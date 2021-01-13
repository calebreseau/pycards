from terrain import Terrain

class Jeu:
    def __init__(self):
        self.terrain = Terrain()
        self.end=False

    def update(self):
        if len(self.terrain.paquet)>0:
            #print('Defausse: \r\n')
            for carte in self.terrain.defausse:
                pass#print('\t\t'+carte.toString())
            #input('')
            self.terrain.tirer()
            self.end=False
            return self.terrain.getDefausse()
        else:
            self.__init__()
            return self.terrain.getDefausse()

    def stop(self):
        self.end=True
        print('Fin de la partie !')