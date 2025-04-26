#Entra com um número de 9 dígitos representando o CPF e retorna os dígitos de controle

cpf9 = int(input("Digite os 9 primeiros dígitos do CPF: "))

soma = 0
fator = 2
aux = cpf9

while aux != 0:
    dig = aux % 10
    soma = soma + dig * fator
    aux = aux // 10
    fator = fator + 1

resto = soma % 11
if resto < 2:
    dc1 = 0
else:
    dc1 = 11 - resto

aux = cpf9 * 10 + dc1
soma = 0
fator = 2
while aux != 0:
    dig = aux % 10
    soma = soma + dig * fator
    aux = aux // 10
    fator = fator + 1

resto = soma % 11
if resto < 2:
    dc2 = 0
else:
    dc2 = 11 - resto

print(f"DC = {dc1}{dc2}")