from estru import main, cadastro, entrar
import os

sair = None
clientes = []

while sair != 0:
    try:
        escolha = main()  
        os.system("cls")

        match escolha:
            case 1:
                clientes.append(cadastro())                                                               
            case 2:
                entrar()

            case 3:
                print("Saindo do sistema...")
                os.system("pause")
                sair = 0

            case _:
                print("OPÇÃO INVÁLIDA")
                os.system("pause")
                os.system("cls")
                
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        os.system("pause")
        os.system("cls")
