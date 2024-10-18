class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)


    def __init__(self, nome, sobrenome, n_user, cpf, n_telefone, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.n_user = n_user
        self.cpf = cpf
        self.n_telefone = n_telefone
        self.senha = senha


    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_n_user(self):
        return self.n_user

    def get_cpf(self):
        return self.cpf

    def get_n_telefone(self):
        return self.n_telefone

    def get_senha(self):
        return self.senha

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def remover_conta(self, conta):
        self.contas.remove(conta)

    def get_contas(self):
        return self.contas

class Conta:
    def __init__(self, usuario, numero_conta, saldo_inicial=0.0):
        self.usuario = usuario 
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
    
    def get_usuario(self):
        return self.usuario

    def get_numero_conta(self):
        return self.numero_conta

    def get_saldo(self):
        return self.saldo

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_numero_conta(self, numero_conta):
        self.numero_conta = numero_conta

    def set_saldo(self, saldo):
        self.saldo = saldo

class Poupanca(Conta):
    def __init__(self, usuario, numero_conta, saldo_inicial=0.0, investimento = 0.0):
        super().__init__(usuario, numero_conta, saldo_inicial, investimento)
        self.investimento = investimento
        
    
    def investir(self, investimento):
            investimento = input("Insira o valor que deseja investir")
            if investimento > self.saldo:
                self.saldo -= investimento
                return f"Investimento de {investimento} realizado com sucesso. Investimento atual: {self.investimento}"
            else:
                print("Investimento falhou!")


class Corrente(Conta):
    def __init__(self, usuario, numero_conta, saldo_inicial = 0.0):
        super().__init__(usuario, numero_conta, saldo_inicial = 0.0)

    def saque(self, valor_saque):
        valor_saque =  input(("Insira o valor que deseja sacar:"))
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            return f"Saque de {valor_saque} realizado com sucesso. Saldo atual: {self.saldo}"
        else:
            return "Saldo insuficiente para realizar o saque."
    
    def depositos(self,deposito_valor):
        deposito_valor =  input(("Insira o valor que deseja depositar:"))
        if deposito_valor:
            self.saldo += deposito_valor
            return f"Saque de {deposito_valor} realizado com sucesso. Saldo atual: {self.saldo}"
        else:
            return "Depósito deu errado"


