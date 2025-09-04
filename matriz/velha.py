def haGanhador(mat: list) -> bool:
    for t in range(len(mat)):
        if mat[t][0] != ' ' and mat[t][0] == mat[t][1] and mat[t][1] == mat[t][2]:
            return True
    
        if mat[0][t] != ' ' and mat[0][t] == mat[1][t] and mat[1][t] == mat[2][t]:
            return True
    
    if mat[0][0] != ' ' and mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2]:
        return True
    
    if mat[0][2] != ' ' and mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0]:
        return True

    return False
    


def temEspaco(matriz: list) -> bool:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == ' ':
                return True
    return False



def joga(matriz: list, lin: int, col: int, jogador: str) -> bool:
    if matriz[lin][col] != 'X' and matriz[lin][col] != 'O':
    #if matriz[lin][col] == ' ':
        matriz[lin][col] = jogador
        return True
    else:
        return False
    

def imprime(matriz: list):
    for lin in matriz:
        print(lin)
