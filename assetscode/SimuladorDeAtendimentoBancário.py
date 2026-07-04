senha = 0
fila = []
atendidos = 0
tempo_espera = 0
total_desistentes = 0

while True:
    print("\nMenu:")
    print("G - Gerar senha comum")
    print("P - Gerar senha preferencial")
    print("C - Chamar próximo cliente")
    print("A - Avançar tempo")
    print("F - Exibir fila")
    print("E - Exibir estatísticas")
    print("S - Sair")

    escolha = input("Escolha uma opção: ").upper()

    if escolha == 'G':
        senha += 1
        tipo = 'C'
        temp = 0
        status = []
        status.append(senha)
        status.append(tipo)
        status.append(temp)
        fila.append(status)
        print(f"Senha {senha} gerada para cliente comum.")

    elif escolha == 'P':
        senha += 1
        tipo = 'P'
        temp = 0
        status = []
        status.append(senha)
        status.append(tipo)
        status.append(temp)
        fila.append(status)
        print(f"Senha {senha} gerada para cliente preferencial.")

    elif escolha == 'C':
        encontrou = False
        for cliente in fila:
            if cliente[1] == "P" and cliente[2] >= 8:
                chamar = cliente
                encontrou = True
                break      
        if encontrou == False:
            for cliente in fila:
                if cliente[1] == "C" and cliente[2] >= 8:
                    chamar = cliente
                    encontrou = True
                    break
        if encontrou == False:    
            for cliente in fila:
                if cliente[1] == "P":
                    chamar = cliente
                    encontrou = True
                    break
        if encontrou == False:   
            for cliente in fila:
                if cliente[1] == "C":
                    chamar = cliente
                    encontrou = True   
                    break
        
        if encontrou == False:
            print("Não há clientes na fila.")
            

        if encontrou == True:
            print("Cliente chamado:")
            print("Senha", chamar[0], "| Tipo", chamar[1], "| Espera", chamar[2])
            tempo_espera += chamar[2]
            fila.remove(chamar)
            atendidos += 1
            
        
    elif escolha == 'A':
        for cliente in fila:
            cliente[2] += 1
        
        desistentes = []

        for cliente in fila:
            if cliente[2] >= 10:
                desistentes.append(cliente)

        for cliente in desistentes:
            print("Cliente desistiu:")
            print("Senha", cliente[0], "| Tipo", cliente[1], "| Espera", cliente[2])
            fila.remove(cliente)
            total_desistentes += 1

    elif escolha == 'F':
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            print("Fila atual:")
            for cliente in fila:
                print("Senha", cliente[0], "| Tipo", cliente[1], "| Espera", cliente[2])

    elif escolha == 'E':
        print("Total de senhas geradas:", senha)
        print("Total de clientes atendidos:", atendidos)
        print("Total de clientes desistentes:", total_desistentes)
        print("Quantidade de clientes na fila:", len(fila))
        if atendidos > 0:
            tempo_espera_medio = tempo_espera / atendidos
            print(f"Tempo médio de espera: {tempo_espera_medio:.2f}")
        else:
             print("Ainda não houve atendimentos para calcular o tempo médio de espera.")
    
    elif escolha == 'S':
        print("Encerrando o programa.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")