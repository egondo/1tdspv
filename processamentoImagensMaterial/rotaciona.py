import Imagem

def gira90(img: list) -> list:
    lin = len(img)
    col = len(img[0])
    resp = []
    for i in range(col):
        resp.append([0] * lin)
    for i in range(lin):
        for j in range(col):
            resp[col - 1 - j][i] = img[i][j]
    return resp

matrizes = Imagem.getMatrizImagemColorida("gato.jpg")
resp_red = gira90(matrizes[0])
resp_green = gira90(matrizes[1])
resp_blue = gira90(matrizes[2])

Imagem.salvaImagemColorida("gato_girado.jpg", 
                resp_red, resp_green, resp_blue)