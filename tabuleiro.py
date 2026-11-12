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

        # Escolher o tipo do campeonato
        vitorias_serie_j1 = 0
        vitorias_serie_j2 = 0

        print("\n========== CAMPEONATO ==========")
        print("1 - Melhor de 3 partidas!")
        print("2 - Melhor de 5 partidas")

        opcao_campeonato = input('Escolha o campeonanto: ')

        while opcao_campeonato != '1' and opcao_campeonato != '2':
            print('Opção inválida!')
            opcao_campeonato = input('Escolha 1 ou 2: ')
        if opcao_campeonato == '1':
            vitorias_necessarias = 2
            print('Campeonato melhor de 3!')
        else:
            vitorias_necessarias = 3
            print('Campeonato melhor de 5!')

            vitorias_serie_j1 = 0
            vitorias_serie_j2 = 0

        print('O primeiro jogador a conseguir', vitorias_necessarias, 'vitórias será o campeão!')

        # MATRIZ DO TABULEIRO
        tabuleiro = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
            ]
        
        # CAMPEONATO
        while vitorias_serie_j1 < vitorias_necessarias and vitorias_serie_j2 < vitorias_necessarias:

            #Limpa e reinicia o tabuleiro com for aninhado
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = str(i * 3 + j + 1)

            jogador = 1
            vencedor = 0
            empate = False
            jogadas = 0

            # PARTIDA
            while vencedor == 0 and not empate and jogadas < 9:

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

                # ESCOLHER E VALIDAR POSIÇÃO
                posicao_valida = False

                while not posicao_valida:

                    posicao = input("Escolha uma posição de 1 a 9: ")

                    numero_encontrado = False

                    # VALIDAR SE A ENTRADA É UM NÚMERO DE 1 A 9
                    for n in range(1, 10):
                        if posicao == str(n):
                            numero_encontrado = True

                            numero = int(posicao)

                            linha = (numero - 1) // 3
                            coluna = (numero - 1) % 3

                            # VERIFICAR SE A CASA ESTÁ LIVRE
                            if not (tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "O"):
                                posicao_valida = True

                            else:
                                print("Essa posição já está ocupada! Escolha outra.")

                    if not numero_encontrado:
                        print("Entrada inválida! Digite um número de 1 a 9.")

                # MARCAR JOGADA
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

                # VERIFICAR EMPATE COM FOR ANINHADO
                vazias = 0

                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] != "X" and tabuleiro[i][j] != "O":
                            vazias = vazias + 1

                if vazias == 0 and vencedor == 0:
                    empate = True

                # TROCAR DE JOGADOR
                if vencedor == 0 and not empate:
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

        if vitorias_serie_j1 == vitorias_necessarias:
            print("JOGADOR 1 É O CAMPEÃO!")

        else:
            print("JOGADOR 2 É O CAMPEÃO!")

    elif opcao == "2":
        print("\n========== REGRAS DO JOGO ==========")
        print("1 - O jogo possui dois jogadores.")
        print("2 - O Jogador 1 utiliza o X.")
        print("3 - O Jogador 2 utiliza o O.")
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

        if total_partidas > 0:
                porcentagem_j1 = (vitorias_j1 / total_partidas) * 100
                porcentagem_j2 = (vitorias_j2 / total_partidas) * 100

                print("Porcentagem de vitórias do Jogador 1:", porcentagem_j1, "%")
                print("Porcentagem de vitórias do Jogador 2:", porcentagem_j2, "%")

        else:
            print("Ainda não existem partidas para calcular porcentagens.")

    elif opcao == "4":

        print("\n========== RESULTADO FINAL ==========")
        print("Total de partidas:", total_partidas)
        print("Vitórias do Jogador 1:", vitorias_j1)
        print("Vitórias do Jogador 2:", vitorias_j2)
        print("Empates:", empates)

        if total_partidas > 0:
            porcentagem_j1 = (vitorias_j1 / total_partidas) * 100
            porcentagem_j2 = (vitorias_j2 / total_partidas) * 100

            print("Porcentagem de vitórias do Jogador 1:", porcentagem_j1, "%")
            print("Porcentagem de vitórias do Jogador 2:", porcentagem_j2, "%")

        print("\nObrigado por jogar!")
        break

    else:
        print("\nOpção inválida! Escolha uma opção de 1 a 4.")