import baralho

def get_pontos(mao) -> int:
    pontos = 0
    for carta in mao:
        if carta[0] > 10:
            pontos = pontos + 10
        else:
            pontos = pontos + carta[0]
    return pontos

def quer_carta(mao) -> bool:
    print(mao)
    print(f"Pontos : {get_pontos(mao)}")
    resp = input("Voce quer mais cartas (s/n)?")
    if resp == 'S' or resp == 's':
        return True
    return False

def quer_carta_cpu(mao) -> bool:
    if get_pontos(mao) < 15:
        return True
    else:
        return False


deck = baralho.criar()
baralho.embaralhar(deck)
mao_hum = baralho.distribuir(deck, 2)
mao_cpu = baralho.distribuir(deck, 2)

while quer_carta(mao_hum):
    c = baralho.comprar(deck)
    mao_hum.append(c)

while quer_carta_cpu(mao_cpu):
    c = baralho.comprar(deck)
    mao_cpu.append(c)

pontos_hum = get_pontos(mao_hum)    
pontos_cpu = get_pontos(mao_cpu)

print(mao_hum)
print(f"Pontos: {pontos_hum}")

print(mao_cpu)
print(f"Pontos: {pontos_cpu}")
