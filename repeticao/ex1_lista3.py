'''Dada uma sequência de números inteiros onde o último elemento é o 0, escreva um algoritmo
que calcula a soma dos números pares da sequência.'''

#23, 56, -98, 49,20, 7, 6, 18, 0
soma = 0
num = int(input("Digite numero: ")) #23

while num != 0:
    if num % 2 == 0:
        soma = soma + num
    num = int(input("Digite numero: ")) #56
print(soma)