def fatorial(n):
    if  n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


campeonato = {}
campeonato['Corinthians'] = 23
campeonato['Botafogo'] = 21
campeonato['Palmeiras'] = 30
campeonato['Flamengo'] = 18

camp2 = {time: [time, campeonato[time]] for time in campeonato}
print(camp2)