# Placar dos jogadores
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