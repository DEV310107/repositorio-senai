from abc import ABC, abstractmethod #Importa uma classe abstrata e seus métodos.

class Banco:#Cria uma classe utilizando o encapsulamento, ligadas a métodos especiais chamados getters e setters, que irão retornar e setar o valor da propriedade.
    def __init__(self): #Método construtor da classe banco
        self._clientes = [] #Cria uma lista clientes, onde serão armazenados cada cliente do sistema, porém os clientes podem existir sem a classe banco(agregação)

    def adicionar_cliente(self, cliente):#Função para adicionar um cliente no sistema.
        self._clientes.append(cliente)#Adicionar os clientes na lista do cliente.

    def remover_cliente(self, cpf: str): #Função para remover um cliente do sistema.
        for cliente in self._clientes: #Ira iterar sobre a lista cliente
            if cliente.get_cpf() == cpf:  #Verifica se o cpf fornecido for igual o cpf de um cliente já cadastrado num sistema.
                self._clientes.remove(cliente) #Remove o cliente informado da lista.
                print(f"Cliente removido com sucesso.") #Imprime caso dê certo a remoção
                return
            else:
                print(f"Cliente não encontrado.") #Caso não ache o cliente no sistema, ele ira imprimir.

    def obter_cliente(self, cpf: str): #Função para encontrar um cliente no sistema.
        for cliente in self._clientes: #Ira iterar sobre a lista cliente
            if cliente.get_cpf() == cpf: #Verifica se o cpf fornecido for igual o cpf de um cliente já cadastrado num sistema.
                return cliente #Retorna o cliente informado.
        return None #Caso não ache o cliente, não irá retornar nada.

class Transacao:#Cria a classe Transação
    def __init__(self, tipo: str, valor: float):#Inicializa o construtor 
        self.tipo = tipo #Atribui o tipo de transação ("Saque" ou "Deposito")
        self.valor = valor #Atribui o valor de transação(100.00)

    def __str__(self):
        return f"{self.tipo}: R$ {self.valor:.2f}"#Retorna a transação feita, com o tipo e o valor.
    
class Extrato:
    def __init__(self):
        self._transacoes = [] 

    def adicionar_transacao(self, transacao: Transacao):  # Método para adicionar uma nova transação  
        self._transacoes.append(transacao)  # Adiciona a nova transação à lista de transações

    def listar_transacoes(self):
        return self._transacoes 
    
    def imprimir_extrato(self):
        print("Extrato de Transações:")
        for transacao in self._transacoes:
            print(f"Tipo: {transacao.tipo} - Valor: R$ {transacao.valor:.2f}")

class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo: float = 0.0):
        self._saldo = saldo
        self._extrato = Extrato()

    def consultar_saldo(self):
        return self._saldo
    
    @abstractmethod
    def depositar(self, valor: float):
        pass

    def adicionar_transacao(self, transacao):
        self._extrato.adicionar_transacao(transacao)
    
    def transferencia(self, conta_destino, valor: float):
        pass
    
    def adicionar_transacao(self, transacao: Transacao):
        self._extrato.adicionar_transacao(transacao)  

    def listar_transacoes(self):
        return self._extrato.listar_transacoes()

class ContaCorrente(Conta):
    def __init__(self, saldo_corrente: float = 0.0):
        super().__init__(saldo_corrente)

    def sacar(self, valor_saque: float):
        if valor_saque <= 0:
            return "O valor do depósito deve ser positivo."
        self._saldo -= valor_saque
        transacao_saque = Transacao("Saque", valor_saque)
        self.adicionar_transacao(transacao_saque)
        return f"Depósito de R$ {valor_saque:.2f} realizado com sucesso!"
        
    def transferir(self, valor: float, conta_destino: 'Conta'):
         if valor <= 0:
            print("O valor da transferência deve ser positivo.")
         if valor > self.saldo:
            print("Saldo insuficiente para a transferência.")
         self._saldo -= valor
         conta_destino.depositar(valor)
         transacao = Transacao("Transferência", valor)
         self.adicionar_transacao(transacao)
         return True

    def depositar(self, valor: float):
        if valor <= 0:
            return "O valor do depósito deve ser positivo."
        self._saldo += valor
        transacao = Transacao("Deposito", valor)
        self.adicionar_transacao(transacao)
        return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
    

class ContaPoupanca(Conta):
        def __init__(self, saldo_poupanca: float = 0.0):
            super().__init__(saldo_poupanca)

        def sacar(self, valor_saque: float):
            if valor_saque <= 99:
                 return "Saldo insuficiente para realizar o saque. O saldo deve ser superior a R$ 100."
            self._saldo -= valor_saque
            transacao_saque = Transacao("Saque", valor_saque)
            self.adicionar_transacao(transacao_saque)
            return f"Depósito de R$ {valor_saque:.2f} realizado com sucesso!"

        def depositar(self, valor: float):
            if valor <= 0:
              return "O valor do depósito deve ser positivo."
            self._saldo += valor
            transacao = Transacao("Deposito", valor)
            self.adicionar_transacao(transacao)
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"

class Cliente:
    def __init__(self, nome: str, cpf: str, banco = Banco):
        self._nome = nome
        self._cpf = cpf
        self._contas = []
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
   