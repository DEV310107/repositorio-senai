from classes import * # importa as classes do arquivo Classe
import os #importa biblioteca

gerente_nome = "mateus ribeiro" #nome predefinido para o gerente 
gerente_cpf = "110211310107" #cpf predefinido para o gerente

banco =  Banco() #cria uma instância do banco para gerenciar contas e clientes 
contas = [] #cria uma lista que armazena todas as contas
clientes = [] #cria uma lista que armazena todos os clientes 
transacoes = [] #cria uma lista que armazena o historico de transação realizadas 

def menu():#Funções do menu principal, onde pode realizar o cadastro, o login, ou sair do sistema.
    print("=" * 30) #exibe uma linha separada com "="
    print(" " * 8 + "SENAI BANK") #centraliza e exibe o nome do banco 
    print("=" * 30) #exibe outra linha separada com "="
    print("1 - LOGIN")#Caso o cliente digite 1 ele entrára no login
    print("2 - CADASTRO")#Caso o cliente digite 2 ele entrára no cadastro
    print("3 - SAIR")#Caso o cliente digite 3 ele saira do sistema
    print("=" * 30) #exibe mais uma linha separada com "="
    escolha = input("--->")#Váriavel para o cliente realizar a sua escolha
    return escolha #retorna a variavel escolha, "salva o valor"

#limpa console 
def limpa_console():
    os.system("pause") 
    os.system("cls")

def cadastro():
    global banco #define a variavel "banco" como global 
    limpa_console()
    print("=" * 60) #linha separada 
    print(" " * 10 + "BEM-VINDO À TELA DE CADASTRO") #centraliza do titulo 
    print("=" * 60) #cria outra linha de separação
    nome = input("INSIRA O SEU NOME COMPLETO:\n--->") #inserir nome 
    cpf = input("INSIRA O SEU CPF:\n--->") #inserir cpf
    #instancia
    novo_cliente = Cliente(nome, cpf, banco) #cria uma nova instancia para o cliente com o nome e cpf fornecidos 
    banco.adicionar_cliente(novo_cliente) #adiciona o "novo_cliente" a lista "novo cliente"
    clientes.append(novo_cliente) #adiciona também a lista de "clientes"
    print("CADASTRO REALIZADO COM SUCESSO!") #confirmação
    limpa_console() 

 
def login():
    global banco, gerente_nome, gerente_cpf #Define as variaveis banco, gerente_nome, gerente_cpf global 
    limpa_console()
    sair = None
    while sair is None:
        print("=" * 60)
        print(" " * 10 + "BEM-VINDO À TELA DE LOGIN")
        print("")
        print("1 - FAZER LOGIN")
        print("")
        print("2 - VOLTAR AO MENU PRINCIPAL")
        print("")
        escolha = input("ESCOLHA UMA OPÇÃO:\n---> ")

        if escolha == '2':
            print("VOLTANDO AO MENU PRINCIPAL...")
            return

        elif escolha == '1':
            limpa_console()
            nome = input("INSIRA O SEU NOME COMPLETO:\n---> ")
            cpf = input("INSIRA O SEU CPF:\n---> ")


            if nome == gerente_nome and cpf == gerente_cpf: #veriifica se as informações do gerente estão corretas
                print(f"BEM VINDO, GERENTE {nome}!")
                gerente() #chama a função gerente 
                return
            for cliente in banco._clientes: #busca o cliente na lista dos clientes 
                if cliente.get_cpf() == cpf and cliente.get_nome() == nome:
                    print(f"BEM VINDO, {cliente.get_nome()}!")
                    conta_principal(cliente)  # Função específica para o cliente
                    return
            print("Nome ou CPF incorretos. Tente novamente.")
            limpa_console()
        else:
            print("Opção inválida! Tente novamente.")

def conta_principal(cliente):
    sair = None 
    while sair != 0:
            limpa_console()
            print("=" * 30)
            print(" " * 8 + "SENAI BANK")
            print("=" * 30)
            print("BEM VINDO A SUA CONTA!!")
            print("")
            print("")
            print(" ______________________________________")
            print("|                MENU                  |")
            print(" --------------------------------------")
            print("| 1 - ENTRAR NA CONTA POUPANÇA         |")
            print("| 2 - ENTRAR NA CONTA CORRENTE         |")
            print("| 3 - CRIAR PERFIL                     |")
            print("| 4 - EXCLUIR PERFIL                   |")
            print("| 5 - SAIR DO PERFIL                   |")
            print("| 6 - VER TRANSAÇÕES                   |")
            print("|______________________________________|")
            print("")
            print("")
            print("")
            try: 
                escolha= int(input("ESCOLHA UMA OPÇÃO: \n --->"))
                match escolha:

                    case 1:
                        limpa_console()
                        conta_poupanca = ContaPoupanca()  #cria uma conta poupança 
                        cliente.adicionar_conta(conta_poupanca) #adiciona a conta ao cliente 
                        poupanca(conta_poupanca) #chama a função de poupança 

                    case 2:
                        limpa_console()
                        conta_corrente = ContaCorrente() #cria uma conta corrente
                        cliente.adicionar_conta(conta_corrente) #adiciona a conta ao cliente
                        corrente(conta_corrente) #chama a função de corrente 

                    case 3:
                        limpa_console()
                        criar_perfil() #def criar perfil

                    case 4:
                        excluirperfil()
                        
                    case 5:
                        sair = 0  

                    case 6:
                        limpa_console()
                        conta_corrente = ContaCorrente()
                        if cliente:
                                print(f"Transações do cliente {cliente.get_nome()}:")
                                for conta in cliente.get_contas(): #exibe transação de todas as contas  
                                    print(f"Conta {'Corrente' if isinstance(conta, ContaCorrente) else 'Poupança'}:") # Imprime "Conta Corrente" se a variável 'conta' for uma instância de ContaCorrente, caso contrário imprime "Conta Poupança".

                                    for transacao in conta._extrato.listar_transacoes(): #exibe as transações 
                                        print(f"Tipo: {transacao.tipo} - Valor: R$ {transacao.valor:.2f}") # Exibe o tipo e o valor da transação formatado em duas casas decimais
                                                                                                           # 2f serve para exibir os valores decimais 

                    case _: 
                        print("Opção inválida! Tente novamente.")

            except ValueError:
                print("Por favor, insira uma opção numérica válida.")
                os.system("pause")
    

def criar_perfil():
    global banco #define a varial "banco" como global
    limpa_console()
    print("=" * 60) #define a linha de separação 
    print(" " * 10 + "CRIAR PERFIL")
    print("=" * 60) #define a linha de separação
    nome = input("INSIRA O SEU NOME COMPLETO:\n--->") #inserir nome 
    cpf = input("INSIRA O SEU CPF:\n--->")  #inserir cpf
    if banco.obter_cliente(cpf): # Verifica se o cliente já está cadastrado
        print("ERRO: Já existe um cliente com este CPF cadastrado.")
        limpa_console()
    novo_cliente = Cliente(nome, cpf, banco) #Cria uma nova instãncia do cliente
    banco.adicionar_cliente(novo_cliente) #Adiciona o cliente no banco
    clientes.append(novo_cliente) #adiciona cliente na lista de clientes 
    print("CADASTRO REALIZADO COM SUCESSO!")
    os.system("pause")
    

def trocar_conta():
    global banco, gerente_nome, gerente_cpf #define como global as variáveis banco, gerente_nome, gerente_cpf
    limpa_console()
    sair = None
    while sair is None:
        print("=" * 60)
        print(" " * 10 + "BEM-VINDO À TELA DE LOGIN")
        print("1 - Fazer login")
        print("2 - Voltar ao Menu Principal")

        escolha = input("Escolha uma opção:\n---> ")

        if escolha == '2':
            print("Voltando ao menu principal...")
            return

        elif escolha == '1':
            nome = input("INSIRA O SEU NOME COMPLETO:\n---> ")
            cpf = input("INSIRA O SEU CPF:\n---> ")


            if nome == gerente_nome and cpf == gerente_cpf: # Verifica se o login é do gerente usando nome e CPF pré-definidos
                print(f"BEM VINDO, GERENTE {nome}!")
                gerente()
                return


            for cliente in banco._clientes: # Verifica se o CPF e nome correspondem a um cliente registrado
                if cliente.get_cpf() == cpf and cliente.get_nome() == nome: # Verifica se o CPF e o nome fornecidos correspondem ao cliente

                    print(f"BEM VINDO, {cliente.get_nome()}!") # Exibe uma mensagem de boas-vindas personalizada para o cliente
                    conta_principal(cliente)  # Função específica para o cliente
                    return
            print("Nome ou CPF incorretos. Tente novamente.")
            limpa_console()
        else:
            print("Opção inválida! Tente novamente.")

def poupanca(conta_poupanca):
    limpa_console()
    print("BEM-VINDO À POUPANÇA")
    print("")
    while True:
        print("\nEscolha uma opção:")
        print("1: Consultar saldo")
        print("2: Sacar")
        print("3: Depositar")
        print("4: Sair")
        opcao = input("Digite o número da opção: ")
        match opcao:
            case '1':
                print(f"Seu saldo é de: R$ {conta_poupanca.consultar_saldo():.2f}") # Consulta o saldo
                limpa_console()
            case '2':
                try:
                    valor_saque = float(input("Insira o valor que deseja sacar: "))
                    saldo_poupanca = conta_poupanca.sacar(valor_saque) # Chama o método de saque
                    print(saldo_poupanca) #exibe o saldo da conta poupança
                    print(saldo_poupanca)
                    limpa_console()
                except ValueError:
                    print("Por favor, insira um número válido.")
                    limpa_console()
            case '3':
                while True:
                    try:
                        deposito_valor = float(input("Insira o valor que deseja depositar: "))
                        saldo_poupanca = conta_poupanca.depositar(deposito_valor) # Chama o método de depósito
                        print(saldo_poupanca) 
                        print(f"Saldo final da conta corrente: R$ {conta_poupanca.consultar_saldo():.2f}") #exibe o saldo final
                        limpa_console()
                        break
                    except ValueError:
                        print("Por favor, insira um número válido.")
                        limpa_console()
 
            case '4':
                print("Saindo...")
                limpa_console()
                break
            case _:
                print("Opção inválida. Tente novamente.")
                limpa_console()
                
def corrente(conta_corrente): 
    limpa_console()
    print("BEM-VINDO À CORRENTE")
    while True:
        print("\nEscolha uma opção:")
        print("1: Consultar saldo")
        print("2: Sacar")
        print("3: Depositar")
        print("4: Transferir")
        print("5: Sair")
        opcao = input("Digite o número da opção: ")
        match opcao:
            case '1':
                print(f"Seu saldo é de: R$ {conta_corrente.consultar_saldo():.2f}")
                limpa_console()
            case '2':
                try:
                    valor_saque = float(input("Insira o valor que deseja sacar: "))
                    saque_corrente = conta_corrente.sacar(valor_saque) 
                    print(saque_corrente)
                    limpa_console()
                except ValueError:
                    print("Por favor, insira um número válido.")
                    limpa_console()
            case '3':
                while True:
                    try:
                            deposito_valor = float(input("Insira o valor que deseja depositar: "))
                            saldo_corrente = conta_corrente.depositar(deposito_valor)
                            print(saldo_corrente) 
                            print(f"Saldo final da conta corrente: R$ {conta_corrente.consultar_saldo():.2f}")
                            limpa_console()
                            break
                    except ValueError:
                            print("Por favor, insira um número válido.")
                            limpa_console()
            case '4':
                    valor_transferencia = float(input("Insira o valor que deseja transferir: "))  # Solicita o valor
                    cpf_destino = input("Insira o CPF do destinatário: ")  # Solicita o CPF do destinatário
                    cliente_destino = self.encontrar_cliente(cpf_destino)  # Busca o cliente de destino pelo CPF
                    if cliente_destino:  # Verifica se o cliente de destino existe
                        conta_destino = cliente_destino.get_conta_corrente()  # Obtém a conta corrente do destinatário
                        cliente_origem = self._clientes[0]  # Para este exemplo, usa o primeiro cliente
                        conta_origem = cliente_origem.get_conta_corrente()  # Obtém a conta corrente do cliente de origem
                        sucesso = conta_origem.transferir(valor_transferencia, conta_destino)  # Realiza a transferência
                        if sucesso is True:
                            print(f"Transferência de R$ {valor_transferencia:.2f} realizada com sucesso para {cliente_destino.get_nome()}!")
                        else:
                            print(sucesso)  # Exibe a mensagem de erro retornada
                    else:
                        print("Cliente não encontrado.")  # Mensagem de er
                        
                    
            case '5':
                print("Saindo...")
                limpa_console()
                break
            case _:
                print("Opção inválida. Tente novamente.")
                limpa_console()


###################################################################################################              
def gerente():
    limpa_console()
    while True:
        print("=" * 30)
        print(" " * 8 + "GERENTE - SENAI BANK")
        print("=" * 30)
        print("1 - LISTAR TODOS OS CLIENTES")
        print("2 - ADICIONAR NOVO CLIENTE")
        print("3 - EXCLUIR CLIENTE")
        print("4 - CONSULTAR TRANSAÇÕES DE UM CLIENTE")
        print("5 - VOLTAR AO MENU PRINCIPAL")

        try:
            escolha = int(input("---> "))
            match escolha:
                case 1:
                    listar_clientes() #def
                case 2:
                    adicionar_cliente() #def
                case 3:
                    gerente_excluir() #def
                case 4:
                    extrato() #def
                case 5:
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira uma opção numérica válida.")
            limpa_console()

def listar_clientes():
    limpa_console()
    print("LISTA DE TODOS OS CLIENTES:")
    if not clientes: # Verifica se a lista de clientes está vazia
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes: # Percorre a lista de clientes e imprime o nome e CPF de cada um
            print(f"Nome: {cliente.get_nome()} - CPF: {cliente.get_cpf()}")
    limpa_console()

def adicionar_cliente():
    limpa_console()
    print("ADICIONAR NOVO USUÁRIO")
    nome = input("INSIRA O NOME DO NOVO USUÁRIO \n -->")
    cpf = input("INSIRA O CPF DO NOVO USUÁRIO \n -->")

    if banco.obter_cliente(cpf): # Verifica se já existe um cliente cadastrado com o mesmo CPF
        print("ERRO: Já existe um cliente com este CPF cadastrado.")
    else:
         # Cria um novo cliente com os dados fornecidos
        novo_cliente = Cliente(nome, cpf, banco)
        banco.adicionar_cliente(novo_cliente) # Adiciona o novo cliente ao banco de dados
        clientes.append(novo_cliente) # Adiciona o novo cliente à lista de clientes
        print("CADASTRO REALIZADO COM SUCESSO!")
    limpa_console()

def excluir_cliente():
    limpa_console()  
    print("EXCLUIR CLIENTE")  
    cpf = input("INSIRA O CPF QUE VOCÊ DESEJA EXCLUIR:\n---> ")  # Solicita o CPF do cliente
    cliente = banco.obter_cliente(cpf)  # Busca o cliente no banco
    if cliente:  # Se o cliente for encontrado
        for conta in cliente.get_contas():  # Itera sobre todas as contas do cliente
            cliente.remover_conta(conta)  # Remove a conta do cliente
        banco.remover_cliente(cpf)  # Remove o cliente do banco
        clientes.remove_conta(cliente)  # Remove o cliente da lista local
        print("Perfil do cliente removido com sucesso.")  # Mensagem de sucesso
    else:
        print("CLIENTE NÃO ENCONTRADO.")  # Mensagem de erro se o cliente não for encontrado
    os.system("pause")

def extrato():
    limpa_console()
    cpf = input("INSIRA O CPF DO CLIENTE PARA VERIFICAR O EXTRATO \n -->")
    cliente = banco.obter_cliente(cpf)
    if cliente:
        print(f"Transações do cliente {cliente.get_nome()}:")
        for conta in cliente.get_contas(): # Itera sobre todas as contas do cliente
            print(f"Conta {'Corrente' if isinstance(conta, ContaCorrente) else 'Poupança'}:") # Identifica o tipo da conta (Corrente ou Poupança) e imprime
            for transacao in conta._extrato.listar_transacoes(): # Itera sobre todas as transações da conta e as imprime
                print(f"Tipo: {transacao.tipo} - Valor: R$ {transacao.valor:.2f}")
                limpa_console()
    else:
        print("Cliente não encontrado.")
    limpa_console()

def gerente_excluir():
    limpa_console()  
    print("EXCLUIR CLIENTE")  
    cpf = input("INSIRA O CPF QUE VOCÊ DESEJA EXCLUIR:\n---> ")  # Solicita o CPF do cliente
    cliente = banco.obter_cliente(cpf)  # Obtém o cliente pelo CPF
    if cliente:
        for conta in cliente.get_contas():  # Itera sobre as contas do cliente
            cliente.remover_conta(conta)  # Remove a conta do cliente
        banco.remover_cliente(cpf)  # Remove o cliente do banco
        print("Perfil do cliente removido com sucesso.")  # Mensagem de sucesso
    else:
        print("CLIENTE NÃO ENCONTRADO.")  # Mensagem de erro se o cliente não for encontrado
    os.system("pause")  # Pausa para que o usuário possa ler a mensagem


def excluirperfil():
    limpa_console()
    cpf_cliente = input("DIGITE O CPF DA CONTA QUE VOCê DESEJA EXCLUIR?:\n---> ")
    banco.remover_cliente(cpf_cliente)
    return menu()


def transferir():
    limpa_console()
    print("--- ÁREA DE TRANSFERÊNCIA ---")
    print("")
    










#########################################################################################