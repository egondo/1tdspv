num_a = float(input("Digite um numero: "))
op = input("Digite o operador (+-*/): ")
num_b = float(input("Digite outro número: "))

if op == '+':
    resultado = num_a + num_b
elif op == '-':
    resultado = num_a - num_b
elif op == '*':
    resultado = num_a * num_b
elif op == "/":
    resultado = num_a / num_b
else:
    print(f"Operador {op} inválido!")
    resultado = None  #vazio ou nada

if resultado != None:
    print(f"{num_a} {op} {num_b} = {resultado}")
