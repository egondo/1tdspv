total = float(input("Digite o total da compra: "))
print(f"Dinheiro ou pix, desconto de 10% {total * 0.9}")
print(f"Débito, desconto de 5% {total * 0.95}")
print(f"Em 2x iguais de {total/2}")
juros = total * 1.05
print(f"Em 3 parcelas com juros: {juros / 3}")
juros = total * 1.08
print(f"Em 4 parcelas com juros: {juros / 4}")

