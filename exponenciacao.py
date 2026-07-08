def potencia(x,y):
    if y == 0:
        return 1
    else:
        resultado = 1
        for _ in range(y):
            resultado *= x
        return resultado
    

def main():
    x = input("\nDigite o valor de x (base): ")
    while not (x.isdigit()):
        print("\nA base deve ser um número inteiro!\n")
        x = input("\nDigite o valor de x (base): ")

    y = input("\nDigite o valor de y (expoente): ")
    while not (y.isdigit() and int(y) >= 0):
        print("\nO expoente deve ser um número inteiro positivo ou zero!\n")
        y = input("\nDigite o valor de y (expoente): ")

    resultado = potencia(int(x),int(y))
    
    print(f"\n{x}^{y} = {resultado}\n")


if __name__ == "__main__":
    main()
