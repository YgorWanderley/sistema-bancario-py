menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    option = input(menu)

    if option == "d":
        valor = float(input("Quanto você deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor}\n"
            print(extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")
        

    elif option == "s":
        valor = float(input("Quanto você quer sacar? "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor}\n"
            numero_saques += 1

        else:
            print("Operação falhou, o valor informado é inválido")

    elif option == "e":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: {saldo}")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")