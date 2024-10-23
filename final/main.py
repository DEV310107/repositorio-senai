import os
from conf import menu, login, cadastro

sair = False

while not sair:
    try:
        escolha = menu()

        match escolha:
            case "1":
                login()

            case "2":
                cadastro()

            case "3":
                sair = True  

            case _:
                print("OPÇÃO INVÁLIDA")
                os.system("pause")
                os.system("cls")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        os.system("pause")
        os.system("cls")
