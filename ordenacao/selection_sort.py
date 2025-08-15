def menor(lista: list, pos: int) -> int:
    aux = lista[pos]
    aux_pos = pos
    pos = pos + 1

    while pos < len(lista):
        if lista[pos] < aux:
            aux_pos = pos
            aux = lista[pos]
        pos = pos + 1
    
    return aux_pos


def sort(lista: list):
    for i in range(len(lista)):
        pos = menor(lista, i)
        #troca
        aux = lista[pos]
        lista[pos] = lista[i]
        lista[i] = aux


if __name__ == "__main__":
    lst = [-1, 8, 10, 15, -3, 7, 5]
    sort(lst)
    print(lst)

    lst = ["Renato", "Gustavo", "Airton", "Luis", "Raul", "Djavan", "Abel", "Edu"]
    sort(lst)
    print(lst)
