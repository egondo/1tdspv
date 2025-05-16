def menu() -> int:
    print("SISTEMA ENQUETE")
    print("1) cadastra pergunta")
    print("2) visualiza perguntas")
    print("3) apaga pergunta")
    print("4) sair")
    return int(input("Opção: "))

def cadastra_pergunta(lista: list):
    num = int(input("Número: "))
    enun = input("Enunciado: ")
    tipo = input("Tipo: ")
    alternativas = None
    if tipo != 'aberta':
        #coletar as alternativas
        alternativas = []
        i = 1
        aux = input(f"alt {i}: ")
        while aux != "":
            alternativas.append(aux)
            i = i + 1
            aux = input(f"alt {i}: ")
    
    lista.append(num)
    lista.append(enun)
    lista.append(tipo)
    lista.append(alternativas)


#INICIO PROGRAMA (main)
lista = []
opcao = 0
while opcao != 4:
    opcao = menu()
    if opcao == 1:
        cadastra_pergunta(lista)
    elif opcao == 2:
        print(lista)
    elif opcao == 3:
        print("apaga pergunta")
    elif opcao == 4:
        print("saindo do sistema")
    else:
        print("opcao invalida")

