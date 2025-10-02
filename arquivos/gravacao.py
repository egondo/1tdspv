import random

nome = ["Eduardo", "Fabio", "Roberto", "Cassio", "Fernando", "Tadeu"]

with open("duplas.txt", "w") as arq:
    for i in range(len(nome)):
        for j in range(len(nome)):
            arq.write(f"{nome[i]};{nome[j]}\n")

            