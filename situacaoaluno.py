p1 = float(input("\nDigite a nota da Prova 1 (P1): "))
p2 = float(input("\nDigite a nota da Prova 2 (P2): "))

t1 = float(input("\nDigite a nota do Trabalho 1 (T1): "))
t2 = float(input("\nDigite a nota do Trabalho 2 (T2): "))

mp = (p1 + p2)/2
mt = (t1 + t2)/2
mf = (0.8 * mp) + (0.2 * mt)

print(f"\nMédia das Provas: {mp:.2f}")
print(f"\nMédia dos Trabalhos: {mt:.2f}")
print(f"\nMédia Final: {mf:.2f}")

if mf >= 6.0:
    print("\nSituação: Aprovado\n")
else:
    print("\nSituação: Reprovado\n")