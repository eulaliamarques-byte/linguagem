registado = False
consulta = False

while True:
    print("")
    print("MENU")
    print("1 - Registar utente")
    print("2 - Registar consulta")
    print("3 - Ver historico")
    print("4 - Sair")

    opcao = input("Opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        sexo = input("Sexo: ")
        endereco = input("Endereco: ")
        nif = input("NIF: ")
        registado = True
        print("Utente registado")

    elif opcao == "2":
        if registado == True:
            data = input("Data: ")
            diagnostico = input("Diagnostico: ")
            observacoes = input("Observacoes: ")
            consulta = True
            print("Consulta registada")
        else:
            print("Tem de registar um utente primeiro")

    elif opcao == "3":
        if registado == True:
            print("Nome:", nome)
            print("Idade:", idade)
            print("Sexo:", sexo)
            print("Endereco:", endereco)
            print("NIF:", nif)
            if consulta == True:
                print("Data:", data)
                print("Diagnostico:", diagnostico)
                print("Observacoes:", observacoes)
            else:
                print("Sem consultas")
        else:
            print("Nao ha utentes")

    elif opcao == "4":
        print("Adeus")
        break

    else:
        print("Opcao errada")
