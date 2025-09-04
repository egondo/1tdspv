import velha

def trocaJogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

#criando a matriz tab
tab = []
for i in range(3):
    tab.append([' '] * 3)

player = 'X'

while velha.temEspaco(tab) and not velha.haGanhador(tab):
    velha.imprime(tab)
    print(f"Jogador {player}: ")
    lin = int(input("Linha: "))
    col = int(input("Coluna: "))
    if velha.joga(tab, lin, col, player) == True:
        player = trocaJogador(player)
    else:
        print('Jogada inválida, tente outra posicao')

if velha.haGanhador(tab):
    print(f'Parabéns, {trocaJogador(player)} venceu!')
else:
    print('Deu velha!')