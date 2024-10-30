import os
from confg import main, cadastrar, entrar 

sair = None
usuarios = []

while sair != 0:
    try:
        escolha = main()
        os.system("cls" if os.name == "nt" else "clear")

        match escolha:
            case 1:
                usuarios.append(cadastrar())
            case 2:
                entrar()
            case 3:
                sair = 0
            case _:
                print("OPÇÃO INVÁLIDA")
                os.system("pause")
                os.system("cls")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        os.system("pause")
        os.system("cls")