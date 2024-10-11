class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print("andando")

    def falar(self):
        print("falando")

    def SetNome (self, novo_nome):
        self.nome = novo_nome
        print(novo_nome)

    def GetNome(self):
        return self.nome
    

    