'''Exemplos:
times = {
    'Corinthians': {
        'gols_pro': 15,
        'gols_con': 8,
        'vitorias': 4,
        'empates': 2,
        'derrotas': 2
    },
    'Palmeiras': {
        'gols_pro': 23,
        'gols_con': 14,
        'vitorias': 6,
        'empates': 1,
        'derrotas': 0
    }
}
'''

def processa_linha(info: str) -> dict:
    campos = info.strip().split(";")
    resp = {
        'casa': campos[0],
        'gols_casa': int(campos[1]),
        'visitante': campos[2],
        'gols_visitante': int(campos[3])
    }
    return resp


def define_resultado(partida: dict) -> int:
    #1 se o time da casa venceu
    #0 se a partida empatou
    #-1 se o time visitante venceu
    if partida['gols_casa'] > partida['gols_visitante']:
        return 1
    elif partida['gols_casa'] < partida['gols_visitante']:
        return -1
    else:
        return 0
    
def recupera_time(times: dict, nome: str) -> dict:
    if not nome in times:
        times[nome] = {'gols_pro': 0, 'gols_con': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0}

    return times[nome]

def atualiza_resultado_time(time: dict, gols_feitos, gols_levados, resultado):
    time['gols_pro'] = time['gols_pro'] + gols_feitos
    time['gols_con'] = time['gols_con'] + gols_levados
    if resultado == 'G':
        time['vitorias'] = time['vitorias'] + 1
    elif resultado == 'E':
        time['empates'] = time['empates'] + 1
    else:
        time['derrotas'] = time['derrotas'] + 1


#dicionario contendo os times do campeonato
times = {}
#lista de partidas, armazena um dicionário da partida
partidas = []

with open('partidas.txt', mode='r', encoding="utf8") as arquivo:
    dados = arquivo.readlines()

for linha in dados:
    partida = processa_linha(linha) 
    #print(partida)
    partidas.append(partida)
    gc = partida['gols_casa']
    gv = partida['gols_visitante']

    valor = define_resultado(partida)
    time_casa = recupera_time(times, partida['casa'])
    time_visi = recupera_time(times, partida['visitante'])

    if valor == 1: #time da casa venceu
        res_casa = 'G'
        res_visi = 'P'
    elif valor == 0:
        res_casa = 'E'
        res_visi = 'E'
    else:
        res_casa = 'P'
        res_visi = 'G'

    atualiza_resultado_time(time_casa, gc, gv, res_casa)
    atualiza_resultado_time(time_visi, gv, gc, res_visi)

for nome in times.keys():
    print(times[nome])