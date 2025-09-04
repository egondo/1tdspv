notas = [
    [5, 6.7, 8, 8.5],
    [3, 8, 5.8, 3.3],
    [10, 9, 7.2, 4.5],
    [9.4, 8.1, 5.4, 6.8]
]

for lin in notas:
    soma = 0
    for nt in lin:
        soma = soma + nt
    
    media = soma / len(lin)
    print(f"A média foi {media}")