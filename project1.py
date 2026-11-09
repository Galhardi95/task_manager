import json

tarefas = [{
            "id": 0, 
            "titulo": "Adicionar 100 reais", 
            "concluida": True
            },
            {
            "id": 1, 
            "titulo": "Fazer 50 abdominais", 
            "concluida": False
            },
            {
            "id": 2, 
            "titulo": "Testar a nova consulta", 
            "concluida": True
            }]

# print(tarefas[0]["titulo"]) # Acessar uma informação específica da tarefa
# print(tarefas[1])
# print(tarefas[2])

def carregar_lista():

    arq = input("Digite o nome do bloco de tarefas que deseja acessar: ")
    # arq = 'tarefas_teste.json'
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
            # print(dados)

    except FileNotFoundError:
        print(" Erro: Nenhum arquivo foi encontrado! ")

def salvar_tarefas():
    try:
        with open (arq, 'w', encoding='utf-8') as arquivo:
            dados 


def listar_tarefas(dados):
    # print("----------- Tarefas que requerem a sua atenção -----------")
    for tarefa in dados:
        if(tarefa["concluida"]):
            simbolo = "[X]"
        else:
            simbolo = "[ ]"

        print(f"{simbolo} {tarefa['id']} - {tarefa['titulo']}")
# listar_tarefas(tarefas)
#. Uma dica: existe uma função do Python que devolve o maior valor de uma coleção, e dá para aplicá-la aos ids existentes.

def adicionar_tarefa(tarefas):
    proximo_id = max(
        (tarefa["id"] for tarefa in tarefas),
        default=0
    ) + 1

    novo_titulo = input(' Digite o titulo da nova tarefa: ').strip()
    if not novo_titulo:
        print("TÍTULO NAO PODE SER VAZIO!")
        # sys.exit() #Interrompe o programa / No entento, se o usuario apertasse o ENTER sem querer, o programa seria fechado.
        return

    nova_tarefa = {
        "id": proximo_id,
        "titulo": novo_titulo,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    print("Nova tarefa adicionada!")

# adicionar_tarefa(tarefas)
# print(tarefas)

def concluir_tarefa (tarefas):
    #Busca a tarefa conforme o id digitado
    #Confirma se a tarefa ja nao foi concluida
        #Se nao for False -> True
        #Se ja for True -> Tarefa ja se encontra concluida!
    listar_tarefas(tarefas)
    entrada = input("Digite o numero da tarefa a ser concuido: ").strip()

    if not entrada.isdigit():
        print(" Digite um ID numérico válido! ")
        return

    id_digitado = int(entrada)

    for tarefa in tarefas:       
        if id_digitado == int(tarefa["id"]) and tarefa["concluida"] == False:
            tarefa["concluida"] = True
            print("Tarefa concluida com sucesso")
            return         
            
    print(" Tarefa nao encontrado ou, ja concluida.")
# concluir_tarefa(tarefas)


def excluir_tarefa(tarefas):
    #Solicitar o id da tarefa a ser excluida
    #Percorrer todas as tarefas e verificar se possui uma tarefa com esse id
        #Se existir, excluir a tarefa
            #Tarefa excluida com sucesso!
        #Se nao existir:
            #Nenhuma tarefa com esse id foi encontrada. Digite um ID válido.
    
    listar_tarefas(tarefas)
    entrada_excluir = input('Digite o ID da tarefa a ser excluida: ').strip()

    if not entrada_excluir.isdigit():
        print("Digite um ID numérico válido")
        return()

    excluir_id = int(entrada_excluir)

    for indice, tarefa in enumerate(tarefas):
        if excluir_id == int(tarefa["id"]):
            del tarefas[indice]
            print(tarefas)
            print("Tarefa excluída com sucesso!")
            return

    print("Nao encontramos nenhuma tarefa com esse id.")

# excluir_tarefa(tarefas)


# carregar_lista()
while True:
    carregar_lista()
    print("----------------------- GERENCIADOR DE TAREFAS -----------------------")
    print("Selecione a opçao desejada")
    print("1 - Adicionar uma nova tarefa") 
    print("2 - Visualizar todas as tarefas")3
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção (1-5): ")

    if( opcao == "1"):
        adicionar_tarefa(tarefas)
    
    elif opcao == "2":
        listar_tarefas(tarefas)

    elif opcao == "3":
        concluir_tarefa(tarefas)

    elif opcao == "4":
        excluir_tarefa(tarefas)

    elif opcao == "5":
        print("Programa encerrado")
        break
    else:
        print(" Numero digitado é inválido! ")