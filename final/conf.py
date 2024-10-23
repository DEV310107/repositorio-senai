import os
import random
from classes import *





usuarios = []





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

    escolha = int(input("ESCOLHA UMA OPÇÃO \n -->"))
    return escolha





def cadastro():
    limpa()
    limpa()
    print("=" * 30)
    print(" " * 8 + "CADASTRO")
    print("=" * 30)
    nome = input("DIGITE SEU NOME COMPLETO \n --> ")
    os.system("cls")
    sobrenome = input("DIGITE SEU SOBRENOME \n --> ")
    os.system("cls")
    n_user = input("CRIE UM NOME DE USUARIO \n --> ")
    os.system("cls")
    cpf = input("DIGITE SEU CPF \n --> ")
    os.system("cls")
    n_telefone = input("DIGITE SEU NUMERO DE TELEFONE \n --> ")
    os.system("cls")
    senha = input("CRIE UMA SENHA \n --> ")

    novo_user = User(nome, sobrenome, n_user, cpf, n_telefone, senha)
    usuarios.append(novo_user)
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
                        limpa()
                        conta_poupanca = usuario.conta_poupanca
                        poupanca(conta_poupanca)
                        limpa()
                    case 2:
                        limpa()
                        try:
                            valor_deposito = float(input("INSIRA UM VALOR PARA DEPOSITO R$"))
                        except ValueError:
                            print("POR FAVOR INSIRA UM VALOR VALIDO!!")
                            os.system("pause")
                        limpa()
        except ValueError:
            print("POR FAFOR, INSIRA UM VALOR VÁLIDO")
            os.system("pause")
            limpa()
            