from funcoes import * #Importa as funções do menu
import os #Importa biblioteca

sair = None #Define a variavel sair para criação do loop 

while sair != 0:#Define a variável 'sair' para controlar o loop do menu
    try:
        escolha = menu() # Chama a função 'menu' para exibir o menu e retorna a escolha do usuário

        match escolha: # Usa a estrutura 'match' para tratar as diferentes opções do menu
            case "1": 
                login() #chama a função login

            case "2":
                cadastro() #chama a função cadastro

            case "3":
                sair = 0 #Define sair como 0 para finalizar o loop
                      
    except Exception as e:
        print(f"Ocorreu um erro: {e}") #informa o usuario sobre o erro
        limpa_console() 