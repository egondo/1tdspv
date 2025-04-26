num = int(input("Informe o número: "))

resp = ""   #resposta do algoritmo
pot = 1

while num != 0:
    digito = num % 10
    num = num // 10
    #print(digito)
    resp = f"{digito} * {pot} + {resp}"

    pot = pot * 10

print(resp)
print("Fim do programa")
