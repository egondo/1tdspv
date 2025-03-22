#area = pi * raio * raio
#perimetro = 2 * pi * raio

pi = 3.141592
aux = input("Digite o raio do circulo: ")
raio = float(aux)

area = pi * raio * raio
peri = 2 * pi * raio

print("A area do circulo vale", area)

#usando f-string
print(f"O perimetro vale {peri}")
