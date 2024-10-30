class Cachorro():
    def __init__(self, nome, idade, raca, dono, procedimento_medico):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.dono = dono
        self.procedimento_medico = procedimento_medico

    def getnome(self):
        return self.nome
    
    def setnome(self, novo_nome):
        self.nome = novo_nome
    
    def getidade(self):
        return self.idade
    
    def setidade(self, nova_idade):
        self.nome = nova_idade

    def getraca(self):
        return self.raca
    
    def setraca(self, nova_raca):
        self.raca = nova_raca

    def getdono(self):
        return self.dono
    
    def setdono(self, novo_dono):
        self.dono = novo_dono

    def setprocedimento_medico(self, novo_procedimento_medico):
        self.procedimento_medico = novo_procedimento_medico

    def getprocedimento_medico(self):
        return self.procedimento_medico


    def __str__(self):
        return (f"cachorro: {self.nome},Idade: {self.idade}, raça: {self.raca}, dono: {self.dono}, procedimento medico: {self.procedimento_medico}")
        
    


class Gato():
    def __init__(self, nome, idade, raca, dono, procedimento_medico):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.dono = dono
        self.procedimento_medico = procedimento_medico


    def getnome(self):
        return self.nome
    
    def setnome(self, novo_nome):
        self.nome = novo_nome
    
    def getidade(self):
        return self.idade
    
    def setidade(self, nova_idade):
        self.nome = nova_idade

    def getraca(self):
        return self.raca
    
    def setraca(self, nova_raca):
        self.raca = nova_raca

    def getdono(self):
        return self.dono
    
    def setprocedimento_medico(self, novo_procedimento_medico):
        self.procedimento_medico = novo_procedimento_medico

    def getprocedimento_medico(self):
        return self.procedimento_medico
    
    def __str__(self):
        return (f"gato: {self.nome},Idade: {self.idade}, raça: {self.raca}, dono: {self.dono}, procedimento medico: {self.procedimento_medico}")