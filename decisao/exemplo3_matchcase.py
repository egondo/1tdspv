#entrada de dados
num_a = float(input("Digite um numero: "))
op = input("Digite o operador (+-*/): ")
num_b = float(input("Digite outro número: "))

match op:
    case '+':
        result = num_a + num_b
    case '-':
        result = num_a - num_b
    case '*':
        result = num_a * num_b
    case '/':
        if num_b != 0:
            result = num_a / num_b
        else:
            result = None
            print("Impossivel dividir por 0")
    case _:
        print("Operador inválido")
        result = None

if result != None:
    print(f"Resultado = {result}")
