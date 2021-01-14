from random import shuffle
from gameconfig import GameConfig
from carte import Carte

class Terrain:

    def __init__(self):    
        self.defausse = []
        self.paquet = []
        self.trash=0
        for i in range(0,4):
            for j in range(0,13):
                self.paquet.append(Carte(j,i))
                #print('Nouvelle carte: '+self.paquet[len(self.paquet)-1].toString())
        shuffle(self.paquet)

    def tirer(self):
        self.defausse.append(self.paquet[0])
        self.paquet.pop(0)

    def getDefausse(self):
        res=[]
        for carte in self.defausse:
            res.append('<img src="/static/cards/PNG/Cards/'+carte.getTx()+'"/>')
        return res

    def viderDefausse(self):
        self.trash+=len(self.defausse)
        self.defausse=[]