def organiza(lista: list, pos: int):
    aux = lista[pos]
    while pos > 0 and lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    lista[pos] = aux

def sort(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)

if __name__ == "__main__":
    lst = [4, 2, 8, -1, 3, 6, 0]
    sort(lst)
    print(lst)