from classes import User
import os 
import random #importa a biblioteca ramdom


usuarios = [] #lista dos usuarios cadastrados

def limpa():
    os.system("cls" if os.name == "nt" else "clear")

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
    print("=" * 30)
    print("" * 8 + "CADASTRO")
    print("=" * 30)
    nome = input("DIGITE SEU NOME COMPLETO \n -->")
    os.system("cls")
    sobrenome = input("DIGITE SEU SOBRENOME \n -->")
    os.system("cls")
    n_user = input("CRIE UM NOME DE USUARIO \n -->")
    os.system("cls")
    cpf = input("DIGITE SEU CPF \n -->")
    os.system("cls")
    n_telefone = input("DIGITE SEU NUMERO DE TELEFONE \n -->")
    os.system("cls")
    senha = input("CRIE UMA SENHA \n -->")

    novo_user = User(nome, sobrenome, n_user, cpf, n_telefone, senha)
    usuarios.append(novo_user)

    print("cadastrado com sucesso")
    limpa()

def login():
    print("=" * 30)
    print("" * 8 + "LOGIN")
    print("=" * 30)
    cpf = input ("DIGITE SEU CPF \n -->")
    senha = input ("DIGITE SUA SENHA \n -->")

    for usuario in usuarios:
        if usuario.cpf == cpf and usuario.senha == senha:
            print(f"BEM VINDO {usuarios.n_user}!!!")
            return True
    print("USUARIO NÃO ENCONTRADO, TENTE DENOVO!!!")
    return False
limpa()

def menu_opcao():
    print("=" * 30)
    print(" " * 8 + "NEXO BANK")
    print("=" * 30)
    print("1 - VERIFICAR SALDO")
    print("2 - DEPOSITO")
    print("3 - SAQUE")
    print("4 - EMPRESTIMO")
    print("5 - FINALIZAR SESSÃO")
    print("=" * 30)

def menu_login():
    sair = None

    while sair != 0:
        try:
            escolha = menu_opcao

            match escolha:
                case 1:
                    v_saldo()
                case 2:
                    deposito()
                case 3:
                    saque()
                case 4:
                    emprestimo()
                case 5:
                    sair = 0
                

        except Exception as e:
            print(f"OCORREU UM ERRO {e}")
            limpa()

            

def v_saldo():
    saldo = random.random() * 1000
    print(f"seu saldo é de ${saldo}")

def deposito():
    pass

def saque():
    pass

def emprestimo():
    pass




