fn_anterior = 1
fn_atual = 1
n = int(input("Digite o termo da seq de Fibonacci: "))
i = n
while i > 2:
    fn_prox = fn_atual + fn_anterior
    fn_anterior = fn_atual
    fn_atual = fn_prox
    i = i - 1

print(f"O {n}-ésimo termo da sequência é {fn_atual}")



