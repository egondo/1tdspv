import random

def criar() -> list:
    monte = []
    naipes = "♥♦♣♠"
    for valor in range(1, 14):
        for naipe in naipes:
            carta = (valor, naipe)
            monte.append(carta)

    return monte

def embaralhar(monte: list):
    for i in range(200):
        p1 = random.randint(0, len(monte) - 1)
        p2 = random.randint(0, len(monte) - 1)
        aux = monte[p1]
        monte[p1] = monte[p2]
        monte[p2] = aux

def comprar(monte: list) -> tuple:
    return monte.pop()

def distribuir(monte: list, qtd: int) -> list:
    resp = []
    while qtd > 0:
        resp.append(comprar(monte))
        qtd = qtd - 1
    return resp

#MAIN
if __name__ == "__main__":
    deck = criar()    
    print(deck)

    embaralhar(deck)
    print(deck)

    mao_poker = distribuir(deck, 5)
    print(mao_poker)