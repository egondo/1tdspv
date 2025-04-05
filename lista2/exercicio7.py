import math

numero = float(input("Digite um número para extrair a raiz quadrada: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(raiz)
else:
    print("Não existe raiz quadrada de números negativo")

#raiz = numero ** 0.5
#print(raiz)