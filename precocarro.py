custo_fabrica = float(input("\nDigite o custo de fábrica do carro: R$ "))

distribuidor = custo_fabrica * 0.12
impostos = custo_fabrica * 0.30

custo_final = custo_fabrica + distribuidor + impostos

print(f"\nCusto de Fábrica: R$ {custo_fabrica:.2f}")
print(f"Custo do Distribuidor: R$ {distribuidor:.2f}")
print(f"Impostos: R$ {impostos:.2f}")
print(f"Custo ao consumidor: R$ {custo_final:.2f}\n")