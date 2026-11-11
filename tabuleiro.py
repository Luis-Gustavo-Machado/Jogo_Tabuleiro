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

while venceu == False and jogadas < 9:

    # Exibe o tabuleiro com for aninhado
    for i in range(3):
        for j in range(3):
            print("|", tabuleiro[i][j], end=" ")
        print("|")

        if i < 2:
            print("------------")

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

#Exibe o tabuleiro final

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
