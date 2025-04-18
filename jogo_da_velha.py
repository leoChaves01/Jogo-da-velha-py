import random

def imprime_grid(grid):
    print("O status do grid é\n")
    for indice in range(len(grid)):
        print(grid[indice], end=" ")
        if indice == 2 or indice == 5 or indice == 8:
            print("")

def verifica_grid(grid, jogador):

    if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador:
        return 1 if jogador == "X" else 2
    if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador:
        return 1 if jogador == "X" else 2
    if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador:
        return 1 if jogador == "X" else 2

    
    if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador:
        return 1 if jogador == "X" else 2
    if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador:
        return 1 if jogador == "X" else 2
    if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador:
        return 1 if jogador == "X" else 2
    
    
    if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador:
        return 1 if jogador == "X" else 2
    if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador:
        return 1 if jogador == "X" else 2

    return 0

def jogar():
    print("Bem vindo ao jogo da velha!")
    print("Você vai jogar contra o computador.")
    print("Ganha quem conseguir uma linha, coluna ou diagonal do grid com o mesmo símbolo.")
    
    print("Você precisa escolher uma posição no grid para marcar sua jogada, veja o grid:")
    print("_ _ _")
    print("_ _ _")
    print("_ _ _")
    print("Escolha um número de 1 a 9 para sua jogada, conforme o grid a seguir:")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    
    quantidade_escolhas = 0
    grid = ["_"] * 9
    
    while True:
        escolha = int(input("Qual é a sua escolha: "))
        
        while grid[escolha-1] != "_":
            print("Sua escolha foi inválida! Veja como está o grid:")
            imprime_grid(grid)
            escolha = int(input("Qual é a sua escolha: "))
        
        grid[escolha-1] = "X"
        quantidade_escolhas += 1
        
        vencedor = verifica_grid(grid, "X")
        
        if vencedor != 0:
            break
        
        if quantidade_escolhas == 9:
            break
        
        imprime_grid(grid)
        
        escolha_computador = random.randint(1, 9)
        while grid[escolha_computador-1] != "_":
            escolha_computador = random.randint(1, 9)
        
        grid[escolha_computador-1] = "O"
        quantidade_escolhas += 1
        
        vencedor = verifica_grid(grid, "O")
        if vencedor != 0:
            break
        imprime_grid(grid)
    
    if vencedor == 1:
        print("Parabéns, você ganhou!")
    elif vencedor == 2:
        print("Você perdeu, o computador ganhou!")
    else:
        print("Deu velha, ninguém venceu, foi empate!")
    
    imprime_grid(grid)


while True:
    jogar()
    replay = input("Deseja jogar novamente? (s/n): ").lower()
    if replay != "s":
        print("Obrigado por jogar!")
        break