from abc import *
from funcoes import *

class Banco():
    def __init__(self):
        self._clientes = []

    def adicionar_cliente(self, clientes):
        self._clientes.append(clientes)  

    def remover_cliente(self, clientes):
        self._clientes.remove(clientes) 

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

class ContaCorrente(Conta):
    def __init__(self, saldo_corrente:float=0.0):
        self._saldo_corrente = saldo_corrente
    
    def sacar(self, valor_saque:float):
        valor_saque =  input(("Insira o valor que deseja sacar:"))
        if valor_saque <= self._saldo_corrente:
            self._saldo_corrente -= valor_saque
            transacao = Transacao('Saque', valor_saque)
            self.extrato.adicionar_transacao(transacao)
            return f"Saque de {valor_saque} realizado com sucesso. Saldo atual: {self._saldo_corrente}"
        else:
            return "Saldo insuficiente para realizar o saque."   
        
    def consultar_saldo(self, saldo_corrente):
        return self._saldo_corrente
    
class ContaPoupanca(Conta):
    def __init__(self, saldo_poupanca: float = 0.0):
        super().__init__(saldo_poupanca)
        self._saldo_poupanca = saldo_poupanca
    
    
    def sacar(self, valor_saque:float):
        valor_saque =  input(("Insira o valor que deseja sacar:"))
        if valor_saque > 100:
            if self._saldo_poupanca > 100:
                self._saldo_poupanca -= valor_saque
                transacao = Transacao('Saque', valor_saque)
                self.extrato.adicionar_transacao(transacao)
                return f"Saque de {valor_saque} realizado com sucesso. Saldo atual: {self._saldo_poupanca}"
            else:
                return "Saldo insuficiente para realizar o saque."  
     
    def consultar_saldo(self, saldo_poupanca):
         return f"Saldo atual da conta poupança: R$ {str(self._saldo_poupanca)}"
    
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

