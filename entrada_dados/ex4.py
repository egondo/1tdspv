#lendo um número do teclado
aux = input("Digite o primeiro numero: ")
#convertendo a informação para int
num_a = int(aux)

aux = input("Digite o segundo numero: ")
num_b = int(aux)

#processamento
prod = num_a * num_b
soma = num_a + num_b
div = num_a // num_b
resto = num_a % num_b

print("Soma ", soma)
print("Multiplicacao ", prod)
print("Divisao ", div)
print("Resto ", resto)


