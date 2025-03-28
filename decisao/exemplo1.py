numero = int(input("Digite um número: "))
resto = numero % 2
if resto == 0:
    print(f"{numero} é par")
    print(numero, " é par")
else:
    print(f"{numero} é ímpar")
    print(numero, " é ímpar")