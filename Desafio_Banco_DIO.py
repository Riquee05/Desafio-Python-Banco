menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o Valor a Ser Depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor: .2f}n\""

        else: print ("Operação falhou, numero invalido ") 

    if opcao == "s":
        valor = float(input("Insira o Valor a ser Sacado: "))

        excedeu_saque = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print ("Operação invalida, Saldo insuficiente")

        elif excedeu_limite:
            print("Operação invalida, valor excede o limite da Conta ...")

        elif excedeu_saque:
            print("limite de saques diario Excedido, tente novamente mais tarde")

            extrato -= f"saque: R$ {valor: .2f}n\""

    elif opcao =="e":
        print("\n=====Extrato=====")
        print("Não foram feitas movimentações " if not extrato else extrato)
        print(f"n\ saldo: R$ {saldo:.2f}")
        print ("=================")

    if opcao == "t":
        valor = float(input("Informe o valor a ser transferido"))

        if valor >= saldo:
            print("Valor Superior ao saldo, tente novamente")
        elif valor <= saldo:
            print("Tranferencia realizada com Sucesso")
        extrato -= f"saldo: R$ {saldo:.2f}"


    elif opcao == "q":
        break

    else:
        print("Obrigado por ultilizar nossos serviços")


        

        




