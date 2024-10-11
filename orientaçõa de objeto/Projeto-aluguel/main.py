import os
from funcoes import main, cadastro, entrar, conta,limpa_console,adm

sair = None
usuarios = []

while sair != 0:
    try:
        escolha = main()

        match escolha:
            case 1:
                usuarios.append(cadastro())
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