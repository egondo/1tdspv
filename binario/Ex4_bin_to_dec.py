dec = int(input("Informe numero inteiro positivo: "))
while dec < 0:
    print("Numero invalido!")
    dec = int(input("Informe numero inteiro positivo: "))

binario = 0
pot10 = 1
while dec != 0:
    resto = dec % 2
    binario = binario + resto * pot10
    dec = dec // 2
    pot10 = pot10 * 10

print(binario)