import random

times = [
    "Corinthians", 'Flamengo', "Palmeiras", "São Paulo", "Atlético Mineiro", 
    "Internacional", "Fluminense", "Botafogo", "Fortaleza", "Bahia", "Santos",
    "Vasco da Gama", "Mirassol", "RB Bragantino", "Grêmio", "Juventude",  "Vitória",
    "Sport", "Ceará", "Cruzeiro"
]

with open("partidas.txt", mode="w", encoding="utf8") as arq:
    for j in range(len(times)):
        for i in range(j + 1, len(times)):
            gol_visitante = random.randint(0, 6)
            gol_casa = random.randint(0, 6)
            partida = f"{times[i]}; {gol_casa}; {times[j]};{gol_visitante}\n"
            arq.write(partida)