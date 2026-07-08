def reservar_assento(assentos):
    numero = input("\nDigite o número do assento para reservar (1 a 10): ")

    while not (numero.isdigit() and 1 <= int(numero) <= 10):
        print("\nNúmero de assento inválido! Tente novamente.\n")
        numero = input("\nDigite o número do assento para reservar (1 a 10): ")

    if assentos[int(numero) - 1] == False:
        assentos[int(numero) - 1] = True
        print(f"\nAssento {numero} reservado com sucesso. \n")
    else:
        print(f"\nO assento {numero} já está ocupado.\n")


def liberar_assento(assentos):
    numero = input("\nDigite o número do assento para liberar (1 a 10): ")

    while not (numero.isdigit() and 1 <= int(numero) <= 10):
        print("\nNúmero de assento inválido! Tente novamente.\n")
        numero = input("\nDigite o número do assento para liberar (1 a 10): ")

    if assentos[int(numero) - 1] == True:
        assentos[int(numero) - 1] = False
        print(f"\nAssento {numero} liberado com sucesso. \n")
    else:
        print(f"\nO assento {numero} já está livre.\n")


def mostrar_mapa(assentos):
    print("\nMapa de Ocupação dos Assentos: ")
    for i in range(10):
        if assentos[i] == True:
            status = "Ocupado"
        else:
            status = "Livre"
        
        print(f"Assento {i + 1}: {status}")
    print()


def main():

    assentos = [False] * 10

    while True:
        print("\n---Menu do Cinema---")
        print("\n1 - Reservar um assento")
        print("2 - Liberar um assento")
        print("3 - Mostrar mapa de ocupação")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            reservar_assento(assentos)
        elif opcao == "2":
            liberar_assento(assentos)
        elif opcao == "3":
            mostrar_mapa(assentos)
        elif opcao == "4":
            print("\nEncerrando o programa. Até logo!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()