#transforme essa funcao para retornar o seguinte:
#se palavra = 'Argentina' a funcao retorna '_ _ _ _ _ _ _ _ _'
def get_palavra_secreta(palavra: str) -> str:
    resp = ""
    for c in palavra:
        resp = resp + '_ '
    return resp


def substitui(frase: str, letra: str) -> str:
    resp = ""
    for c in frase:
        if c == letra:
            resp = resp + f'{c} '
        else:
            resp = resp + '_ '
    return resp

def get_palavra_secreta_2(palavra: str) -> str:
    return '_ ' * len(palavra)


if __name__ == '__main__':
    palavra = "Espanha"
    segredo = get_palavra_secreta(palavra)
    erros = 6
    while erros > 0 and '_' in segredo:
        print(segredo)
        letra = input("Letra: ")[0]
        segredo = substitui(palavra, letra)
        if not letra in palavra:
            erros = erros - 1 
    
