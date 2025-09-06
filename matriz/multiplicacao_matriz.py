def produto_escalar_2(listaA, listaB):
    soma = 0
    for i in range(len(listaA)):
        soma = soma + listaA[i] * listaB[i]
    return soma



def produto_escalar(matrizA, lin, matrizB, col):
    dimA = len(matrizA[0])
    soma = 0
    for t in range(dimA):
        soma = soma + matrizA[lin][t] * matrizB[t][col]

    return soma    


def multiplica(matrizA, matrizB):
    qtdColunasA = len(matrizA[0])
    qtdLinhasB = len(matrizB)
    if qtdColunasA != qtdLinhasB:
        print("Impossivel realizar a multiplicacao, dimensoes erradas")
        return None
    else:
        resp = []
        qtdLinA = len(matrizA)
        qtdColB = len(matrizB[0])
        for i in range(qtdLinA):
            resp.append([0] * qtdColB)

        for i in range(qtdLinA):
            for j in range(qtdColB):
                valor = produto_escalar(matrizA, i, matrizB, j)
                resp[i][j] = valor
        
        return resp



matA = [[2, 1], [-1, 0]]
matB = [[-1, -2], [1, 2]]

resultado = multiplica(matA, matB)
print(resultado)

a = [2, -5, 7]
b = [1, 0, -1]
resp = produto_escalar_2(a, b)
print(resp)

