a = int(input("\nDigite o valor de A: "))

b = int(input("\nDigite o valor de B: "))

print(f"\nValor antes da troca de A: {a}")
print(f"Valor antes da troca de B: {b}")

auxiliar = a
a = b
b = auxiliar

print(f"\nValor depois da troca de A: {a}")
print(f"Valor depois da troca de B: {b}\n")