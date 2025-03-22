#Calculo do desconto do IPTU na cidade de SP

valor_vista = float(input("Valor à vista do IPTU: "))
parcela = float(input("Parcela: "))
valor_real = parcela * 10

desconto = valor_real - valor_vista
desc_perc = (desconto / valor_vista) * 100

print(f"O desconto concedida é de {desc_perc:.2f}%")
