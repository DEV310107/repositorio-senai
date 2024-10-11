class Motor:
    def __init__(self, potencia, marca):
        self.potencia = potencia
        self.marca = marca

    def getpotencia (self):
        return self.potencia 
    
    def setpotencia (self, potencia):
        self.potencia = potencia

    def getmarca (self):
        return self.marca
    
    def setmarca (self, marca):
        self.marca = marca

class Roda:
    def __init__(self, tamanho, marca):
        self.tamanho = tamanho
        self.marca = marca

    def gettamanho (self):
        return self.tamanho
    
    def settamanho (self, tamanho):
        self.tamanho = tamanho

    def getmarca (self):
        return self.marca
    
    def setmarca (self, marca):
        self.marca = marca

class carro:
    def __init__(self):
        self.motor = None
        self.rodas = None

    def getmotor (self):
        return self.motor
    
    def setmotor (self, motor):
        self.motor = motor

    def getrodas (self):
        return self.rodas
    
    def setrodas (self, rodas):
        self.rodas = rodas

    
motor1 = Motor (1.5, "HONDA")
motor2 = Motor (2.0, "TOYOTA")
motor3 = Motor (1.8, "FORD")

peneu1 = Roda (16, "PIRELLI")
peneu2 = Roda (18, "MICHELIN")


carro1 = carro()
carro1.setmotor(motor1)
carro1.setrodas(peneu1)

carro2 = carro()
carro2.setmotor(motor2)
carro2.setrodas(peneu2)

carro3 = carro()
carro3.setmotor(motor3)
carro3.setrodas(peneu1)

carro4 = carro()
carro4.setmotor(motor1)
carro4.setrodas(peneu2)

carro5 = carro()
carro5.setmotor(motor2)
carro5.setrodas(peneu1)

carro6 = carro()
carro6.setmotor(motor3)
carro6.setrodas(peneu2)

carros = [carro1, carro2, carro3, carro4, carro5, carro6]

for i, carro in enumerate(carros, start=1):
    print(f"Carro {i}:")
    print(f"Marca do motor: {carro.getmotor().getmarca()}")
    print(f"Potência do motor: {carro.getmotor().getpotencia()}")
    print(f"Marca da roda: {carro.getrodas().getmarca()}")
    print(f"Tamanho da roda: {carro.getrodas().gettamanho()}")
    print("-" * 30)