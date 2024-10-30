from funcoes import * # importa as funções do menu
import os

sair = None

while sair != 0:
    try:
        escolha = menu()

        match escolha:
            case "1": 
                login()

            case "2":
                cadastro()

            case "3":
                sair = 0
                      
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        os.system("pause")
        os.system("cls") 