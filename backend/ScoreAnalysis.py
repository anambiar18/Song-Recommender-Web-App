import Attributes
from Attributes import *
from Model import *


def thefinalScore(text):
    scores = scoreOutput(text)
    negativeScore = scores[0]
    positiveScore = scores[2]
    finalScore = positiveScore - negativeScore
    return finalScore


def soundFeatures(finalScore) :
    sound_analysis = Attributes(0, 0, 0, 0, 0)

    if(finalScore > 0.8) :
        sound_analysis.setDancability(0.9)
        sound_analysis.setEnergy(0.9)
        sound_analysis.setValence(0.9)
        sound_analysis.setLiveness(0.9)
        sound_analysis.setTempo(150)
    elif(finalScore <= 0.8 and finalScore > 0.6) :
        sound_analysis.setDancability(0.8)
        sound_analysis.setEnergy(0.8)
        sound_analysis.setValence(0.8)
        sound_analysis.setLiveness(0.8)
        sound_analysis.setTempo(150)
    elif(finalScore <= 0.6 and finalScore > 0.4) :
        sound_analysis.setDancability(0.7)
        sound_analysis.setEnergy(0.7)
        sound_analysis.setValence(0.7)
        sound_analysis.setLiveness(0.7)
        sound_analysis.setTempo(140)
    elif(finalScore <= 0.4 and finalScore > 0.2) :
        sound_analysis.setDancability(0.6)
        sound_analysis.setEnergy(0.6)
        sound_analysis.setValence(0.6)
        sound_analysis.setLiveness(0.6)
        sound_analysis.setTempo(150)
    elif(finalScore <= 0.2 and finalScore > 0.0) :
        sound_analysis.setDancability(0.5)
        sound_analysis.setEnergy(0.5)
        sound_analysis.setValence(0.5)
        sound_analysis.setLiveness(0.5)
        sound_analysis.setTempo(150)
    elif(finalScore <= 0.0 and finalScore > -0.2) :
        sound_analysis.setDancability(0.4)
        sound_analysis.setEnergy(0.4)
        sound_analysis.setValence(0.4)
        sound_analysis.setLiveness(0.4)
        sound_analysis.setTempo(120)
    elif(finalScore <= -0.2 and finalScore > -0.4) :
        sound_analysis.setDancability(0.3)
        sound_analysis.setEnergy(0.3)
        sound_analysis.setValence(0.3)
        sound_analysis.setLiveness(0.3)
        sound_analysis.setTempo(110)
    elif(finalScore <= -0.4 and finalScore > -0.6) :
        sound_analysis.setDancability(0.2)
        sound_analysis.setEnergy(0.2)
        sound_analysis.setValence(0.2)
        sound_analysis.setLiveness(0.2)
        sound_analysis.setTempo(100)
    elif(finalScore <= -0.6 and finalScore > -0.8) :
        sound_analysis.setDancability(0.1)
        sound_analysis.setEnergy(0.1)
        sound_analysis.setValence(0.1)
        sound_analysis.setLiveness(0.1)
        sound_analysis.setTempo(90)
    elif(finalScore <= 0.8) :
        sound_analysis.setDancability(0.0)
        sound_analysis.setEnergy(0.0)
        sound_analysis.setValence(0.0)
        sound_analysis.setLiveness(0.0)
        sound_analysis.setTempo(80)

    return sound_analysis
