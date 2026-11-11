# Placar geral
vitorias_j1 = 0
vitorias_j2 = 0
empates = 0
total_partidas = 0

# Menu principal
opcao = "0"

while opcao != "4":

    print("\n========== JOGO DA VELHA ==========")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")
    print("===================================")

    opcao_valida = False

    while opcao_valida == False:
        entrada = input("Escolha uma opção: ")

        for n in range(1, 5):
            if entrada == str(n):
                opcao = entrada
                opcao_valida = True

        if opcao_valida == False:
            print("Opção inválida! Digite de 1 a 4.")

    # OPÇÃO 1 - JOGAR
    if opcao == "1":

        vitorias_serie_j1 = 0
        vitorias_serie_j2 = 0

        print("\nCAMPEONATO MELHOR DE 3!")
        print("Vence quem ganhar 2 partidas primeiro.")

        # Repete enquanto ninguém alcançar 2 vitórias
        while vitorias_serie_j1 < 2 and vitorias_serie_j2 < 2:

            # Matriz do tabuleiro
            tabuleiro = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ]

            jogador = 1
            partida_finalizada = False

print("\n========== NOVA PARTIDA ==========")

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