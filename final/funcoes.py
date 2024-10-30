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
    cpf = input("INSIRA O SEU CPF:\n--->")  # Mantenha como string para evitar conversão
    novo_cliente = Cliente(nome, cpf, [], banco)  # Correção aqui
    banco.adicionar_cliente(novo_cliente)
    clientes.append(novo_cliente)
    print("CADASTRO REALIZADO COM SUCESSO!")
    limpa_console()
    menu()

def login():
    global banco
    limpa_console()
    sair = None
    while sair is None:
        print("=" * 60)
        print(" " * 10 + "BEM-VINDO À TELA DE LOGIN")
        nome = input("INSIRA O SEU NOME COMPLETO:\n--->")
        cpf = input("INSIRA O SEU CPF:\n--->")  # Mantenha como string
        for cliente in banco._clientes:
            if cliente.get_cpf() == cpf and cliente.get_nome() == nome:
                print(f"BEM VINDO, {cliente.get_nome()}!")
                menu_opcao(cliente)  # Passa o cliente para o menu
                return  # Sai após o menu
        print("Nome ou CPF incorretos. Tente novamente.")

def menu_opcao(cliente):  # Corrigido para receber um objeto Cliente
    sair = None
    while sair != 0:  # Alterado para verificar se sair é 0
        print("1 - CRIAR CONTA POUPANÇA")
        print("2 - CRIAR CONTA CORRENTE")
        print("0 - SAIR")

        try:
            escolha = int(input("ESCOLHA UMA OPÇÃO \n --> "))
            match escolha:
                case 1:
                    conta_poupanca = ContaPoupanca()  
                    cliente.adicionar_conta(conta_poupanca)  # Adiciona a conta ao cliente
                    print("CONTA POUPANÇA CRIADA")
                    limpa_console()
                    poupanca(conta_poupanca)

                case 2:
                    conta_corrente = ContaCorrente() 
                    cliente.adicionar_conta(conta_corrente)  # Adiciona a conta ao cliente
                    print("Conta corrente criada")
                    limpa_console()
                    corrente(conta_corrente)

                case 0:
                    sair = 0  # Encerra o loop

        except ValueError:
            print("Por favor, insira uma opção numérica válida.")
            os.system("pause")
           
        except Exception as e:
            print(f"OCORREU UM ERRO: {e}")
            limpa_console()
            
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
                valor_saque = float(input("Insira o valor que deseja sacar: "))
                resultado = conta_poupanca.sacar(valor_saque)
                print(f"Saque realizado de {resultado}")
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
    try:
        escolha = int(input("ESCOLHA UMA OPÇÃO \n --> "))
        
        match escolha:
            case 1:
                saldo = conta_corrente.consultar_saldo
                print (f"Seu saldo é de: R${saldo}")

            case 2:
                valor_saque = float(input("Insira o valor que deseja sacar: "))
                resultado = conta_corrente.sacar(valor_saque)
                print(f"Saque realizado de {resultado}")
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



def adicionar_cliente():
        limpa_console()
        print("ADICIONAR NOVO CLIENTE")
        print("")
        nome = input("INSIRA O NOME DO CLIENTE:\n---> ")
        print("")
        cpf = input("INSIRA O CPF DO CLIENTE:\n---> ")


        if banco.adicionar_cliente(cpf, nome):
            print("Cliente já cadastrado.")
        else:
            novo_cliente = Cliente(nome, cpf, banco)
            banco.adicionar_cliente(novo_cliente)
            print("Cliente adicionado com sucesso.")
        os.system("pause")


def excluir_cliente():
        limpa_console()
        print("EXCLUIR CLIENTE")
        cpf = input("INSIRA O CPF DO CLIENTE QUE VOCÊ DESEJA EXCLUIR:\n---> ")
        print("")
        nome = input("INSIRA O NOME DO CLIENTE QUE VOCE DESEJA EXCLUIR:\n--->: ")

        cliente = banco.obter_cliente(cpf, nome)
        if cliente:
            banco.remover_cliente(cliente)
            print(f"Cliente {nome} removido com sucesso.")
        else:
            print("Cliente não encontrado.")
        os.system("pause")