# PARTE 1 - JOGABILIDADE E VALIDACAO
# RESPONSAVEL: Luis Gustavo

opcao = ""

# Placar acumulado
vitorias_j1 = 0
vitorias_j2 = 0
empates_total = 0

# Menu principal
while opcao != "4":

    print("\n========== JOGO DA VELHA ==========")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Ver placar")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":

        print("\n===== CAMPEONATO MELHOR DE 3 =====")
        print("Vence a serie quem ganhar 2 partidas.")

        # Pontuacao da serie
        vitorias_serie_j1 = 0
        vitorias_serie_j2 = 0
        partidas_serie = 0

        # Criacao da matriz, linha por linha
        tabuleiro = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        # A serie termina quando alguem ganhar 2 partidas
        # ou quando forem realizadas 3 partidas.
        while (vitorias_serie_j1 < 2 and
               vitorias_serie_j2 < 2 and
               partidas_serie < 3):

            # Prepara as posicoes do tabuleiro
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = str(i * 3 + j + 1)

            jogador = "X"
            venceu = False
            jogador_vencedor = ""
            jogadas = 0

            print("\n===== NOVA PARTIDA =====")


# PARTE 2 - JOGABILIDADE E VALIDACAO
# RESPONSAVEL: Wagner Vinícius

while venceu == False and jogadas < 9:

    # Exibe o tabuleiro com for aninhado
    for i in range(3):
        for j in range(3):
            print("|", tabuleiro[i][j], end=" ")
        print("|")

        print()

        if i < 2:
            print("             -----------")

    print("\nVez do jogador:", jogador)

    jogada_valida = False

    # Repete ate o jogador informar uma posicao valida
    while jogada_valida == False:

        entrada = input("Escolha uma posicao de 1 a 9: ")

        entrada_valida = False

        # Verifica se a entrada esta entre 1 e 9
        for n in range(1, 10):

            if entrada == str(n):
                entrada_valida = True
                posicao = n

        if entrada_valida == False:

            print("Entrada invalida! Digite um numero de 1 a 9.")

        else:

            # Converte a posicao em linha e coluna
            linha = (posicao - 1) // 3
            coluna = (posicao - 1) % 3

            # Verifica se a casa ja esta ocupada
            if (tabuleiro[linha][coluna] == "X" or
                tabuleiro[linha][coluna] == "O"):

                print("Essa posicao ja esta ocupada!")

            else:

                tabuleiro[linha][coluna] = jogador
                jogadas = jogadas + 1
                jogada_valida = True

    # Verificacao das linhas e colunas
    for i in range(3):

        # Verifica uma linha
        if (tabuleiro[i][0] == jogador and
            tabuleiro[i][1] == jogador and
            tabuleiro[i][2] == jogador):

            venceu = True

        # Verifica uma coluna
        if (tabuleiro[0][i] == jogador and
            tabuleiro[1][i] == jogador and
            tabuleiro[2][i] == jogador):

            venceu = True

    # Verificacao da diagonal principal
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):

        venceu = True

    # Verificacao da diagonal secundaria
    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):

        venceu = True

    # Guarda quem venceu
    if venceu == True:

        jogador_vencedor = jogador

    # Troca o jogador se ainda nao houve vitoria
    else:

        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

    # =================================================
    # EXIBE O TABULEIRO FINAL
    # =================================================

    print("\n===== TABULEIRO FINAL =====")
    print("        COLUNAS")
    print("        1   2   3")

    for i in range(3):

        print("LINHA", i + 1, end="  | ")

        for j in range(3):

            print(tabuleiro[i][j], end="")

            if j < 2:
                print(" | ", end="")

        print()

        if i < 2:
            print("             -----------")

partidas_serie = partidas_serie + 1

if venceu == True:

    print("\nJogador", jogador_vencedor, "venceu a partida!")

    if jogador_vencedor == "X":

        vitorias_j1 = vitorias_j1 + 1
        vitorias_serie_j1 = vitorias_serie_j1 + 1

    else:

        vitorias_j2 = vitorias_j2 + 1
        vitorias_serie_j2 = vitorias_serie_j2 + 1

else:

    # Conta as casas livres usando for aninhado
    casas_livres = 0

    for i in range(3):
        for j in range(3):

            if (tabuleiro[i][j] != "X" and
                tabuleiro[i][j] != "O"):

                casas_livres = casas_livres + 1

    if casas_livres == 0:

        print("\nA partida terminou empatada!")
        empates_total = empates_total + 1

# Exibe o placar acumulado
print("\n===== PLACAR GERAL =====")
print("Vitorias do jogador X:", vitorias_j1)
print("Vitorias do jogador O:", vitorias_j2)
print("Empates:", empates_total)

# Exibe o placar da serie
print("\n===== PLACAR DO CAMPEONATO =====")
print("Vitorias de X:", vitorias_serie_j1)
print("Vitorias de O:", vitorias_serie_j2)
print("Partidas realizadas:", partidas_serie)
