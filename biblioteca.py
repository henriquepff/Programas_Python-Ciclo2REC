def adicionar_livro(estoque):
    titulo = input("\nTítulo do livro: ").strip()

    qtd = input("\nQuantidade a adicionar: ")

    while not (qtd.isdigit() and int(qtd) >= 0):
        print("\nA quantidade deve ser um número inteiro e positivo!\n")
        qtd = input("\nQuantidade a adicionar: ")

    if titulo in estoque:
        estoque[titulo] += int(qtd)
    else:
        estoque[titulo] = int(qtd)

    print(f"\n{qtd} unidade(s) de '{titulo}' adicionada(s).\n")

def remover_livro(estoque):
    titulo = input("\nTítulo do livro: ").strip()

    if titulo not in estoque:
        print("\nLivro não encontrado no estoque\n")
        return

    qtd = input("\nQuantidade a remover: ")

    while not (qtd.isdigit() and int(qtd) >= 0):
        print("\nA quantidade deve ser um número inteiro e positivo!\n")
        qtd = input("\nQuantidade a remover: ")

    if int(qtd) > estoque[titulo]:
        print(f"\nNão há unidades suficientes para remover. Estoque atual: {estoque[titulo]}\n")
        return
    
    estoque[titulo] -= int(qtd)

    print(f"\n{qtd} unidade(s) removida(s) de '{titulo}'.\n")

    if estoque[titulo] == 0:
        print(f"\nEstoque do livro '{titulo}' zerado.\n")


def consultar_livro(estoque):
    titulo = input("\nTitulo do livro: ").strip()

    if titulo in estoque:
        print(f"\nQuantidade disponível de '{titulo}': {estoque[titulo]}\n")
    else:
        print("\nLivro não está no estoque.\n")

def mostrar_estoque(estoque):
    if not estoque:
        print("\nEstoque vazio\n")
        return
    
    print("\nLivros em estoque: ")
    for titulo in sorted(estoque.keys()):
        print(f"{titulo}: {estoque[titulo]}")
    print()

def main():
    estoque = {}

    while True:
        print("\n===MENU===\n")
        print("1 - Adicionar livro ao estoque")
        print("2 - Remover unidades de um livro")
        print("3 - Consultar quantidade de um livro")
        print("4 - Mostrar todos os livros com quantidades")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ").strip()

        if opcao == "1":
            adicionar_livro(estoque)
        elif opcao == "2":
            remover_livro(estoque)
        elif opcao == "3":
            consultar_livro(estoque)
        elif opcao == "4":
            mostrar_estoque(estoque)
        elif opcao == "5":
            print("\nEncerrando o programa...\n")
            break
        else: 
            print("\nOpção inválida! Tente novamente.\n")
        



if __name__ == "__main__":
    main()