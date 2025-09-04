def produto_escalar(listaA, listaB):
    soma = 0
    for i in range(len(listaA)):
        soma = soma + listaA[i] * listaB[i]
    return soma

a = [2, -5, 7]
b = [1, 0, -1]
resp = produto_escalar(a, b)
print(resp)

