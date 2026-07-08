
def multiplos(x):
    print(f"\nMúltiplos de {x} entre 1 e 100:")
    for num in range(1, 101):
        if num % x == 0:
            print(num, end=" ")
    print()


def main():
    x = input("\nDigite um número inteiro positivo: ")

    while not (x.isdigit() and int(x) > 0):
        print("\nNúmero inválido. O número deve ser inteiro, positivo e maior do que zero.\n")
        x = input("Digite um número inteiro positivo: ")

    multiplos(int(x))
    print()


if __name__ == "__main__":
    main()