import os
from classes import Veiculo, Moto, Carro
contas = []
carros = []
carros_alugados = []
motos = []
motos_alugados = []


global user 
global senha
global cpf
global alugado


def limpa_console():
    os.system("pause")
    os.system("cls")

def linha():
    ("-------------------------------------")

def main():
    print("---- SISTEMA DE LOCADORA DE VEÍCULOS ----")
    print("")
    print("1 - CADASTRAR")
    print("2 - LOGIN")
    print("3 - SAIR")
    print("")
    while True:
        try:
            escolha = int(input("QUAL OPÇÃO VOCÊ DESEJA? \n--> "))
            if escolha in [0, 1, 2]:
                return escolha
            else:
                print("Opção inválida.\nTente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
            

def cadastro():
    while True:
        try:
            limpa_console()
            print("--- CADASTRO ---")
            print("\nFAÇA SEU CADASTRO ABAIXO\n")

            nome = input("INSIRA SEU NOME:\n---> ")
            sobrenome = input("INSIRA SEU SOBRENOME:\n---> ")
            user = input("INSIRA SEU NOME DE USUÁRIO (pode conter números e letras):\n---> ")
            senha = input("INSIRA SUA SENHA:\n---> ")
            cpf = int(input("INSIRA O SEU NÚMERO DE CPF (somente números):\n---> "))
            tel = input("INSIRA SEU NÚMERO DE TELEFONE:\n---> (+55) ")
            email = input("INSIRA SEU EMAIL:\n---> ")

            print("\nCADASTRO REALIZADO COM SUCESSO!\n")
            limpa_console()
            print("1 - SIM")
            print("2 - NÃO")
            modificar = int(input("Tudo pronto? (Escolha 1 ou 2): "))

            if modificar == 1:
                contas.append({
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "user": user,
                    "senha": senha,
                    "cpf": cpf,
                    "telefone": tel,
                    "email": email
                })

                limpa_console()
                print("INFORMAÇÕES DE CADASTRO:")
                print("")
                print(f"Nome: {nome} {sobrenome}")
                print("")
                print(f"Usuário: {user}")
                print("")
                print(f"CPF: {cpf}")
                print("")
                print(f"Telefone: +55 {tel}")
                print("")
                print(f"E-mail: {email}")
                break  
            else:
                print("Cadastro cancelado. Tente novamente.")
                input("Pressione Enter para continuar...")
        
        except ValueError:
            print("Entrada inválida. Por favor, tente novamente.")
            input("Pressione Enter para continuar...")



   
def entrar():    
    adm_user = 103020

    adm_senha = "Adm_502"
    limpa_console()
    print("ENTRAR NA CONTA")
    print("")
    v_cpf = (int(input("DIGITE SEU CPF \n ---> ")))
    print("")
    v_senha = input("DIGITE A SUA SENHA \n ---> ")
    

    if v_cpf == adm_user and v_senha == adm_senha:
        limpa_console()
        adm()

    for conta in contas:
        if conta[cpf] == v_cpf and conta[senha] == v_senha:
            limpa_console()
            conta()
        
def adm():
    limpa_console()
    print("--- BEM VINDO A CONTA DE ADMINISTRADOR ---")
    print("")
    print("")
    print("QUAL OPÇÃO VOCÊ DESEJA EXECUTAR?")
    print("")
    print("1 --- CADASTRAR CARRO")
    print("2 --- VISUALIZAR RESERVAS")
    print("3 --- CARROS CADASTRADOS")
    print("4 --- CADASTRAR MOTO")
    print("5 --- VISUALIZAR RESERVAS")
    print("6 --- MOTOS CADASTRADAS")
    print("")
    escolha = int(input("--->"))

    if escolha == 1:
        limpa_console()
        cadastro_carros()

    elif escolha == 2:
        limpa_console()
        if carros_alugados:  
            print("AQUI ESTÃO OS CARROS ALUGADOS:")
            i = 1 
            for carro in carros_alugados:
                print(f"{i} - Marca: {carros['marca']}, Modelo: {carros['modelo']}, Ano: {carros['ano']}, Placa: {carros['placa']}")
                i += 1  
    
    elif escolha == 3:
        limpa_console()
        print("--- CARROS CADASTRADOS ---")
        print("")
        if not carros:
            print("Nenhum carro cadastrado.")
        else:
            print("Carros cadastrados:")
            i = 1
        for i, carro in carros:
            print(f"{i}° carro: {carros.marca} {carros.modelo} - {carros.ano} - {carros.placa}")
            i += 1 
            limpa_console()

  
        


def cadastro_carros():
    limpa_console()
    while True:
        try:
            print("Adicione as informações do carro que deseja cadastrar: ")
            marca = input("Qual a marca: ")
            modelo = input("Qual o modelo: ")
            ano = input("Qual o ano: ")
            placa = input("Qual a placa: ")
            
            if not marca or not modelo or not ano or not placa:
                raise ValueError("Todos os campos são obrigatórios.")
            
            carro = Carro(marca, modelo, ano, placa)
            carros.append(carro)
            print("Carro cadastrado com sucesso!")
            break 

        except ValueError as ve:
            print(f"Erro de validação: {ve}")
            os.system("pause")
            os.system("cls")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            os.system("pause")
            os.system("cls")


def alugar_carros():
    limpa_console()
    print("Carros disponíveis para aluguel: ")
    i = 1 
    for carro in carros:
        print(f"{i} - {carros.marca} {carros.modelo} ({carros.ano}) - Placa: {carros.placa}")
        i += 1 
    
    escolha = int(input("Digite o número do carro que deseja alugar: "))
    
    
    if 1 <= escolha <= i - 1:  
        carro_selecionado = carros[escolha - 1]
        carro_info = {
            "marca": carro_selecionado.marca,
            "modelo": carro_selecionado.modelo,
            "ano": carro_selecionado.ano,
            "placa": carro_selecionado.placa
        }
  
        carros_alugados.append(carro_info)
        print(f"Você alugou: {carro_info['marca']} {carro_info['modelo']} ({carro_info['ano']}) - Placa: {carro_info['placa']}")
    else:
        print("Escolha inválida.")





def cadastro_motos():
 while True:
        try:
            print("Adicione as informações da moto que deseja cadastrar: ")
            marca = input("Qual a marca: ")
            modelo = input("Qual o modelo: ")
            ano = input("Qual o ano: ")
            placa = input("Qual a placa: ")
            moto = Moto(marca, modelo, ano, placa)
            carros.append(motos)
            print("Moto cadastrada com sucesso!! ")
            break
        except Exception as e:
            print(f"Essa opção não existe\n Erro {e}")
            os.system("pause")
            os.system("cls")

def alugar_motos():
    limpa_console()
    print("Motos disponíveis para aluguel: ")
    i = 1 
    for moto in motos:
        print(f"{i} - {moto.marca} {moto.modelo} ({moto.ano}) - Placa: {moto.placa}")
        i += 1 
    
    escolha = int(input("Digite o número da moto que deseja alugar: "))
    
    
    if 1 <= escolha <= i - 1:  
        motos_selecionadas = motos[escolha - 1]
        moto_info = {
            "marca": motos_selecionadas.marca,
            "modelo": motos_selecionadas.modelo,
            "ano": motos_selecionadas.ano,
            "placa": motos_selecionadas.placa
        }
  
        motos_alugados.append(moto_info)
        print(f"Você alugou: {moto_info['marca']} {moto_info['modelo']} ({moto_info['ano']}) - Placa: {moto_info['placa']}")
    else:
        print("Escolha inválida.")


    
def conta():
    while True:       
        limpa_console()
        print("\n---- MENU DA CONTA ----")
        print("")
        print("1 - ALUGAR CARRO")
        print("2 - Visualizar e Alterar Informações da Conta")
        print("3 - ALUGAR MOTO")
        print("4 - Sair")
        print("------------------------")
        
        try:
            escolha = int(input("Escolha uma opção:\n--> "))

            match escolha:
                case 1:
                    alugar_carros()
                case 2:
                    visualizar_informacoes()                                                
                case 3:
                    alugar_motos()
                    break
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def visualizar_informacoes():
      for conta in contas:
            print("INFORMAÇÕES DA CONTA:")
            print(f"Nome: {conta['nome']} {conta['sobrenome']}")
            print(f"CPF: {conta['cpf']}")
            print(f"Telefone: {conta['telefone']}")
            print(f"E-mail: {conta['email']}")

            

