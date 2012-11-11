import Classes 
import Paint


def acquisition_extinction():
    tab = {}
    manager = Classes.Manager()
    manager.addSI("food", 1)
    manager.addSI("goOut", 0.8)
    manager.addSC("light", 0.25)
    manager.addSC("sound", 0.6)
    manager.addSC("move", 0.3)
    manager.showAssociationsTitles()
    manager.showAssociations()

    myFile = open('fichier.csv', 'w')
    
    manager.exportCSVHeader( myFile )
    manager.exportCSV(myFile)
    tab = manager.createArray()
    
    for i in range(10):
        manager.trial(["light", "sound"], "food", 0)
        manager.exportCSV(myFile)
        tab = manager.exportArray(tab)
    
    for i in range(10):
        manager.trial(["light", "sound"], [], 0)
        manager.exportCSV(myFile)
        tab = manager.exportArray(tab)
    Paint.savePlot(tab, 'graph.png', True)

    myFile.close()

def masquage():
    manager = Classes.Manager()
    manager.addSI("food", 1)
    manager.addSC("light", 0.25)
    manager.addSC("sound", 0.6)

    myFile = open('fichier.csv', 'w')
    
    manager.exportCSVHeader( myFile )
    manager.exportCSV(myFile)
    
    for i in range(10):
        manager.trial(["light", "sound"], "food", 0)
        manager.exportCSV(myFile)
    for i in range(10):
        manager.trial(["light", "sound"], [], 0)
        manager.exportCSV(myFile)

    myFile.close()


acquisition_extinction()

