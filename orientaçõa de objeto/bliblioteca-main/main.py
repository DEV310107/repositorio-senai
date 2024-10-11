from funcoes import linha, main, cliente, bibliotecário, cadastrar_cliente, login
from classes import Cliente,Livro
import os

sair = None
clientes = []

while sair != 0:
    escolha = main()
    os.system("cls")

    if escolha == 1:
        os.system("cls")
        opcao = cliente()

        if opcao == 1:
            os.system("cls")
            clientes.append(cadastrar_cliente())


        elif opcao == 2:
            login()
             
   
    elif escolha == 2:
        bibliotecário()

    elif escolha == 3:
        pass
    
    
    elif escolha == 0:
        print("")
        os.system("pause")
        sair = 0
    else:
        print("OPÇÃO INVALIDA")
        print("")
        os.system("pause")
        os.system("cls")