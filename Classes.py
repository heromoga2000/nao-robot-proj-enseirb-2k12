import sys, os, re, struct, threading, time
#from xml.dom import minidom

class Manager:
    def __init__(self):
        self.sc = {}
        self.si = {}
        self.associations = {}
        self.apprentissage = 1

    def setApprentissage(self, value):
        self.apprentissage = value

    def addSI(self, nameSI, beta):
        self.si[nameSI] = beta     
        for nameSC in self.sc:
            self.associations[nameSC+"->"+nameSI] = 0.
    
    def addSC(self, nameSC, alpha):
        self.sc[nameSC] = alpha     
        for nameSI in self.si:
            self.associations[nameSC+"->"+nameSI] = 0.
    
    def showAssociationsTitles(self):
        print("Associations are :")
        for name in self.associations:
            print(name)
        
    def showAssociations(self):
        print("Associations values are :")
        for name in self.associations:
            print(name + " : " + (str)(self.associations[name]))

    def trial(self, givenSC, givenSI, graphical = 0): #givenSC est une liste
        delta = 0.
        lambd = 0.

        tmp = {}
        for nameSI in self.si:
            tmp[nameSI]=0
            for nameSC in givenSC:
                tmp[nameSI] += self.associations[nameSC+"->"+nameSI]

        for nameSC in givenSC:
            for nameSI in self.si:
                if(nameSI == givenSI):
                    lambd = 1.
                else:
                    lambd = 0.

                delta = self.sc[nameSC] * self.si[nameSI] * (lambd - tmp[nameSI])
                self.associations[nameSC+"->"+nameSI] += delta

        if(graphical):
            self.showAssociations()
            

    def exportCSV(self, myFile):
        tmp = ''
        for name in self.associations:
            tmp += (str)(self.associations[name])+';'
        myFile.write(tmp+'\n')
        


def acquisition_extinction():
    manager = Manager()
    manager.addSI("food", 1)
    manager.addSI("goOut", 0.8)
    manager.addSC("light", 0.25)
    manager.addSC("sound", 0.6)
    manager.addSC("move", 0.3)
    manager.showAssociationsTitles()
    manager.showAssociations()

    myFile = open('fichier.csv', 'w')
    tmp = ''
    for name in manager.associations:
        tmp += name+';'
    myFile.write(tmp+'\n')

    manager.exportCSV(myFile)
    for i in range(10):
        manager.trial(["light", "sound"], "food", 0)
        manager.exportCSV(myFile)
    for i in range(10):
        manager.trial(["light", "sound"], [], 0)
        manager.exportCSV(myFile)

    myFile.close()

def masquage():
    manager = Manager()
    manager.addSI("food", 1)
    manager.addSC("light", 0.25)
    manager.addSC("sound", 0.6)

    myFile = open('fichier.csv', 'w')
    tmp = ''
    for name in manager.associations:
        tmp += name+';'
    myFile.write(tmp+'\n')

    manager.exportCSV(myFile)
    for i in range(10):
        manager.trial(["light", "sound"], "food", 0)
        manager.exportCSV(myFile)
    for i in range(10):
        manager.trial(["light", "sound"], [], 0)
        manager.exportCSV(myFile)

    myFile.close()


acquisition_extinction()
