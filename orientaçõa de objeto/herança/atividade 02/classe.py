class Conta:
    def __init__(self, nome, senha, email, cpf, rg, telefone):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone

def get_nome(self):
    return self._nome

def get_senha(self):
    return self._senha

def get_email(self):
    return self._email

def get_cpf(self):
    return self._cpf

def get_rg(self):
    return self._rg

def get_telefone(self):
    return self._telefone


def set_nome(self, nome):
    self._nome = nome

def set_senha(self, senha):
    self._senha = senha

def set_email(self, email):
    self._email = email

def set_cpf(self, cpf):
    self._cpf = cpf

def set_rg(self, rg):
    self._rg = rg

def set_telefone(self, telefone):
    self._telefone = telefone


class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def get_marca(self):
        return self._marca
    
    def get_modelo(self):
        return self._modelo

    def get_ano(self):
        return self._ano


    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_ano(self, ano):
        self._ano = ano