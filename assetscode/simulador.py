# simulador de investimento

def pedir_float(mensagem, positivo=True):
    while True:
        try:
            valor = float(input(mensagem))
            if positivo and valor < 0:
                print("O valor não pode ser negativo.")
            else:
                return valor
        except ValueError:
            print("Digite um número válido.")

def pedir_int(mensagem, positivo=True):
    while True:
        try:
            valor = int(input(mensagem))
            if positivo and valor <= 0:
                print("O valor deve ser positivo.")
            else:
                return valor
        except ValueError:
            print("Digite um número inteiro válido.")

def fmt(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def pedir_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Digite S ou N.")

def rodar_simulacao(valorf, valorinvestido, valord, valormensal, taxa, tempo, ano):
    mes = 0
    valorextra = 0
    pediu_extra = False

    for i in range(tempo):
        mes += 1

        juros = valorf * (taxa / 100)
        valord += juros
        valorf += juros + valormensal
        valorinvestido += valormensal

        if mes == 7 and not pediu_extra:
            valorextra = pedir_float("Digite o valor extra a ser investido em dezembro: ")
            pediu_extra = True

        if mes == 12 or i == tempo - 1:
            investido_ano = valorinvestido
            juros_ano = valord

            if mes == 12:
                valorf += valorextra
                valorinvestido += valorextra
                print(f"\n {'='*40}")
                print(f"  RELATÓRIO — Ano {ano}")
                print(f" {'='*40}")
                print(f"  Aporte extra de dezembro: R$ {fmt(valorextra)}")
                print(f"  Total investido até agora: R$ {fmt(valorinvestido)}")
                print(f"  Total de juros até agora:  R$ {fmt(valord)}")
                print(f"  Patrimônio atual:          R$ {fmt(valorf)}")
                print(f" {'='*40}\n")

                valorextra = 0
                pediu_extra = False
                mes = 0
                ano += 1

                if i < tempo - 1:
                    if pedir_sim_nao("Deseja alterar o valor mensal para o próximo ano? (S/N): "):
                        valormensal = pedir_float(f"Digite o novo valor mensal a partir de {ano}: ")
            else:
                # relatório parcial no último mês se não fechar ano completo
                print(f"\n {'='*40}")
                print(f"  RELATÓRIO PARCIAL — Ano {ano} (Mês {mes})")
                print(f" {'='*40}")
                print(f"  Total investido até agora: R$ {fmt(valorinvestido)}")
                print(f"  Total de juros até agora:  R$ {fmt(valord)}")
                print(f"  Patrimônio atual:          R$ {fmt(valorf)}")
                print(f" {'='*40}\n")

    return valorf, valorinvestido, valord, valormensal, taxa, ano, mes

# --- início ---
valorinicial  = pedir_float("Digite o valor inicial do investimento: ")
valormensal   = pedir_float("Digite o valor mensal a ser investido: ")
taxa          = pedir_float("Digite a taxa de juros (em %): ")
tempo         = pedir_int("Digite o tempo de investimento (em meses): ")
ano           = pedir_int("Digite o ano inicial do investimento: ")

valorf        = valorinicial
valorinvestido = valorinicial
valord        = 0

valorf, valorinvestido, valord, valormensal, taxa, ano, mes = rodar_simulacao(
    valorf, valorinvestido, valord, valormensal, taxa, tempo, ano
)

# --- opção de continuar ---
while pedir_sim_nao("\nDeseja continuar o investimento adicionando mais meses? (S/N): "):
    tempo_extra = pedir_int("Quantos meses a mais deseja simular? ")
    if pedir_sim_nao("Deseja alterar o valor mensal? (S/N): "):
        valormensal = pedir_float("Digite o novo valor mensal: ")

    valorf, valorinvestido, valord, valormensal, taxa, ano, mes = rodar_simulacao(
        valorf, valorinvestido, valord, valormensal, taxa, tempo_extra, ano
    )

# --- resumo final ---
print(f"\n {'#'*40}")
print(f"  RESUMO FINAL")
print(f" {'#'*40}")
print(f"  Total investido:        R$ {fmt(valorinvestido)}")
print(f"  Total de juros:         R$ {fmt(valord)}")
print(f"  Patrimônio final:       R$ {fmt(valorf)}")
print(f"  Rendimento próximo mês: R$ {fmt(valorf * (taxa / 100))}")
print(f" {'#'*40}\n")