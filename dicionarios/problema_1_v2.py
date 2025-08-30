def organiza(lista: list, pos: int):
    aux = lista[pos]
    while pos > 0 and aux < lista[pos-1]:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    
    lista[pos] = aux

frase = "Socorram me subi no onibus em Marrocos"
frase = frase.lower()

dic = {}
for letra in frase:
    if letra != ' ':
        if letra in dic.keys():
            dic[letra] = dic[letra] + 1
        else:
            dic[letra] = 1

#impressao em ordem alfabetica
letras = []
i = 0
for chave in dic:
    if not chave in letras:
        letras.append(chave)
        organiza(letras, i)
        i = i + 1

for letra in letras:
    print(f"{letra} => {dic[letra]}")
