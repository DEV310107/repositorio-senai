class Animal:
    def mover(self):
        return "se move"
    
class Cachorro (Animal):
    def mover (self):
        return "se move com quatro patas"
    
class Peixe (Animal):
    def mover (self):
        return "nada"
    
class Lesma (Animal):
    pass

animal = Animal
cachorro = Cachorro
peixe = Peixe
lesma = Lesma

animal.mover()
#se move
cachorro.mover()
#se move com 4 patas
peixe.mover()
#nada
lesma.mover()
#se move