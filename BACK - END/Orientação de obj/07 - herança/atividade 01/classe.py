class Conta:
    def __init__(self, nome, senha, email, cpf, saldo=0):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
         
    def get_nome(self):
        return self._nome

    def get_senha(self):
        return self._senha

    def get_email(self):
        return self._email

    def get_cpf(self):
        return self._cpf

    def get_saldo(self):
        return self._saldo

    def set_nome(self, nome):
        self._nome = nome

    def set_senha(self, senha):
        self._senha = senha

    def set_email(self, email):
        self._email = email

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_saldo(self, saldo):
        self._saldo = saldo


class ContaCorrente(Conta):
    def __init__(self, cpf, saldo=0):
        super().__init__(cpf, saldo)


class ContaPoupanca(Conta):
    def __init__(self, cpf, saldo=0):
        super().__init__(cpf, saldo)