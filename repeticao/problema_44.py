#Problema da validacao
nota = float(input("Digite a nota: "))
while nota < 0 or nota > 10:
    print("Nota inválida! Digite entre 0 e 10!")
    nota = float(input("Nota: "))

outra_nota = float(input("Digite outra nota: "))
while outra_nota < 0 or outra_nota > 10:
    print("Nota inválida! Digite entre 0 e 10!")
    outra_nota = float(input("Nota: "))

media = (nota + outra_nota) / 2
print(f"A média vale {media}")