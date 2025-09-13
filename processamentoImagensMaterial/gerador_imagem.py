import Imagem

desenho = []
for i in range(400):
    desenho.append([240] * 600)

for i in range(250):
    for j in range(60):
        desenho[i + 90][j + 35] = 110


Imagem.salvaImagemCinza("nosso_desenho.png", desenho)