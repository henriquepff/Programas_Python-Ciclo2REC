def adicionar_nota(notas):
    nome = input("\nNome do aluno: ")

    disciplina = input("\nDisciplina: ")

    nota = float(input("\nNota do aluno: "))

    while not (nota >= 0.0 and nota <= 10.0):
        print("\nA nota deve ser um número de 0 a 10!\n")
        nota = float(input("\nNota do aluno: "))

    notas.append((nome,nota,disciplina))

    print("\nNota adicionada com sucesso.\n")




def melhor_por_disciplina(notas):
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
    
    disciplinas = []

    for n in notas:
        if n[2] not in disciplinas:
             disciplinas.append(n[2])

    print("\nMelhor aluno por disciplina: \n")
    for d in disciplinas:
        melhor_nota = -1
        melhor_aluno = ""
        for n in notas:
            if n[2] == d and n[1] > melhor_nota:
                melhor_nota = n[1]
                melhor_aluno = n[0]
        
        print(f"{d}: {melhor_aluno} ({melhor_nota})")
    
    print()

def consultar_por_aluno(notas):
    nome_busca = input("\nDigite o nome do aluno: ")

    encontrou = False

    for n in notas:
        if n[0].lower() == nome_busca.lower():
            print(f"\n{n[2]}: {n[1]}")
            encontrou = True

    if not encontrou:
        print("\nNenhuma nota encontrada para este aluno.\n")


def obter_nota(tupla):
    return tupla[1]


def exibir_ordenadas(notas):
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
    
    ordenadas = sorted(notas, key=obter_nota, reverse= True)
    
    print("\nNotas ordenadas (decrescente): \n")
    for n in ordenadas:
        print(f"{n[1]:.2f}, {n[0]}, {n[2]}")
    print()


def main():

    notas = []

    while True:
        print("\n---Menu de Notas---")
        print("\n1 - Adicionar nota")
        print("2 - Mostrar melhor aluno por disciplina")
        print("3 - Consultar notas por aluno")
        print("4 - Exibir notas ordenadas (decrescente)")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            adicionar_nota(notas)
        elif opcao == "2":
            melhor_por_disciplina(notas)
        elif opcao == "3":
            consultar_por_aluno(notas)
        elif opcao == "4":
            exibir_ordenadas(notas)
        elif opcao == "5":
            print("\nEncerrando o programa. Até logo!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()