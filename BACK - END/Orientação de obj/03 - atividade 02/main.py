import os
from confg import *

animais = []

x = 1
while x == 1: 
    print("---- Cadastro de Animais ----")
    print("1 -- Cadastrar gato")
    print("2 -- Cadastrar cachorro")
    print("3 -- Lista de animais cadastrados")
    print("4 -- Sair")
    escolha = int(input("--->"))
    os.system("pause")
    os.system("cls")


    if escolha == 1:
        print("---- Cadastro de Gatos ----")
        nome = input("Informe o nome do seu Gato\n--> ")
        os.system("cls")
        raca = input("Informe a Raça do seu Gato\n--> ")
        os.system("cls")
        idade = input("Informe a Idade do seu Gato\n--> ")
        os.system("cls")
        dono = input("Informe a Dono do seu Gato\n--> ")
        os.system("cls")
        procedimento_medico = input("Informe a Procedimento Medico do seu Gato\n--> ")
        os.system("cls")

        gato = Gato(nome,idade , raca, dono, procedimento_medico  )
        animais.append(gato)

    elif escolha == 2:
        print("---- Cadastro de Cachorro ----")
        nome = input("Informe o nome do seu cachorro\n--> ")
        os.system("cls")
        raca = input("Informe a Raça do seu cachorro\n--> ")
        os.system("cls")
        idade = input("Informe a Idade do seu cachorro\n--> ")
        os.system("cls")
        dono = input("Informe a Dono do seu cachorro\n--> ")
        os.system("cls")
        procedimento_medico = input("Informe a Procedimento Medico do seu cachorro\n--> ")
        os.system("cls")
        
        cachorro = Cachorro(nome,idade , raca, dono, procedimento_medico )
        animais.append(cachorro)

    elif escolha == 3:
        ("---- Lista de animais cadastrados ----")
        if animais:
            for animal in animais:
                print(animal)
        os.system("pause")
        os.system("cls")
            

    elif escolha == 4:
        print("saindo")
        x = 0
        os.system("pause")
    
    else:
        print("Resposta Incorreta")