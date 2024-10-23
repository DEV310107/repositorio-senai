class User:
    def __init__(self, nome, sobrenome, n_user, cpf, n_telefone, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.n_user = n_user
        self.cpf = cpf
        self.n_telefone = n_telefone
        self.senha = senha

    def getNome(self):
        return self.nome
    def setNome (self, nome):
        self.nome = nome


    def getSobrenome(self):
        return self.sobrenome
    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome


    def getN_user(self):
        return self.n_user
    def setSobrenome(self, n_user):
        self.n_user = n_user


    def getCpf(self):
        return self.cpf
    def setCpf(self, cpf):
        self.cpf = cpf


    def getN_telefone(self):
        return self.n_telefone
    def setN_telefone(self, n_telefone):
        self.n_telefone = n_telefone


    def getSenha(self):
        return self.senha
    def
