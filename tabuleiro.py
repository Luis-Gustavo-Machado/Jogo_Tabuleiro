
# =====================================
#           JOGO DA VELHA
# =====================================

# Placar geral
vitorias_x = 0
vitorias_o = 0
empates = 0

total_partidas = 0

opcao = "0"

# Menu principal
while opcao != "3":

    print("\n========================")
    print("      JOGO DA VELHA")
    print("========================")
    print("1 - Jogar")
    print("2 - Ver placar")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        # Configuração do campeonato
        print("\n1 - Partida única")
        print("2 - Campeonato melhor de 3")

        modo = input("Escolha o modo de jogo: ")

        if modo == "1" or modo == "2":

            # Pontuação do campeonato atual
            pontos_x = 0
            pontos_o = 0

            jogar = True

            if modo == "1":
                limite = 1
            else:
                limite = 3

            # Repetição das partidas
            while jogar == True:

                # Criando a matriz do tabuleiro
                tabuleiro = [
                    [" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]
                ]

                jogador = "X"
                venceu = False
                vazias = 9

                print("\nNova partida!")

                # Enquanto ninguém vencer e houver casas vazias
                while venceu == False and vazias > 0:

                    # Exibindo o tabuleiro
                    print("\n       TABULEIRO")
                    print("       1   2   3")

                    for i in range(3):
                        print("   ", end="")

                        for j in range(3):
                            if tabuleiro[i][j] == " ":
                                print(" " + str(i * 3 + j + 1), end="")
                            else:
                                print(" " + tabuleiro[i][j], end=" ")

                            if j < 2:
                                print(" |", end="")

                        print()

                        if i < 2:
                            print("      -----------")

                    # Vez do jogador
                    print("\nVez do jogador", jogador)

                    # Validação da posição
                    valida = False

                    while valida == False:

                        entrada = input("Escolha uma posição (1 a 9): ")

                        for n in range(1, 10):
                            if entrada == str(n):
                                posicao = n
                                valida = True

                        if valida == False:
                            print("Posição inválida! Digite de 1 a 9.")

                    # Transformando posição em linha e coluna
                    linha = (posicao - 1) // 3
                    coluna = (posicao - 1) % 3

                    # Verificando se a posição está ocupada
                    if tabuleiro[linha][coluna] != " ":
                        print("Essa posição já está ocupada!")

                    else:

                        # Registrando a jogada
                        tabuleiro[linha][coluna] = jogador
                        vazias = vazias - 1

                        # Verificando linhas e colunas
                        for i in range(3):

                            if (tabuleiro[i][0] == jogador and
                                tabuleiro[i][1] == jogador and
                                tabuleiro[i][2] == jogador):
                                venceu = True

                            if (tabuleiro[0][i] == jogador and
                                tabuleiro[1][i] == jogador and
                                tabuleiro[2][i] == jogador):
                                venceu = True

                        # Verificando as diagonais
                        if (tabuleiro[0][0] == jogador and
                            tabuleiro[1][1] == jogador and
                            tabuleiro[2][2] == jogador):
                            venceu = True

                        if (tabuleiro[0][2] == jogador and
                            tabuleiro[1][1] == jogador and
                            tabuleiro[2][0] == jogador):
                            venceu = True

                        # Verificando o resultado
                        if venceu == True:

                            print("\nJogador", jogador, "venceu!")

                            if jogador == "X":
                                vitorias_x = vitorias_x + 1
                                pontos_x = pontos_x + 1
                            else:
                                vitorias_o = vitorias_o + 1
                                pontos_o = pontos_o + 1

                            total_partidas = total_partidas + 1

                        elif vazias == 0:

                            print("\nDeu empate!")

                            empates = empates + 1
                            total_partidas = total_partidas + 1

                        else:

                            # Alternando os jogadores
                            if jogador == "X":
                                jogador = "O"
                            else:
                                jogador = "X"

                # Mostrando o tabuleiro final
                print("\nResultado final:")

                for i in range(3):

                    for j in range(3):
                        print("[" + tabuleiro[i][j] + "]", end=" ")

                    print()

                # Resultado do campeonato
                print("\nPlacar do campeonato:")
                print("Jogador X:", pontos_x)
                print("Jogador O:", pontos_o)

                if modo == "1":
                    jogar = False

                elif pontos_x == 2 or pontos_o == 2:
                    jogar = False

                else:
                    resposta = input("\nDesejam continuar? (s/n): ")

                    if resposta != "s" and resposta != "S":
                        jogar = False

            # Campeão do campeonato
            if modo == "2":

                print("\n===== RESULTADO DO CAMPEONATO =====")

                if pontos_x > pontos_o:
                    print("Jogador X é o campeão!")

                elif pontos_o > pontos_x:
                    print("Jogador O é o campeão!")

                else:
                    print("O campeonato terminou empatado!")

        else:
            print("\nModo inválido!")

    elif opcao == "2":

        # Exibindo o placar geral
        print("\n======= PLACAR GERAL =======")
        print("Jogador X:", vitorias_x, "vitórias")
        print("Jogador O:", vitorias_o, "vitórias")
        print("Empates:", empates)
        print("Total de partidas:", total_partidas)

    elif opcao == "3":

        print("\n======= RESULTADO FINAL =======")
        print("Jogador X:", vitorias_x, "vitórias")
        print("Jogador O:", vitorias_o, "vitórias")
        print("Empates:", empates)
        print("Total de partidas:", total_partidas)
        print("\nObrigado por jogar!")

    else:
        print("\nOpção inválida! Tente novamente.")
