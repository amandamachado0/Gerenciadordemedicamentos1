#Permitirá cadastrar medicamentos com nome, validade, quantidade e tambémdefinir horários Controlar, organizar, facilitar o registro de entradas e saídas de medicamentos, com data e horário Avisar quando algum medicamento estiver perto de vencer e quando estiver acabando (controle de estoque

import datetime

# Lista para armazenar os medicamentos
medicamentos = []

# Função para cadastrar medicamento
def cadastrar_medicamento():
    nome = input("Nome do medicamento: ")
    validade = input("Data de validade (dd/mm/aaaa): ")
    quantidade = int(input("Quantidade em estoque: "))
    horarios = input("Horários (ex: 08:00,13:00): ").split(',')

    medicamento = {
        "nome": nome,
        "validade": datetime.datetime.strptime(validade, "%d/%m/%Y"),
        "quantidade": quantidade,
        "horarios": horarios
    }

    medicamentos.append(medicamento)
    print("Medicamento cadastrado com sucesso!")

# Função para registrar entrada de medicamento
def registrar_entrada():
    nome = input("Digite o nome do medicamento para entrada: ")
    encontrado = False
    for m in medicamentos:
        if m["nome"].lower() == nome.lower():
            qtd = int(input("Quantidade a adicionar: "))
            m["quantidade"] += qtd
            print("Entrada registrada. Estoque atual:", m["quantidade"])
            encontrado = True
            break
    if not encontrado:
        print("Medicamento não encontrado.")

# Função para registrar saída de medicamento
def registrar_saida():
    nome = input("Digite o nome do medicamento para saída: ")
    encontrado = False
    for m in medicamentos:
        if m["nome"].lower() == nome.lower():
            if m["quantidade"] > 0:
                m["quantidade"] -= 1
                print("Saída registrada. Estoque atual:", m["quantidade"])
            else:
                print("Estoque zerado!")
            encontrado = True
            break
    if not encontrado:
        print("Medicamento não encontrado.")

# Verificar validade e estoque baixo
def verificar_alertas():
    hoje = datetime.datetime.now()
    for m in medicamentos:
        dias = (m["validade"] - hoje).days
        if dias <= 7:
            print(f"ALERTA: '{m['nome']}' vence em {dias} dias!")
        if m["quantidade"] <= 3:
            print(f"ALERTA: Estoque baixo de '{m['nome']}': {m['quantidade']} unidades")

# Menu principal
def menu():
    while True:
        print("\n=== CONTROLE DE MEDICAMENTOS ===")
        print("1 - Cadastrar medicamento")
        print("2 - Registrar entrada")
        print("3 - Registrar saída")
        print("4 - Verificar alertas")
        print("5 - Listar todos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_medicamento()
        elif opcao == "2":
            registrar_entrada()
        elif opcao == "3":
            registrar_saida()
        elif opcao == "4":
            verificar_alertas()
        elif opcao == "5":
            for m in medicamentos:
                print(f"{m['nome']} | Validade: {m['validade'].strftime('%d/%m/%Y')} | Estoque: {m['quantidade']} | Horários: {', '.join(m['horarios'])}")
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

# Executa o programa
menu()
