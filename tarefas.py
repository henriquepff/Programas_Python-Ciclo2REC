def adicionar_tarefa(tarefas):
    descricao = input("\nDescrição da tarefa: ")

    prioridade = input("\nPrioridade (1-5, 1 = mais alta): ")
    while not (prioridade.isdigit() and 1 <= int(prioridade) <= 5):
        print("\nPor favor, digite um número inteiro entre 1 e 5.\n")
        prioridade = input("\nPrioridade (1-5, 1 = mais alta): ")

    tarefa = {
        "descrição": descricao,
        "prioridade": prioridade,
        "status": "pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa adicionada com sucesso!\n")


def pegar_prioridade(tarefa):
    return tarefa["prioridade"]

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.\n")
        return
    
    tarefas.sort(key=pegar_prioridade)
    
    print("\nTAREFAS:\n")
    for i in range(len(tarefas)):
        t = tarefas[i]
        print(f"\n{i + 1}. {t["descrição"]} [Prioridade: {t["prioridade"]}] - Status: {t["status"]}")
    print()


def marcar_concluida(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.\n")
        return
    
    listar_tarefas(tarefas)

    escolha = input("\nDigite o número da tarefa concluída: ")
    while not (escolha.isdigit() and 1 <= int(escolha) <= len(tarefas)):
        print("\nNúmero inválido, tente novamente.\n")
        escolha = input("\nDigite o número da tarefa concluída: ")

    indice = int(escolha) - 1

    tarefas[indice]["status"] = "concluída"

    print("\nTarefa marcada como concluída!\n")

def main():
    tarefas = []

    while True:
        print("\n===Menu Gerenciador de Tarefas===\n")
        print("1 - Adicionar tarefas")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            print("\nSaindo do programa. Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")



if __name__ == "__main__":
    main()