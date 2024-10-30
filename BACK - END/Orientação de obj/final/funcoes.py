from classes import *
import os
import random



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
    global banco
    limpa_console()
    sair = None
    while sair is None:
        print("=" * 60)
        print(" " * 10 + "BEM-VINDO À TELA DE LOGIN")
        nome = input("INSIRA O SEU NOME COMPLETO:\n--->")
        cpf = input("INSIRA O SEU CPF:\n--->")  
        for cliente in banco._clientes:
            if cliente.get_cpf() == cpf and cliente.get_nome() == nome:
                print(f"BEM VINDO, {cliente.get_nome()}!")
                conta_principal(cliente)  
                return 
        print("Nome ou CPF incorretos. Tente novamente.")




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
                        adicionar_perfil()

                    case 4:
                        excluir_cliente()
                        
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
                saldo = conta_poupanca.consultar_saldo
                print (f"Seu saldo é de: R${saldo}")

            case 2:
                 try:
                    valor_saque = float(input("Digite o valor que deseja sacar: "))
                    print(ContaCorrente.sacar(valor_saque))
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
                saldo = ContaCorrente.saldo_corrente
                print (f"Seu saldo é de: {saldo}")

            case 2:
                valor_saque = float(input("Insira o valor que deseja sacar: "))
                conta_corrente.sacar(valor_saque)
                print(conta_corrente.saldo(valor_saque))

            case 3:
                pass #deposito

    except Exception as e:
        print(f"OCORREU UM ERRO: {e}")
        limpa_console()
                

def gerente():
    limpa_console()
    
    while True:
            limpa_console()
            print("=" * 30)
            print(" " * 8 + "GERENTE - MAIN BANK")
            print("=" * 30)
            print("1 - LISTAR TODOS OS CLIENTES")
            print("2 - ADICIONAR NOVO CLIENTE")
            print("3 - EXCLUIR CLIENTE")
            print("0 - VOLTAR AO MENU PRINCIPAL")
            try:
                escolha = input("---> ")

                match escolha:

                    case 1:
                        listar_clientes()

                    case 2:
                        adicionar_cliente()

                    case 3:
                        excluir_cliente()

                    case 4:
                        menu()

            except Exception as e:
                print(f"OCORREU UM ERRO: {e}")
                limpa_console()




def listar_clientes():
        limpa_console()
        print("LISTA DE TODOS OS CLIENTES")
        if len(banco._clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in banco._clientes:
                print(f"Nome: {cliente.get_nome()} | CPF: {cliente.get_cpf()}")
                os.system("pause")



def adicionar_perfil():
        limpa_console()
        print("CRIAR NOVO PERFIL")
        print("")
        nome = input("INSIRA O NOME DO NOVO USUÁRIO:\n---> ")
        print("")
        cpf = input("INSIRA O CPF DO NOVO USUÁRIO:\n---> ")

        novo_cliente = Cliente(nome, cpf)
        banco.adicionar_cliente(novo_cliente)
        clientes.append(novo_cliente)
        print("NOVO USUARIO CADASTRADO COM SUCESSO")
        limpa_console()


def excluir_cliente():
        limpa_console()
        print("EXCLUIR PERFIL")
        cpf = input("INSIRA O CPF  QUE VOCÊ DESEJA EXCLUIR:\n---> ")
        print("")
        nome = input("INSIRA O NOME DO USUÁRIO QUE VOCE DESEJA EXCLUIR:\n--->: ")

        cliente = banco.obter_cliente(cpf, nome)
        if cliente:
            banco.remover_cliente(cliente)
            print(f"Cliente {nome} removido com sucesso.")
        else:
            print("Cliente não encontrado.")
        os.system("pause")
        


        