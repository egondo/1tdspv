def busca(lista: list, valor: float) -> int:
    i = 0
    while i < len(lista) and lista[i] != valor:
        i = i + 1

    if i == len(lista):
        return -1
    else:
        return i    


def busca_for(lista: list, valor: float) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    
    return -1


def busca_binaria(lista: list, valor: float) -> int:
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] < valor:
            ini = meio + 1
        elif lista[meio] > valor:
            fim = meio - 1
        else:
            return meio
    
    return -1