#transforme essa funcao para retornar o seguinte:
#se palavra = 'Argentina' a funcao retorna '_ _ _ _ _ _ _ _ _'
def get_palavra_secreta(palavra: str) -> str:
    resp = ""
    for c in palavra:
        resp = resp + '_ '
    return resp


def substitui(frase: str, letras: str) -> str:
    resp = ""
    for c in frase:
        if c in letras:
            resp = resp + f'{c} '
        else:
            resp = resp + '_ '
    return resp

def get_palavra_secreta_2(palavra: str) -> str:
    return '_ ' * len(palavra)


if __name__ == '__main__':
    palavra = "Estados Unidos"
    segredo = get_palavra_secreta(palavra)
    erros = 0
    letras_chutadas = ''

    while erros < 6 and '_' in segredo:
        print(segredo)
        print(f"Erros {erros}")
        letra = input("Letra: ")[0]
        letras_chutadas = letras_chutadas + letra
        segredo = substitui(palavra, letras_chutadas)
        if not letra in palavra:
            erros = erros + 1 
    
    if erros >= 6:
        print("Você perdeu, a palavra era: ")
    else:
        print("Você venceu, a palavra era: ")

    print(palavra)