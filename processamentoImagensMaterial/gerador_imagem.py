import Imagem
import rotaciona

def desenha_coluna(matriz, altura, pos_lin, pos_col):
    for i in range(altura):
        for j in range(50):
            if i == 0 or i == altura - 1 or j == 0 or j == 49:
                matriz[i + pos_lin][j + pos_col] = 0
            else:      
                matriz[i + pos_lin][j + pos_col] = 110
            

desenho = []
for i in range(400):
    desenho.append([240] * 600)

desenha_coluna(desenho, 13, 30, 20)
desenha_coluna(desenho, 33, 30, 80)
desenha_coluna(desenho, 84, 30, 140)
desenha_coluna(desenho, 147, 30, 200)
desenha_coluna(desenho, 231, 30, 260)
desenha_coluna(desenho, 95, 30, 320)

desenha_coluna(desenho, 73, 30, 380)
desenha_coluna(desenho, 23, 30, 440)
desenha_coluna(desenho, 27, 30, 500)

img = rotaciona.gira90(desenho)
desenho = rotaciona.gira90(img)

Imagem.salvaImagemCinza("nosso_desenho.png", desenho)