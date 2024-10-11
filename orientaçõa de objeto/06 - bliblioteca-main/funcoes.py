from funcoes import *
from classes import *
global nome
global senha
global lista_livros
import os

cadastro = []

admin_password = "bibliosenai2024"      
admin_email = "bibliotecasenai@gmail.com" 

def linha():
    print('════════════════════════════════════════════════ ♦️')

def main():
    print("╔════════════════════════════════════════════════╗")
    print("║                                                ║")
    print("║              BIBLIOTECA SENAI                  ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")
    print("")
    print("╔════════════════════════════════════════════════╗")
    print("║ 1 - CLIENTE         2 - BIBLIOTECÁRIO          ║")
    print("╚════════════════════════════════════════════════╝")

    escolha = int(input("Qual opção deseja ? \n--> "))
    return escolha

os.system("cls")


def cliente():
    print("╔════════════════════════════════════════════════╗")
    print("║ 1 - CADASTRAR         2 - LOGIN                ║")
    print("╚════════════════════════════════════════════════╝")
    opcao = int(input("Qual opção deseja ? \n--> "))
    return opcao

os.system("cls")
    
def bibliotecário():
    os.system("cls")
    print("╔════════════════════════════════════════════════╗")
    print("║                BIBLIOTECÁRIO                   ║")
    print("║                Seja bem vindo                  ║")
    print("╚════════════════════════════════════════════════╝")
    print("")
    print("")
    email = input("Insira o email:\n--->")
    print("")
    senha = input("Insira a senha:\n--->")

    if email == admin_email  and senha == admin_password:
        print("Email e senha corretos")
        os.system("pause")
        os.system("cls")
        print("╔══════════════════════════════════════════╗")
        print("║          Seja bem vindo                  ║")
        print("╚══════════════════════════════════════════╝")
        print("")
        print("")
        print("╔══════════════════════════════════════════╗")
        print("║          QUAL OPÇÃO VOCÊ DESEJA?         ║")
        print("║                                          ║")
        print("║       1 = REALIZAR RESERVA DE LIVRO      ║")
        print("║       2 = ADICIONAR UM LIVRO            ║")
        print("║       3 = LIVROS DISPONÍVEIS             ║")
        print("╚══════════════════════════════════════════╝")

        escolha = int(input("--->  "))
    
        if escolha == 1:
            os.system("cls")
            print("╔════════════════════════════════════════════════╗")
            print("║                RESERVA DE LIVRO                ║")
            print("╚════════════════════════════════════════════════╝")

            class Livro:
                def __init__(self, nome, genero, classificacao_etaria):
                    self.nome = nome
                    self.genero = genero
                    self.classificacao_etaria = classificacao_etaria

                def getNome(self):
                    return self.nome

                def getGenero(self):
                    return self.genero

                def getClassificacaoEtaria(self):
                    return self.classificacao_etaria


            # Lista de livros
            lista_livros = [
                Livro("Harry Potter e a Pedra Filosofal", "Fantasia", "10+"),
                Livro("Jogos Vorazes", "Distopia", "14+"),
                Livro("O Hobbit", "Fantasia", "12+"),
                Livro("A Culpa é das Estrelas", "Romance/Drama", "12+"),
                Livro("Percy Jackson e o Ladrão de Raios", "Fantasia/Infantojuvenil", "10+"),
                Livro("O Código Da Vinci", "Mistério/Thriller", "16+"),
                Livro("Cinquenta Tons de Cinza", "Romance/Erótico", "18+"),
                Livro("Extraordinário", "Drama", "Livre")
            ]

            # Imprimir a tabela de livros
            print("---- LISTA DE TODOS OS LIVROS ----\n")
            print("ID\tNOME\t\t\t\t\tGÊNERO\t\tCLASSIFICAÇÃO ETÁRIA")

            cont = 1
            for livro in lista_livros:
                print(f"{cont}\t{livro.getNome():<30}\t{livro.getGenero():<25}\t{livro.getClassificacaoEtaria()}")
                cont += 1

    
    


        elif escolha == 2:
            os.system("cls")
            print("╔════════════════════════════════════════════════╗")
            print("║                ADICIONAR LIVRO                 ║")
            print("╚════════════════════════════════════════════════╝")
        elif escolha == 3:
             os.system("cls")
             print("╔════════════════════════════════════════════════╗")
             print("║             LIVROS DISPONÍVEIS                 ║")
             print("╚════════════════════════════════════════════════╝")
        else:
            print ("COMANDO INVÁLIDO. TENTE NOVAMENTE")
        
        
         


    else:
        print("Email e senhas incorret")
        main()


os.system("cls")



def cadastrar_cliente():
    os.system("cls")
    print("╔════════════════════════════════════════════════╗")
    print("║                   CADASTRO                     ║")
    print("║                Seja bem vindo                  ║")
    print("╚════════════════════════════════════════════════╝")

    nome = input("Digite seu nome de usuário: ")
    linha()
    senha = input("Digite sua senha: ")
    linha()
    tel = input("Digite o seu telefone: (55)")
    linha()
    email = input("Digite o seu email: ")
    linha()
    endereco = input("Digite seu endereço: ")
    linha()
    genero = input("Insira o seu gênero: ")
    linha()
    clientes = Cliente(nome, senha, tel, email, endereco, genero)
    print("")
    print("CLIENTE CADASTRADO COM SUCESSO!!!!")
    os.system("pause")
    os.system("cls")

    cadastro.append({
        "nome": nome,
        "senha": senha,
        "telefone": tel,
        "email": email,
        "endereço": endereco,
        "genero": genero
    })

os.system("cls")

def login():
    os.system("cls")
    print("╔════════════════════════════════════════════════╗")
    print("║                                                ║")
    print("║                    LOGIN                       ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")
    entrar_email = input("Insira o nome de seu usúario: ")
    linha()
    entrar_senha = input("Insira a senha do seu usúario: ")
    linha()
    os.system("cls")

    for user in cadastro:
        if entrar_email == user["email"] and entrar_senha == user["senha"]:
            print("Email e senha corretos")
            os.system("pause")
            os.system("cls")
    
    while True:  
        print("╔════════════════════════════════════════════════╗")
        print("║         ♦️  Área de Cliente  ♦️                  ║")
        print("╚════════════════════════════════════════════════╝")
        print("")
        print("1. Livros para reservar")
        print("2. minhas reservas")
        print("3. Sair")
        escolha = int(input("--->"))
        os.system("cls")

        if escolha == 1:
            print(lista_livros)

    else:
        print("email e senha nao encontrados")

os.system("cls")