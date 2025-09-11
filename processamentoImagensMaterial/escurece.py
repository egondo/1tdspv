import Imagem

matrizes = Imagem.getMatrizImagemColorida("lago_canada.jpg")
red = matrizes[0]
green = matrizes[1]
blue = matrizes[2]

lin = len(red)
col = len(red[0])
for i in range(lin):
    for j in range(col//2):
        red[i][j] = red[i][j] - 50
        green[i][j] = green[i][j] - 50
        blue[i][j] = blue[i][j] - 50

Imagem.salvaImagemColorida("lago_escuro.jpg", red, green, blue)