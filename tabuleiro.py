# PLACAR GERAL
vitorias_j1 = 0
vitorias_j2 = 0
empates = 0
total_partidas = 0

# MENU PRINCIPAL
while True:
    print("\n========== JOGO DA VELHA ==========")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Placar")
    print("4 - Sair")
    print("===================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        vitorias_serie_j1 = 0
        vitorias_serie_j2 = 0

        print("\n========== CAMPEONATO ==========")
        print("Melhor de 3 partidas!")
        print("O primeiro jogador que conseguir 2 vitórias será o campeão.")

        # CAMPEONATO
        while vitorias_serie_j1 < 2 and vitorias_serie_j2 < 2:

            # MATRIZ DO TABULEIRO
            tabuleiro = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ]

            jogador = 1
            vencedor = 0
            jogadas = 0

            # PARTIDA
            while vencedor == 0 and jogadas < 9:

                print("\n========== TABULEIRO ==========")

                # EXIBIÇÃO DO TABULEIRO SEM LINHAS E COLUNAS EXTERNAS
                for i in range(3):
                    for j in range(3):
                        print("|", tabuleiro[i][j], end=" ")
                    print("|")

                # DEFINIR SÍMBOLO DO JOGADOR
                if jogador == 1:
                    simbolo = "X"
                    print("\nVez do JOGADOR 1 (X)")
                else:
                    simbolo = "O"
                    print("\nVez do JOGADOR 2 (O)")

                # ESCOLHER POSIÇÃO
                posicao = input("Escolha uma posição de 1 a 9: ")

                posicao_valida = False

                # VALIDAR ENTRADA
                for n in range(1, 10):
                    if posicao == str(n):
                        posicao_valida = True

                if posicao_valida == False:
                    print("Entrada inválida! Digite um número de 1 a 9.")

                else:
                    numero = int(posicao)

                    linha = (numero - 1) // 3
                    coluna = (numero - 1) % 3

                    # VERIFICAR SE A POSIÇÃO ESTÁ OCUPADA
                    if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "O":
                        print("Essa posição já está ocupada! Escolha outra.")

                    else:
                        tabuleiro[linha][coluna] = simbolo
                        jogadas = jogadas + 1

            # VERIFICAR VITÓRIA NAS LINHAS
                        for i in range(3):
                            if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
                                vencedor = jogador

                        # VERIFICAR VITÓRIA NAS COLUNAS
                        for j in range(3):
                            if tabuleiro[0][j] == simbolo and tabuleiro[1][j] == simbolo and tabuleiro[2][j] == simbolo:
                                vencedor = jogador

                        # VERIFICAR VITÓRIA NAS DIAGONAIS
                        if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
                            vencedor = jogador

                        if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
                            vencedor = jogador

                        # TROCAR DE JOGADOR
                        if vencedor == 0:
                            if jogador == 1:
                                jogador = 2
                            else:
                                jogador = 1

            # MOSTRAR TABULEIRO FINAL
            print("\n========== RESULTADO DA PARTIDA ==========")

            for i in range(3):
                for j in range(3):
                    print("|", tabuleiro[i][j], end=" ")
                print("|")
# =================================================
            # PARTE 3 - PLACAR E DESAFIO
            # RESPONSAVEL: INTEGRANTE 3
            # =================================================

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

            # Limpa a matriz usando for aninhado
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = " "

        # Resultado final do campeonato
        print("\n===== RESULTADO DO CAMPEONATO =====")

        if vitorias_serie_j1 > vitorias_serie_j2:

            print("Jogador X foi o CAMPEAO!")

        elif vitorias_serie_j2 > vitorias_serie_j1:

            print("Jogador O foi o CAMPEAO!")

        else:

            print("O campeonato terminou empatado!")

    elif opcao == "2":

        print("\n========== REGRAS ==========")
        print("1. O jogo possui dois jogadores: X e O.")
        print("2. Os jogadores escolhem posicoes de 1 a 9.")
        print("3. Cada jogador marca uma posicao por vez.")
        print("4. Vence quem completar uma linha, coluna ou diagonal.")
        print("5. Se todas as casas forem preenchidas sem vencedor, ocorre empate.")
        print("6. O campeonato possui ate 3 partidas.")
        print("7. Vence o campeonato quem ganhar 2 partidas.")

    elif opcao == "3":

        print("\n========== PLACAR GERAL ==========")
        print("Vitorias do jogador X:", vitorias_j1)
        print("Vitorias do jogador O:", vitorias_j2)
        print("Empates:", empates_total)

    elif opcao == "4":

        print("\nObrigado por jogar!")
        print("Placar final:")
        print("Vitorias de X:", vitorias_j1)
        print("Vitorias de O:", vitorias_j2)
        print("Empates:", empates_total)

    else:

        print("\nOpcao invalida! Escolha de 1 a 4.")