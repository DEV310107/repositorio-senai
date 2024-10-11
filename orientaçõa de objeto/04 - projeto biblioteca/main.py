from funcoes import main, cadastrar_cliente, login, cliente_opcao, bibliotecario_opcao
import os
x = 0 


#loop que continua funcionando até que x seja diferente de 0    
while x == 0:
    escolha = main()

    if escolha == 1:
        cadastrar_cliente() # chama a função para cadastrar o cliente

    
    elif escolha == 2:
        usuario, tipo = login() # retorna o tipo do usuario (cliente ou bibliotecario)

        if usuario and tipo == "cliente":
            while True: #loop interno do cliente
                cliente_opcao(usuario)
                print("Deseja voltar para o menu principal?")
                print("1 - Sim")
                print("2 - Não")
                var = int(input("--->"))

                if var == 1:
                    print("Voltando para o menu...")
                    break #sai do loop interno do cliente e volta para o menu prinipal

                elif var == 2:
                    print("continuando no menu do cliente")
                    os.system("pause")
                    os.system("cls")

                else:
                    print("OPÇÃO INVÁLIDA.")


        # Chama a função se ele for o usuario bibliotecario
        elif usuario and tipo == "bibliotecario":
            bibliotecario_opcao(usuario)

    if escolha == 0:
        print("saindo...")
        x = 1 
