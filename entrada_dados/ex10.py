#aux = input("Distancia em metros: ")
#dist_metros = int(aux)

dist_metros = int(input("Distancia em metros: "))
tempo_seg = int(input("Tempo em segundos: "))

velocidade = dist_metros / tempo_seg
print(f"Velocidade em m/s: {velocidade}")

dist_km = dist_metros / 1000
tempo_h = tempo_seg / 3600
vel_kmhora = dist_km / tempo_h
print(f"Velocidade em km/h: {vel_kmhora}")


