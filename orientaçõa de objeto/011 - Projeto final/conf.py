from classes import *
import os

def limpa():
    os.system("pause") and os.system("cls")

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

def login():
    print("=" * 30)
    print("" * 8 + "LOGIN")
    print("=" * 30)
    v_nome_usuario = input("")

def cadastro():
    print("=" * 30)
    print("" * 8 + "CADASTRO")
    print("=" * 30)
    nome = input("DIGITE SEU NOME COMPLETO \n -->")
    limpa()
    sobrenome = input("DIGITE SEU SOBRENOME \n -->")
    limpa()
    n_user = input("CRIE UM NOME DE USUARIO \n -->")
    limpa()
    cpf = input("DIGITE SEU CPF \n -->")
    limpa()
    n_telefone = input("DIGITE SEU NUMERO DE TELEFONE \n -->")
    limpa()
    senha = input("CRIE UMA SENHA \n -->")

