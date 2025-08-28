def particao(lista, ini, fim):
    pivo = lista[fim]
    pos = ini
    i = ini
    while i < fim:
        if lista[i] <= pivo:
            aux = lista[i]
            lista[i] = lista[pos]
            lista[pos] = aux

            pos = pos + 1
        i = i + 1
        
    aux = lista[i]
    lista[i] = lista[pos]
    lista[pos] = aux
    return pos


a = [5, 20, 41, 6, -1, 10, 13, 2, 7]
pos = particao(a, 0, len(a) - 1)
print(a)
print(pos)