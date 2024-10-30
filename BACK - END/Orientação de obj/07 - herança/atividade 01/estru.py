from classe import Conta, ContaCorrente, ContaPoupanca
import os 

global cpf
global senha
global nome
global email                                                                                                                    
global saldo
global conta

contas = []

def limpa_console():
    os.system("pause")
    os.system("cls")

def main ():
    limpa_console()
    print("sistema de banco")
    print("1 - Cadastrar")
    print("2 - Entrar")
    print("3 - sair")
    
    while True:
        try:
            escolha = int(input("Qual opção você deseja: "))
            return escolha
        except Exception as e: 
            print(f"Valor incorreto, erro: {e}")
            os.system("pause")
            os.system("cls")



def cadastro ():
    limpa_console()
    print("cadastrar")
    print("")
    nome = input("Digite seu nome completo \n --->")
    print("")
    senha = input("Digite sua senha \n --->")
    print("")
    email = input("digite seu email \n --->")
    print("")
    cpf = int(input("digite se cpf (EX: 12398765476) \n --->"))
    print("")
    saldo = int(input("Digite o seu saldo \n ---> "))
    print("")
    print("cadastrado com sucesso")
    conta = Conta(nome, senha, email, cpf, saldo=saldo)
    contas.append(conta)
    return conta

    
def entrar ():
    x = 1
    while x == 1:
        limpa_console()
        print("Entrar")
        cpf_verifi = input("digite seu nome de usuario \n --->")
        senha_verifi = input("digite a senha \n --->")
        print("")
        print("")
        for conta in contas:
            if cpf_verifi == cpf and senha_verifi == senha:
                print(f"Bem Vindo {Conta.nome}")
                limpa_console()


            print("Conta Bancaria")
            print("")
            print("1 - Ver dados")
            print("2 - Conta corrente")
            print("3 - Poupança")
            print("4 - Sair da conta")

            var = int(input("--->"))
            os.system("pause")
            os.system("cls")

            if var == 3:
                print("DADOS")
                print(f"nome:{nome} \n senha:{senha} \n email:{email} \n cpf:{cpf} \n sald:{saldo} ")
                os.system("pause")
                os.system("cls")
                
            if var == 2:
                limpa_console()
                print("--- CONTA CORRENTE ---")
                print("")
                print("")
                print("---------------------------------")
                print(f"| SEU SALDO ATUAL É DE R${saldo}|")
                print("---------------------------------")
                print("")
                print("")
                sacar = float(input("QUAL VALOR VOCÊ DESEJA SACAR?\n--->"))
                if sacar < saldo:
                    valor_atual = ContaCorrente(saldo) - sacar
                    print(f"Seu valor agora é de {valor_atual}")

                else:
                    print("SEU SALDO É INSUFICIENTE")
                    

            if var == 3:
                print("conta Poupança")

            if var == 4:
                print("saindo da conta")
                x == 1

