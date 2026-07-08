saldo = 0.0

print("\n===Bem-vindo ao Caixa Eletrônico===\n")

while True:
    print("\n   ===[MENU]===\n")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("4 - Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")

    elif opcao == "2":
        valor = float(input("\nValor a depositar: "))
        if valor > 0:
            saldo += valor
            print("\nDepósito realizado com sucesso!\n")
        else:
            print("\nValor inválido. Digite um valor positivo.\n")

    elif opcao == "3":
        valor = float(input("\nValor a sacar: "))
        if valor <= 0:
            print("\nValor inválido. Digite um valor positivo.\n")
        elif valor > saldo:
            print("\nSaldo insuficiente para o saque.\n")
        else:
            saldo -= valor
            print("\nSaque realizado com sucesso!\n")
    

    elif opcao == "4":
        print("\nObrigado por usar nosso sistema. Até logo!\n")
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")


