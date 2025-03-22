#considere que o rm possui 6 dígitos
soma = 0

rm = int(input("Digite o RM: "))

resto = rm % 10
soma = soma + resto  #acumulando valor na variavel resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

print(f"A soma dos dígitos do RM vale {soma}")