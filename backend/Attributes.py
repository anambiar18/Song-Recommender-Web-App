class Attributes:
    def __init__(self, dancability, energy, liveness, valence, tempo) :
        self.dancability = dancability
        self.energy = energy
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo

    def getDancability(self) :
        return self.dancability
    
    def getEnergy(self) :
        return self.energy
    
    def getLiveness(self) :
        return self.liveness
    
    def getValence(self) :
        return self.valence
    
    def getTempo(self) :
        return self.tempo
    
    def setDancability(self, new_dancability) :
        self.dancability = new_dancability
    
    def setEnergy(self, new_energy) :
        self.energy = new_energy
    
    def setLiveness(self, new_liveness) :
        self.liveness = new_liveness
    
    def setValence(self, new_valence) :
        self.valence = new_valence

    def setTempo(self, new_tempo) :
        self.tempo = new_tempo