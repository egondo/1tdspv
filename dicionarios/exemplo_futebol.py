if __name__ == "__main__":
    campeonato = {}
    campeonato['Corinthians'] = 23
    campeonato['Botafogo'] = 21
    campeonato['Palmeiras'] = 30
    campeonato['Flamengo'] = 18

    print(campeonato)

    campeonato['Santos'] = 19
    
    for time in campeonato.keys():
        print(f'{time} pts: {campeonato[time]}')

    
    #Crie um outro dicionario a partir do dicionario acima para armazenar 
    # uma lista contendo o nome do time e os pontos ao inves de apenas os pontos

    camp2 = {}  #criando outro dicionario
    
    #camp2['Corinthians'] = ['Corinthians', 23]
    #camp2['Botafogo'] = ['Botafogo', 21]

    for time in campeonato.keys():
        camp2[time] = [ time, campeonato[time] ]

    print(camp2)