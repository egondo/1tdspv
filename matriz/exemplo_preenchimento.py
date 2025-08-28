matriz = []

for i in range(4):
    matriz.append([0] * 5)

x = 1
for i in range(4):
    j = 0
    while j < 5:
        matriz[i][j] = x
        x = x + 1
        j = j + 1

#imprimindo uma matriz
for lin in matriz:
    print(lin)
