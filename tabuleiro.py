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

# Loop principal da partida
while partida_finalizada == False:

# Exibe o tabuleiro usando for aninhado
 print("\n      COLUNAS")
print("       1   2   3")

for i in range(3):
    print("Linha", i + 1, end=" | ")

    for j in range(3):
        print(tabuleiro[i][j], end=" | ")

    print()

# Define o símbolo do jogador
if jogador == 1:
    simbolo = "X"
    print("\nVez do Jogador 1 (X)")
else:
    simbolo = "O"
    print("\nVez do Jogador 2 (O)")

# Validação da jogada
jogada_valida = False

while jogada_valida == False:

    entrada = input("Escolha uma posição de 1 a 9: ")

    posicao_encontrada = False

    # Confere se a entrada é um número válido
    for n in range(1, 10):

        if entrada == str(n):

            posicao_encontrada = True

            linha = (n - 1) // 3
            coluna = (n - 1) % 3

    if posicao_encontrada == True:

        # Confere se a casa está livre
        if tabuleiro[linha][coluna] != "X" and tabuleiro[linha][coluna] != "O":

            tabuleiro[linha][coluna] = simbolo
            jogada_valida = True

        else:
            print("Essa posição já está ocupada!")

    else:
        print("Entrada inválida! Digite de 1 a 9.")

# Verificação de vitória
venceu = False

# Verificação das linhas
for i in range(3):
    if tabuleiro [i][0] == simbolo and tabuleiro [i][1] == simbolo and tabuleiro [i][2] == simbolo:
        venceu == True

#Verificação das colunas
for j in range (3):

    if tabuleiro[0][j] == simbolo and tabuleiro[1][j] == simbolo and tabuleiro:
        venceu = True

# Verifica as diagonais
if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
    venceu = True

if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
    venceu = True
                
# Se alguém venceu
if venceu == True:

    if jogador == 1:
        print("\nJogador 1 venceu a partida!")
        vitorias_j1 = vitorias_j1 + 1
        vitorias_serie_j1 = vitorias_serie_j1 + 1