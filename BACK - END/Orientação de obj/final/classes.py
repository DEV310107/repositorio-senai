from abc import *
from funcoes import *

class Banco:
    def __init__(self):
        self._clientes = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)  

    def remover_cliente(self, cliente):
        if cliente in self._clientes:  # Verifica se o cliente está na lista
            self._clientes.remove(cliente)  # Remove o cliente da lista
        else:
            print("Cliente não encontrado na lista.")

    def obter_cliente(self, cpf: str):
        for cliente in self._clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None

class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo: float=0.0 ):
        self._saldo = saldo
    
    def depositar(self, valor:float):
        pass
      
        
    def sacar(self, valor:float):
       pass

    def consultar_saldo(self, saldo):
        return self._saldo
    
    def transferir(self):
        pass
    
    def get_saldo(self):
        return self._saldo
    
 
class Cliente():
    def __init__ (self, nome: str, cpf: str, contas:list, banco: Banco):
        self._nome = nome
        self._cpf = cpf
        self._contas  = []
        self._banco = banco
    
    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf
    
    def set_nome(self, nome: str):
        self._nome = nome  

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)  

    def remover_conta(self, conta: Conta):
        self._contas.remove(conta)  

    def get_contas(self):
        return self._contas 

class Transacao:
    def __init__(self, tipo: str, valor: float):
        self.tipo = tipo
        self.valor = valor

class Extrato:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao) 

    def listar_transacoes(self):
        return self.transacoes 
    

class ContaCorrente(Conta):
    def __init__(self, saldo_corrente: float=0.0):
        super().__init__(saldo_corrente)  
        self._saldo_corrente = saldo_corrente
        self._extrato = Extrato()  

    def sacar(self, valor_saque: float):
        if valor_saque <= self._saldo_corrente:
            self._saldo_corrente -= valor_saque
            transacao = Transacao("Saque", valor_saque)
            self._extrato.adicionar_transacao(transacao)
            return f"Saque de R$ {valor_saque:.2f} realizado com sucesso. Saldo atual: R$ {self._saldo_corrente:.2f}"
        else:
            return "Saldo insuficiente para realizar o saque."
        
    def depositar(self, valor_deposito: float):
        if valor_deposito > 0:
            self._saldo_corrente += valor_deposito 
            transacao = Transacao("Depósito", valor_deposito)
            self._extrato.adicionar_transacao(transacao)  
            return f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso. Saldo atual: R$ {self._saldo_corrente:.2f}"
        else:
            return "Valor de depósito inválido."
        
    def consultar_saldo(self):
        return f"R$ {self._saldo_corrente:.2f}"
    
class ContaPoupanca(Conta):
    def __init__(self, saldo_poupanca: float = 0.0):
        super().__init__(saldo_poupanca)
        self._saldo_poupanca = saldo_poupanca
        self._extrato = Extrato()  
    
    def depositar(self, deposito_valor: float):
            deposito_valor =  float(input(("Insira o valor que deseja depositar:")))
            if deposito_valor:
                self._saldo += deposito_valor
                return f"Saque de {deposito_valor} realizado com sucesso. Saldo atual: {self._saldo_poupanca}"
            else:
                return "Depósito deu errado"
    
    def sacar(self, valor_saque:float):
           if valor_saque <= self._saldo_poupanca:
                self._saldo_poupanca -= valor_saque
                transacao = Transacao("Saque", valor_saque)
                self._extrato.adicionar_transacao(transacao)
                return f"Saque de R$ {valor_saque:.2f} realizado com sucesso. Saldo atual: R$ {self._saldo_poupanca:.2f}"
           else:
                return "Saldo insuficiente para realizar o saque."
            
    def consultar_saldo(self):
        return f"Saldo atual da conta poupança: R$ {self._saldo_poupanca:.2f}"
    


