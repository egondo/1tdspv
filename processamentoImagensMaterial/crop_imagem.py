import Imagem

#recuperando a matriz de pixels da imagem
mat = Imagem.getMatrizImagemCinza("domino.png")

#pegando as dimensoes da matriz
linhas = len(mat)
colunas = len(mat[0])
print(f'{linhas} X {colunas}')

pedra = []
for i in range(40):
    pedra.append([0] * 70)

for i in range(40):
    for j in range(70):
        pedra[i][j] = mat[i + 10][j + 12]

Imagem.salvaImagemCinza("pedra_00.png", pedra)

for i in range(40):
    for j in range(70):
        pedra[i][j] = mat[i + 10][j + 80]

Imagem.salvaImagemCinza("pedra_01.png", pedra)