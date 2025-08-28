
def soma(matA, matB):
    resp = []
    lin = len(matA)
    col = len(matA[0])
    for i in range(lin):
        resp.append([0] * col)
        for j in range(col):
            resp[i][j] = matA[i][j] + matB[i][j]
    return resp        
