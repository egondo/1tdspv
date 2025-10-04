import negocio

partidas = []

with open('partidas.txt', mode="r") as arq:
    registro = arq.readline()
    while registro:
        #print(registro)
        info = registro.split(";")
        game = {
            "time_casa": info[0],
            "gols_casa": int(info[1]),
            "time_visitante": info[2],
            "gols_visitante": int(info[3])
        }
        partidas.append(game)
        registro = arq.readline()

negocio.importa_partidas(partidas)