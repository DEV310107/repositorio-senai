class Veiculo():
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def ligar(self):
       print("LIGANDO...")

    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def getAno(self):
        return self.ano

    def getPlaca(self):
        return self.placa

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setAno(self, ano):
        self.ano = ano

    def setPlaca(self, placa):
        self.placa = placa

class Moto(Veiculo):
    def dar_grau(self):
        print("Dando grau... RAMDAMDAM")

class Carro(Veiculo):
    def cantar_pneu(self):
        print("Cantando pneu... tufff")
      