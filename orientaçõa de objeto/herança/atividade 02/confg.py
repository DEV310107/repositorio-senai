import os
from classe import Conta, Veiculo

global cpf
global senha

contas = []

def linha():
    print("----------------------------------------")

def main():
    print("SISTEMA DE ALUGUEL DE VEICULOS")
    linha()
    print("1 - CADASTRAR")
    print("2 - ENTRAR")
    print("3 - SAIR")
    linha

    while True:
        try:
            escolha = int(input("Qual opção você deseja: "))
            return escolha
        except Exception as e:
            print(f"Valor incorreto, erro: {e}")
            os.system("pause")
            os.system("cls")

def cadastrar():
    print("CADASTRO")
    linha()
    nome = input("DIGITE SEU NOME COMPLETO \n --->")
    print("")
    email = input("DIGITE SEU EMAIL \n --->")
    print("")
    senha = input("DIGITE SUA SENHA \n --->")
    print("")
    cpf = input("DIGITE SEU CPF (EX: 12398765476) \n --->")
    print("")
    rg = input("DIGITE SEU RG (EX: 12398765476) \n --->")
    print("")
    telefone = input("DIGITE SEU NUMERO DE TELEFONE (EX: 12398765476) \n ---> ")
    linha()
    print("")
    print("CADASTRO FEITO COM SUCESSO")
    conta = Conta(nome, senha, email, senha, cpf, rg, telefone)
    contas.append(conta)
    return conta 

def entrar():
        print("ENTRAR NA CONTA")
        linha()
        v_cpf = input("DIGITE SEU CPF \n --->")
        linha()
        v_senha = input("DIGITE A SUA SENHA \n --->")
        
        if v_cpf == cpf and v_senha == senha:
             print("BEM VINDO {nome}.")

        


