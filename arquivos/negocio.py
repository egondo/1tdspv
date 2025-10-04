import banco

def importa_partidas(lista: list):
    for registro in lista:
        insere_partida(registro)


def insere_partida(partida: dict):
    '''recupero os times pelo nome
    se os dois times nao existirem, cadastro eles no sistema.
    verifico o ganhador da partida, atualizo os dois times com os 
    valores de vitorias, empates ou derrotas mais os gols pro e gols
    levados.
    atualizo o time no banco de dados
    gravo a partida na tabela partida de acordo com os times que se 
    enfrentaram''''
    tc = partida.get('time_casa')
    tv = partida.get('time_visitante')
    time_casa = banco.recupera_pelo_nome(tc)
    if time_casa == None:
        time_casa = banco.insere_time(tc)
    
    time_visitante = banco.recupera_pelo_nome(tv)
    if time_visitante == None:
        time_visitante = banco.insere_time(tv)

    if partida['gols_casa'] > partida['gols_visitante']:
        time_visitante['derrota'] = time_visitante['derrota'] + 1
        time_casa['vitoria'] = time_casa['vitoria'] + 1
    elif partida['gols_casa'] < partida['gols_visitante']:
        time_visitante['vitoria'] = time_visitante['vitoria'] + 1
        time_casa['derrota'] = time_casa['derrota'] + 1
    else:
        time_visitante['empate'] = time_visitante['empate'] + 1
        time_casa['empate'] = time_casa['empate'] + 1

    time_visitante['gol_pro'] += partida['gols_visitante']
    time_casa['gol_pro'] += partida['gols_casa']

    time_visitante['gol_contra'] += partida['gols_casa']
    time_casa['gol_contra'] += partida['gols_visitante']

    banco.atualiza_time(time_casa)
    banco.atualiza_time(time_visitante)

    banco.insere_partida(partida)