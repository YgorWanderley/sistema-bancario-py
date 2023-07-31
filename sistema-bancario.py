def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("=== Depósito realizado com sucesso! ===")
    else:
            print("@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = len(numero_saques) >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        numero_saques.append("a")
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("=== Saque realizado com sucesso! ===")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_user(users):
    cpf = input("Informe o CPF (somente número): ")
    user = filtrar_user(cpf, users)
    if user:
        print("@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço: ")
    users.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })
    print("=== Usuário criado com sucesso! ===")

def filtrar_user(cpf, users):
    usuarios_filtrados = [user for user in users if user["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filtrar_user(cpf, users)

    if user:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuário": user}
    
    print("@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    numero_saques = []
    extrato = ""
    users = []
    contas = []

    while True:
        option = menu()
        
        if option == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif option == "s":
            valor = float(input("informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif option == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif option == "nu":
            criar_user(users)

        elif option == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, users)

            if conta:
                contas.append(conta)
                print(contas)
        
        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada")

main()