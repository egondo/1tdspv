alt = float(input("Altura em m: "))
peso = float(input("Em kg: "))

imc = alt / (peso * peso)

print(f"IMC = {imc}")
if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("Obesidade")