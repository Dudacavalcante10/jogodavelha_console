def criar_tabuleiro():
    """Cria um tabuleiro vazio 3x3 representado por uma lista de listas."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro no console."""
    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def realizar_jogada(tabuleiro, jogador, linha, coluna):
    """Realiza uma jogada no tabuleiro se a posição estiver vazia."""
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Posição ocupada! Tente novamente.")
        return False

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador venceu (linhas, colunas ou diagonais)."""
    # Verificar linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    # Verificar colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    """Verifica se houve empate (tabuleiro cheio sem vencedor)."""
    return all(celula != ' ' for linha in tabuleiro for celula in linha)

def alternar_jogador(jogador_atual):
    """Alterna entre os jogadores 'X' e 'O'."""
    return 'O' if jogador_atual == 'X' else 'X'

def main():
    """Programa principal do Jogo da Velha."""
    # Pedir nomes dos jogadores
    nome_jogador1 = input("Digite o nome do Jogador 1 (X): ")
    nome_jogador2 = input("Digite o nome do Jogador 2 (O): ")
    
    # Inicializar pontuações
    pontuacao = {nome_jogador1: 0, nome_jogador2: 0}
    
    while True:
        # Criar novo tabuleiro para cada jogo
        tabuleiro = criar_tabuleiro()
        jogador_atual = 'X'
        jogador_nome_atual = nome_jogador1
        
        while True:
            mostrar_tabuleiro(tabuleiro)
            print(f"Vez de {jogador_nome_atual} ({jogador_atual})")
            
            # Pedir jogada
            try:
                linha = int(input("Digite a linha (0-2): "))
                coluna = int(input("Digite a coluna (0-2): "))
                if linha not in range(3) or coluna not in range(3):
                    print("Posição inválida! Use 0, 1 ou 2.")
                    continue
            except ValueError:
                print("Entrada inválida! Digite números.")
                continue
            
            # Realizar jogada
            if not realizar_jogada(tabuleiro, jogador_atual, linha, coluna):
                continue
            
            # Verificar vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"{jogador_nome_atual} venceu!")
                pontuacao[jogador_nome_atual] += 1
                break
            
            # Verificar empate
            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("Empate!")
                break
            
            # Alternar jogador
            jogador_atual = alternar_jogador(jogador_atual)
            jogador_nome_atual = nome_jogador1 if jogador_atual == 'X' else nome_jogador2
        
        # Perguntar se querem jogar novamente
        jogar_novamente = input("Jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break
    
    # Mostrar pontuação final
    print("\nPontuação Final:")
    for nome, pontos in pontuacao.items():
        print(f"{nome}: {pontos} vitórias")

# Executar o programa
if __name__ == "__main__":
    main()
