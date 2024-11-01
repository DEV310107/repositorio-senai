from abc import ABC, abstractmethod #Importa uma classe abstrata e seus métodos.

####################### encapsulamento #######################
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
    
    def excluir_conta_cliente(self, cpf_cliente: str):  # Função para excluir uma conta de um cliente no sistema.
        cliente = self.obter_cliente(cpf_cliente)  # Obtém o cliente pelo CPF fornecido.
        if cliente:  # Se o cliente foi encontrado
            cliente.excluir_conta()  # Chama o método para excluir a conta do cliente.
        else:  # Se o cliente não foi encontrado
            print("CLIENTE NÃO ENCONTRADO.")
    

    def excluir_conta_cliente(self, cpf_cliente: str): #Função para excluir uma conta de um cliente no sistema, do gerente, pois ele tem acesso a todas as contas
        cliente = self.obter_cliente(cpf_cliente) # Obtém o cliente pelo CPF fornecido, utilizando a função'obter_cliente'
        if cliente: #Caso o cliente esteja no obter_cliente
            cliente.excluir_conta() #Irá excluir a conta dele
        else: #Caso o cliente não esteja no obter_cliente
            print("CLIENTE NÃO ENCONTRADO.") 


class Transacao:#Cria a classe Transação
    def __init__(self, tipo: str, valor: float):#Inicializa o construtor 
        self.tipo = tipo #Atribui o tipo de transação ("Saque" ou "Deposito")
        self.valor = valor #Atribui o valor de transação(100.00)

    def __str__(self):
        return f"{self.tipo}: R$ {self.valor:.2f}"#Retorna a transação feita, com o tipo e o valor.
    
class Extrato:
    def __init__(self):
        # Inicializa um objeto da classe Extrato, que será responsável por armazenar as transações.
        self._transacoes = [] # transacoes é uma lista que irá conter todas as transações realizadas (sacados e depósitos) para um cliente específico.


    def adicionar_transacao(self, transacao: Transacao):  # Função para adicionar uma nova transação  
        self._transacoes.append(transacao)  # Adiciona a nova transação à lista de transações

    def listar_transacoes(self):
        # Retorna a lista de transações do extrato
        return self._transacoes 
    
    def imprimir_extrato(self):
        print("Extrato de Transações:")
        for transacao in self._transacoes: # Itera sobre cada transação na lista de transações.
            print(f"Tipo: {transacao.tipo} - Valor: R$ {transacao.valor:.2f}")   # Imprime o tipo da transação (saca ou depósito) e seu valor formatado em reais.

###################### Abstrto #######################
class Conta(ABC):
    #Classe abstrata que representa uma conta bancária, definindo os métodos que as contas concretas devem implementar
    @abstractmethod
    def __init__(self, saldo: float = 0.0):
        #Inicializa uma nova instância da conta com um saldo inicial, sendo 0 
        self._saldo = saldo # Armazena o saldo atual da conta.
        self._extrato = Extrato() # Cria um objeto Extrato para armazenar transações.

    def consultar_saldo(self):
        return self._saldo #Retorna o saldo atual da conta.
    
    @abstractmethod
    def depositar(self, valor: float): #Método abstrato para depositar um valor na conta.
        pass

    def adicionar_transacao(self, transacao):
        self._extrato.adicionar_transacao(transacao) #Adiciona uma transação ao extrato da conta.
    
    def transferencia(self, conta_destino, valor: float): #Método abstrato para transferir um valor para outra conta.
        pass
    
    def adicionar_transacao(self, transacao: Transacao): #Adiciona uma transação ao extrato da conta.
        self._extrato.adicionar_transacao(transacao)  

    def listar_transacoes(self): #Retorna a lista de transações realizadas na conta.
        return self._extrato.listar_transacoes()

###################### Herança #######################
class ContaCorrente(Conta):
    def __init__(self, saldo_corrente: float = 0.0):
        super().__init__(saldo_corrente) #permite chamar métodos de classes pai de forma simples e fácil, principalmente em hierarquias de herança complexas

    def sacar(self, valor_saque: float):
        if valor_saque <= 0:
            return "O valor do depósito deve ser positivo."
        self._saldo -= valor_saque
        transacao_saque = Transacao("Saque", valor_saque)
        self.adicionar_transacao(transacao_saque)
        return f"Depósito de R$ {valor_saque:.2f} realizado com sucesso!"
        
    def transferir(self, valor: float, conta_destino):
       if valor <= self._saldo:  # Verifica se há saldo suficiente para a transferência
            self.sacar(valor)  # Tenta sacar o valor
            conta_destino.depositar(valor)  # Deposita o valor na conta de destino
            return True  # Retorna True se a transferência for bem-sucedida
       else: 
            return "Transferência deu errado! Saldo insuficiente."

    def depositar(self,valor):
        # Verifica se o valor do depósito é menor ou igual a zero
        if valor <= 0:
            return "O valor do depósito deve ser positivo."
        self._saldo += valor # Adiciona o valor do depósito ao saldo atual da conta
        transacao = Transacao("Deposito", valor)
        self.adicionar_transacao(transacao)
        return f"Depósito de R$ {valor:.2f} realizado com sucesso!"  # Retorna uma mensagem de sucesso informando o valor do depósito
    
class ContaPoupanca(Conta):
        def __init__(self, saldo_poupanca: float = 0.0): #Inicializa uma nova conta poupança com um saldo inicial.
            super().__init__(saldo_poupanca) #é utilizada para chamar métodos de uma classe pai (superclasse) a partir de uma classe filha (subclasse)

        def sacar(self, valor_saque: float):
            # Método para realizar um saque da conta poupança.
            if valor_saque <= 99: #Caso o saldo for menor que 100, ele não podera realizar um saque
              return "Saldo insuficiente para realizar o saque. O saldo deve ser superior a R$ 100"
            self._saldo -= valor_saque #Retira o valor informado do saque, no saldo da conta.
            transacao_saque = Transacao("Saque", valor_saque) #Salva como uma transação, e gera um extrato, onde está sendo passado o transa
            self.adicionar_transacao(transacao_saque) #Adiciona a transação ao adicionar uma transação
            return f"Depósito de R$ {valor_saque:.2f} realizado com sucesso!"

        def depositar(self, valor: float):
            if valor <= 0:
              return "O valor do depósito deve ser positivo."
            self._saldo += valor
            transacao = Transacao("Deposito", valor)
            self.adicionar_transacao(transacao)
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"

###################### agregação #######################
class Cliente:
    def __init__(self, nome: str, cpf: str, banco = Banco): #Método construtor da classe Cliente
        self._nome = nome #Nome do cliente
        self._cpf = cpf #CPF do cliente
        self._contas = [] #Lista onde será armazenado o cliente, que será nas contas
        self._banco = banco #Assosiação da classe Banco, onde possui os clientes

    def get_nome(self):#Retorna o nome do cliente
        return self._nome

    def get_cpf(self):#Retorna o cpf do cliente
        return self._cpf

    def set_nome(self, nome: str):#Setta o nome do cliente
        self._nome = nome

    def adicionar_conta(self, conta: Conta):#Adiciona uma conta á lista de contar
        self._contas.append(conta)

    def remover_conta(self, conta: Conta):#Remove uma conta á lista de contas
        self._contas.remove(conta)

    def get_contas(self):#Retorna as todas as contas do sistema.
        return self._contas
   