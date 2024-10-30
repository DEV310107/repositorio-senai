import os
while True:
    try:
        escolha = int (input("1 ou 2 "))
        break
    except Exception as e:
        print(f"valor invalido, o erro foi {e}")
    os.system("pause")