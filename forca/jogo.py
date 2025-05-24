def get_palavra_secreta(palavra: str) -> str:
    resp = ""
    for c in palavra:
        resp = resp + c + ' '
    return resp


if __name__ == '__main__':
    word = "Manga"
    aux = get_palavra_secreta(word)
    print(aux)