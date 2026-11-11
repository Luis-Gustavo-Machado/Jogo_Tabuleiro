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

            # CONTABILIZAR RESULTADO
            total_partidas = total_partidas + 1

            if vencedor == 1:
                print("\nJOGADOR 1 VENCEU A PARTIDA!")
                vitorias_j1 = vitorias_j1 + 1
                vitorias_serie_j1 = vitorias_serie_j1 + 1

            elif vencedor == 2:
                print("\nJOGADOR 2 VENCEU A PARTIDA!")
                vitorias_j2 = vitorias_j2 + 1
                vitorias_serie_j2 = vitorias_serie_j2 + 1

            else:
                print("\nA PARTIDA TERMINOU EM EMPATE!")
                empates = empates + 1

            # PLACAR GERAL
            print("\n========== PLACAR GERAL ==========")
            print("Vitórias do Jogador 1:", vitorias_j1)
            print("Vitórias do Jogador 2:", vitorias_j2)
            print("Empates:", empates)
            print("Total de partidas:", total_partidas)

            # PLACAR DO CAMPEONATO
            print("\n========== PLACAR DO CAMPEONATO ==========")
            print("Jogador 1:", vitorias_serie_j1, "vitórias")
            print("Jogador 2:", vitorias_serie_j2, "vitórias")

        # RESULTADO DO CAMPEONATO
        print("\n========== RESULTADO FINAL ==========")

        if vitorias_serie_j1 == 2:
            print("JOGADOR 1 É O CAMPEÃO!")

        else:
            print("JOGADOR 2 É O CAMPEÃO!")

    elif opcao == "2":
        print("\n========== REGRAS DO JOGO ==========")
        print("1 - O jogo possui dois jogadores.")
        print("2 - O Jogador 1 utiliza o símbolo X.")
        print("3 - O Jogador 2 utiliza o símbolo O.")
        print("4 - Cada jogador escolhe uma posição de 1 a 9.")
        print("5 - Não é permitido escolher uma posição ocupada.")
        print("6 - Vence quem formar uma sequência de três símbolos.")
        print("7 - A sequência pode ser horizontal, vertical ou diagonal.")
        print("8 - Se todas as posições forem preenchidas sem vencedor, ocorre empate.")
        print("9 - O campeonato é decidido por melhor de 3 partidas.")
        print("10 - O primeiro jogador a conseguir 2 vitórias é o campeão.")

    elif opcao == "3":
        print("\n========== PLACAR GERAL ==========")
        print("Vitórias do Jogador 1:", vitorias_j1)
        print("Vitórias do Jogador 2:", vitorias_j2)
        print("Empates:", empates)
        print("Total de partidas:", total_partidas)

    elif opcao == "4":
        print("\n========== RESULTADO FINAL ==========")
        print("Total de partidas:", total_partidas)
        print("Vitórias do Jogador 1:", vitorias_j1)
        print("Vitórias do Jogador 2:", vitorias_j2)
        print("Empates:", empates)
        print("\nObrigado por jogar!")
        break

    else:
        print("\nOpção inválida! Escolha uma opção de 1 a 4.")