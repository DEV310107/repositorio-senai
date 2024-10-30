from classe import Cliente, Bibliotecario, Livro
import os 
from tabulate import tabulate #importamos a biblioteca para fazer tabelas 

clientes = [] #lista para armazenar as informçoes do cadastro

email_padrão = "adm110211@gmail.com" #email padrão do bibliotecário.
senha_padrão = "Adm110211@" # senha padrão para o bibliotecário.

#catálogo de livros
lista_livros = [
    Livro("Harry Potter e a Pedra Filosofal", "Fantasia", "10+"),
    Livro("Jogos Vorazes", "Distopia", "14+"),
    Livro("O Hobbit", "Fantasia", "12+"),
    Livro("A Culpa é das Estrelas", "Romance/Drama", "12+"),
    Livro("Percy Jackson e o Ladrão de Raios", "Fantasia", "10+"),
    Livro("O Código Da Vinci", "Mistério", "16+"),
    Livro("Cinquenta Tons de Cinza", "Romance/Erótico", "18+"),
    Livro("Extraordinário", "Drama", "Livre")
]

#def para o menu
def main():
    print("╔════════════════════════════════════════════════╗")
    print("║                                                ║")
    print("║              BIBLIOTECA SENAI                  ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")
    print("")
    print("╔════════════════════════════════════════════════╗")
    print("║ 1 - CADASTRAR         2 - LOGIN                ║")
    print("╚════════════════════════════════════════════════╝")
    var = int(input("--->"))
    os.system("pause")
    os.system("cls")
    return var


#def para adicionar informações do cliente
def cadastrar_cliente():
    nome = input("Nome: ")
    os.system("cls")
    email = input("Email: ")
    os.system("cls")
    senha = input("Senha: ")
    os.system("cls")
    tel = input("Telefone: ")
    os.system("cls")
    cpf = input("CPF: ")
    os.system("cls")
    cliente = Cliente(nome, email, senha, tel, cpf)
    clientes.append(cliente)
    print("Cadastrado com sucesso!")
    os.system("pause")
    os.system("cls")
    return cliente


#def para o login
def login():
    email = input("Email: ")
    os.system("cls")
    senha = input("Senha: ")
    os.system("cls")
    os.system("pause")

#Login do bibliotecário
    if email == "adm110211@gmail.com" and senha == senha_padrão:
        print("Bem vindo bibliotecário.")
        os.system("pause")
        os.system("cls")
        return Bibliotecario(email, senha), "bibliotecario"

#login do cliente 
    for cliente in clientes:
        if cliente.email == email and cliente.senha == senha:
            print(f"BEM-VINDO {cliente.nome}!!!")
            return cliente, "cliente"

    else:
        print("Email ou senha incorreto.")
        

#def para listar livros 
def listar_livros_dis():
    livro_formatado = []
    limpa_console()
    print("--- LIVROS DISPONÍVEIS ---:")
    cont = 1
    for livro in lista_livros:
        if not livro.reservado: #verifica se o livro não está reservado
            #adicionando os atributos formatados do livro à lista 'livro_formatado'
            livro_formatado.append([livro.getTitulo(), livro.getGenero(), livro.getClassificacao(), livro.getReservado()])
            cont += 1
            # Usa a função 'tabulate' para exibir os dados da lista de livros formatados em uma tabela
    print(tabulate(livro_formatado, headers=["Titulo", "Genero", "Classificação", "Reservado"], tablefmt="fancy_grid"))
            


#def para adicionar os livros 
def adicionar_livro(bibliotecario):
    limpa_console()
    nome = input("NOME DO LIVRO: ")
    print("")
    genero = input("GÊNERO: ")
    print('')
    classificacao = input("CLASSIFICAÇÃO: ")
    print("")
    bibliotecario.adicionar_livro(lista_livros, nome, genero, classificacao)
    print("")
    print("--- LIVRO ADICIONADO COM SUCESSO! ---")


#menu cliente
def cliente_opcao(cliente):
    limpa_console()
    print("╔══════════════════════════════════════════════╗")
    print("║              1 - RESERVA DE LIVRO            ║")    
    print("║              2 - VER RESERVAS                ║") 
    print("║              3 - CANCELAR RESERVAS           ║")
    print("║              4 - SAIR                        ║")  
    print("╚══════════════════════════════════════════════╝")
    opcao = int(input("--->"))




    #reservando livro
    if opcao == 1:
        limpa_console()
        listar_livros_dis()
        print("")
        print("")
        livro_nome = input("DIGITE O NOME DO LIVRO\n(OBS: digite o nome do livro exatamente como está no catálogo ) \n --->")
        print("")
        for livro in lista_livros: 
            if livro.titulo == livro_nome and not livro.reservado:
                cliente.reservar_livro(livro)
                livro.reservar()
                print(f"A Reserva foi concluída com sucesso. {livro.titulo}")
                return
        
        else:   
         print("LIVRO NÃO ENCONTRADO OU JÁ FOI RESERVADO POR OUTRO CLIENTE.")


    #lista os livros que foram reservados 
    elif opcao == 2:
     limpa_console()
     reservas = cliente.listar_reservas()
     livro_formatado = []
     if reservas:
        print("---- LISTA DE TODOS OS LIVROS RESERVADOS ----\n")
        cont = 1
        for livro in reservas:
            livro_formatado.append([livro.getTitulo(), livro.getGenero(), livro.getClassificacao(), livro.getReservado()])
            cont += 1
        print(tabulate(livro_formatado, headers=["Titulo", "Genero", "Classificação", "Reservado"], tablefmt="fancy_grid"))
        
    


    elif opcao == 3:
        limpa_console()
        reservas = cliente.listar_reservas()
        livro_formatado = []
        if reservas:
                print("LIVROS QUE VOCÊ PODE FAZER  O CANCELAMENTO:")
                print("")
                for livro in reservas:
                    #Tabela dos livros que você pode fazer o cancelamento junto com a biblioteca tabulate
                    livro_formatado.append([livro.getTitulo(), livro.getGenero(), livro.getClassificacao(), livro.getReservado()])
                    print(tabulate(livro_formatado, headers=["Titulo", "Genero", "Classificação", "Reservado"], tablefmt="fancy_grid"))
                print("")
                escolha = input("Digite o nome do livro para cancelar a reserva: ")
                for livro in reservas:
                    if escolha == livro.getTitulo():
                        reservas.remove(livro)
                        print(f"Reserva do livro '{livro.getTitulo()}' cancelada.")
                    else:
                        print(f"Livro '{livro.getTitulo()}' não encontrado na lista de reservas.")
        else:
                print("Nenhum livro reservado para cancelar.")

    elif opcao == 4:
        print("Voltando para o menu...")
        return
    
def limpa_console():
    os.system("pause")
    os.system("cls")

def bibliotecario_opcao(bibliotecario):
    while True:
        print("╔════════════════════════════════════════════════╗")
        print("║           1 - ADICIONAR LIVRO                  ║")    
        print("║           2 - LISTAR LIVROS DISPONÍVEIS        ║") 
        print("║           3 - SAIR                             ║")     
        print("╚════════════════════════════════════════════════╝")
        opcao = int(input("--->"))

        if opcao == 1:
            adicionar_livro(bibliotecario)
        elif opcao == 2:
            listar_livros_dis()
        elif opcao == 3:
            break
