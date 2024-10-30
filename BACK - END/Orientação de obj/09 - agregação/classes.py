class Tecnico:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getnome(self):
        return self.nome
    
    def setnome(self, nome):
        self.nome = nome

    def getidade(self):
        return self.idade
    
    def setidade(self, idade):
        self.idade = idade

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def getnome(self):
        return self.nome
    
    def setnome(self, nome):
        self.nome = nome

    def getposicao(self):
        return self.posicao
    
    def setposicao(self, posicao):
        self.posicao = posicao

class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time

    def getnome_time(self):
        return self.nome_time
    
    def setnome_time(self, nome_time):
        self.nome_time = nome_time




# time 1
time1 = Time("Corintians")
tecnico1 = Tecnico("Ramon", 43)
jogador1 = Jogador("Romero", "Atacante")

# time 2
time2 = Time("Palmeiras")
tecnico2 = Tecnico("Ferreira", 30)
jogador2 = Jogador("Estevão", "Atacante")