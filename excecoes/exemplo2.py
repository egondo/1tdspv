try:
    a = float(input("Informe a: "))
    b = float(input("Informe b: "))
    resultado = a / b
    print(f"{a}/{b} = {resultado}")
except ZeroDivisionError as erro:
    print("Tentou dividir por zero")
except ValueError as erro2:
    print("Erro na conversao para numero")

