import busca
import time

def cria_lista(n):
    resp = []
    for i in range(n):
        resp.append(i)

    return resp


lista = cria_lista(3_000_000)

t_ini = time.time()
for i in range(100):
    busca.busca(lista, -1)
t_fim = time.time()

print(f"Tempo do busca simples {t_fim - t_ini}")


t_ini = time.time()
for i in range(100):
    busca.busca_binaria(lista, -1)
t_fim = time.time()

print(f"Tempo do busca binaria {t_fim - t_ini}")
