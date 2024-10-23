from classes import User, Poupanca
import os
import random

usuarios = []

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("=" * 30)
    print(" " * 8 + "NEXO BANK")
    print("=" * 30)
    print("1 - LOGIN")
    print("2 - CADASTRO")
    print("3 - SAIR")
    print("=" * 30)
    
    escolha = input("Escolha uma opção\n ---> ")
    return escolha

def cadastro():
    limpa()
    print("=" * 30)
    print(" " * 8 + "CADASTRO")
    print("=" * 30)
    nome = input("DIGITE SEU NOME COMPLETO \n --> ")
    sobrenome = input("DIGITE SEU SOBRENOME \n --> ")
    n_user = input("CRIE UM NOME DE USUARIO \n --> ")
    cpf = input("DIGITE SEU CPF \n --> ")
    n_telefone = input("DIGITE SEU NUMERO DE TELEFONE \n --> ")
    senha = input("CRIE UMA SENHA \n --> ")
    novo_user = User(nome, sobrenome, n_user, cpf, n_telefone, senha)
    usuarios.append(novo_user)
    print("Cadastrado com sucesso!!!")
    limpa()

def login():
    limpa()
    print("=" * 30)
    print(" " * 8 + "LOGIN")
    print("=" * 30)
    cpf = input("DIGITE SEU CPF \n --> ")
    senha = input("DIGITE SUA SENHA \n --> ")
    limpa()

    for usuario in usuarios:
        if usuario.cpf == cpf and usuario.senha == senha:
            print(f"BEM VINDO {usuario.n_user}!!!") 
            menu_opcao(usuario)  # Passar o usuário logado para o menu de opções
            return True
    print("USUÁRIO NÃO ENCONTRADO, TENTE NOVAMENTE!!!")
    os.system("pause")
    limpa()
    return False

def menu_opcao(usuario):
    sair = None
    while sair != 0:
        print("=" * 30)
        print(" " * 8 + "NEXO BANK")
        print("=" * 30)
        print("1 - CONTA POUPANÇA")
        print("2 - CONTA CORRENTE")
        print("0 - SAIR")
        print("=" * 30)
        
        try:
            escolha = int(input("ESCOLHA UMA OPÇÃO \n --> "))
            
            match escolha:
                case 1:
                    conta_poupanca = usuario.conta_poupanca  # Atribuir a conta poupança do usuário
                    poupanca(conta_poupanca)
                case 2:
                    conta_corrente = usuario.conta_corrente  # Atribuir a conta corrente do usuário
                    corrente(conta_corrente)
                case 0:
                    sair = 0
                    
        except ValueError:
            print("Por favor, insira uma opção numérica válida.")
            os.system("pause")
            limpa()
        except Exception as e:
            print(f"OCORREU UM ERRO: {e}")
            os.system("pause")
            limpa()

def poupanca(conta_poupanca):
    limpa()
    print("BEM-VINDO À POUPANÇA")
    print("O QUE VOCÊ DESEJA FAZER: ")
    print("1 - SALDO")
    print("2 - INVESTIR")
    print("3 - SAQUE")
    
    try:
        escolha = int(input("---> "))

        match escolha:
            case 1:
                limpa()
                conta_poupanca.exibir_saldo()  # Exibir saldo
                os.system("pause")
                limpa()
            case 2:
                limpa()
                try:
                    valor_deposito = float(input("Insira o valor para depósito: R$ "))
                    resultado = conta_poupanca.depositos(valor_deposito)  # Depositar valor
                    print(resultado)
                except ValueError:
                    print("Por favor, insira um valor válido.")
                os.system("pause")
                limpa()
            case 3:
                limpa()
                try:
                    valor_saque = float(input("Insira o valor para saque: R$ "))
                    resultado = conta_poupanca.saque(valor_saque)  # Sacar valor
                    print(resultado)
                except ValueError:
                    print("Por favor, insira um valor válido.")
                os.system("pause")
                limpa()
    except ValueError:
        print("Por favor, insira uma opção numérica válida.")
        os.system("pause")
        limpa()

def corrente(conta_corrente):
    limpa()
    print("BEM-VINDO À CONTA CORRENTE")
    # Implementar funcionalidades da conta corrente
