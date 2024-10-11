class Programador:
    def __init__(self,nome):
        self.nome = nome
        self.equip = None
    
    def getnome (self):
        return self.nome
    
    def setnome(self, x):
        self.nome = x
    
    def getequip(self):
        return self.equip
    
    def setequip(self, x):
        self.equip

class Equipamento:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def getmarca (self);
        return self.marca
    
    def setmarca (self, x):
        self.marca = x 
    
    def getmmodelo (self):
        return self.modelo
    
    def setmodelo (self, x):
        self.marca = x

marcos = Programador(marcos)
marcos.getequip()
#none
macbook = Equipamento (apple, air)
marcos.setequip(macbook)
#__class__ a#37*5
marcos.getequip()
marcos.getequip().getmarca()
#apple