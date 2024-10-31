from classes import *
import os

gerente_nome = "1"
gerente_cpf = "1"

global banco 
global cpf
global nome

banco =  Banco()
contas = []
clientes = []
transacoes = []

def menu():
    print("=" * 30)
    print(" " * 8 + "SENAI BANK")
    print("=" * 30)
    print("1 - LOGIN")
    print("2 - CADASTRO")
    print("3 - SAIR")
    print("=" * 30)
    escolha = input("--->")   
    return escolha

def limpa_console():
    os.system("pause")
    os.system("cls")
    
def cadastro():
    global banco
    limpa_console()
    print("=" * 60)
    print(" " * 10 + "BEM-VINDO À TELA DE CADASTRO")
    print("=" * 60)
    nome = input("INSIRA O SEU NOME COMPLETO:\n--->")
    cpf = input("INSIRA O SEU CPF:\n--->")  
    novo_cliente = Cliente(nome, cpf, [], banco) 
    banco.adicionar_cliente(novo_cliente)
    clientes.append(novo_cliente)
    print("CADASTRO REALIZADO COM SUCESSO!")
    limpa_console()

def criarperfil():
    global banco 
    limpa_console()
    print("=" * 60)
    print(" " * 10 + "CRIAR PERFIL")
    print("=" * 60)
    nome = input("INSIRA O SEU NOME COMPLETO:\n--->")
    cpf = input("INSIRA O SEU CPF:\n--->")  
    novo_cliente = Cliente(nome, cpf, [], banco) 
    banco.adicionar_cliente(novo_cliente)
    clientes.append(novo_cliente)
    print("CADASTRO REALIZADO COM SUCESSO!")
    limpa_console()

def login():
    global banco, gerente_nome, gerente_cpf
    limpa_console()
    sair = None
    while sair is None:
        print("=" * 60)
        print(" " * 10 + "BEM-VINDO À TELA DE LOGIN")
        nome = input("INSIRA O SEU NOME COMPLETO:\n---> ")
        cpf = input("INSIRA O SEU CPF:\n---> ")  

        if nome == gerente_nome and cpf == gerente_cpf:
            print(f"BEM VINDO, GERENTE {nome}!")
            gerente()  # Função específica para o gerente
            return 
    
        for cliente in banco._clientes:
            if cliente.get_cpf() == cpf and cliente.get_nome() == nome:
                print(f"BEM VINDO, {cliente.get_nome()}!")
                conta_principal(cliente)  # Função específica para o cliente
                return 
        
        print("Nome ou CPF incorretos. Tente novamente.")
        limpa_console()

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
            print("|______________________________________|")
            print("")
            print("")
            print("")
            try: 
                escolha= int(input("ESCOLHA UMA OPÇÃO: \n --->"))
                match escolha:

                    case 1:
                        limpa_console()
                        conta_poupanca = ContaPoupanca()  
                        cliente.adicionar_conta(conta_poupanca) 
                        poupanca(conta_poupanca)

                    case 2:
                        limpa_console()
                        conta_corrente = ContaCorrente() 
                        cliente.adicionar_conta(conta_corrente) 
                        corrente(conta_corrente)

                    case 3:
                        adicionar_cliente()

                    case 4:
                        excluir_cliente(cliente)
                        
                    case 5:
                        sair = 0  

                    case _: 
                        print("Opção inválida! Tente novamente.")

            except ValueError:
                print("Por favor, insira uma opção numérica válida.")
                os.system("pause")
    
def poupanca(conta_poupanca):
    limpa_console()

    print("BEM-VINDO À POUPANÇA")
    print("")
    print("O QUE VOCÊ DESEJA FAZER: ")
    print("1 - SALDO")
    print ("2 - SACAR")
    try:
        escolha = int(input("ESCOLHA UMA OPÇÃO \n --> "))
        
        match escolha:
            case 1:
                conta_poupanca = ContaPoupanca(500.00)
                print("Seu saldo é de:", conta_poupanca.consultar_saldo())

            case 2:
                 try:
                    valor_saque = float(input("Digite o valor que deseja sacar: "))
                    if valor_saque <= conta_poupanca.get_saldo_poupanca():
                        print(conta_poupanca.sacar(valor_saque))
                    else:
                        print("Valor maior que o saldo")
                 except ValueError:
                    print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"OCORREU UM ERRO: {e}")
        limpa_console()
          
def corrente(conta_corrente): 
    limpa_console()
    print("BEM-VINDO À CORRENTE")
    print("")
    print("O QUE VOCÊ DESEJA FAZER: ")
    print("1 - SALDO")
    print ("2 - SACAR")
    print("3 - DEPOSITAR")
    try:
        escolha = int(input("ESCOLHA UMA OPÇÃO \n --> "))
        
        match escolha:
            case 1:
                print("Seu saldo é de:", conta_corrente.consultar_saldo())
            case 2:
                valor_saque = float(input("Insira o valor que deseja sacar: "))
                mensagem = conta_corrente.sacar(valor_saque) 
                print(mensagem)
            case 3:
                valor_deposito = float(input("Insira o valor que deseja depositar: "))
                conta_corrente.depositar(valor_deposito)
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    except Exception as e:
        print(f"OCORREU UM ERRO: {e}")
        limpa_console()
###################################################################################################              
def gerente():
    limpa_console()
    while True:
        print("=" * 30)
        print(" " * 8 + "GERENTE - MAIN BANK")
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
                    listar_clientes()
                case 2:
                    adicionar_cliente()
                case 3:
                    excluir_cliente()
                case 4:
                    extrato()
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
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"Nome: {cliente.get_nome()} - CPF: {cliente.get_cpf()}")
    limpa_console()

def adicionar_cliente():
    limpa_console()
    print("ADICIONAR  NOVO USUÁRIO")
    nome = input("INSIRA O NOME DO NOVO USUÁRIO \n -->")
    cpf = input("INSIRA O CPF DO NOVO USUÁRIO \n -->")

    novo_cliente = Cliente(nome, cpf, [], banco)
    banco.adicionar_cliente(novo_cliente)
    clientes.append(novo_cliente)
    limpa_console()

def excluir_cliente():
    limpa_console()
    print("EXCLUIR PERFIL")
    cpf = input("INSIRA O CPF QUE VOCÊ DESEJA EXCLUIR:\n---> ")

    cliente = banco.obter_cliente(cpf) 
    
    if cliente:  
        banco.remover_cliente(cliente)  
        clientes.remove(cliente)  
        print(f"Cliente {cliente.get_nome()} removido com sucesso.")
    else:
        print("Cliente não encontrado.")
        
    os.system("pause")

def extrato():
    limpa_console()
    cpf = input("INSIRA O CPF DO CLIENTE PARA VERIFICAR O EXTRATO \n -->")
    cliente = banco.obter_cliente(cpf)

    if cliente:
        print(f"Transações do cliente {cliente.get_nome()}:")
        for conta in cliente.get_contas():
            print(f"Conta {'Corrente' if isinstance(conta, ContaCorrente) else 'Poupança'}:")
            for transacao in conta._extrato.listar_transacoes():
                print(f"Tipo: {transacao.tipo} - Valor: R$ {transacao.valor:.2f}")
    else:
        print("Cliente não encontrado.")
    limpa_console()


def excluir_cliente(cliente):
    limpa_console()
    print("EXCLUIR PERFIL")
    cpf = input("INSIRA O CPF QUE VOCÊ DESEJA EXCLUIR:\n---> ")
    if cliente.get_cpf() == cpf: 
        banco.remover_cliente(cliente) 
        clientes.remove(cliente) 
        print(f"Perfil de {cliente.get_nome()} excluído com sucesso.")
    else:
        print("Você não tem permissão para excluir este perfil.")
    limpa_console()
#########################################################################################


        