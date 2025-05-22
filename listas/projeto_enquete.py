def menu() -> int:
    print("SISTEMA ENQUETE")
    print("1) cadastra pergunta")
    print("2) visualiza perguntas")
    print("3) apaga pergunta")
    print("4) aplica perguntas")
    print("5) sair")
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

def monta_alternativas(opcoes: list) -> str:
    resp = ""
    letras = "abcdefghijk"
    i = 0
    while i < len(opcoes):
        resp = resp + f"\t{letras[i]}) {opcoes[i]}\n"   
        i = i + 1
    return resp

def aplica_enquete(perguntas: list, respostas: list):
    i = 0
    while i < len(perguntas):
        print(f"{perguntas[i]}) {perguntas[i+1]}")
        if perguntas[i+2] != 'aberta':
            info = monta_alternativas(perguntas[i+3])
            print(info)
        
        resp = input("Resp: ")
        respostas.append(resp)
        i = i + 4



#INICIO PROGRAMA (main)
lista = [1, 'O que é Objeto?', 'aberta', None, 2, 
    'Em Java, quais desses tipos representam números inteiros?', 'unica', 
    ['int, short, byte', 'long, float', 'bigint, bigfloat', 'double, char'], 3, 'Assinale as alternativas incorretas?', 'multipla', ['a palavra reservada new serve para criar uma nova variavel', 'extends significa uma extensão de telefone', 'implements é um recurso da linguagem Java', 'enum define tipos fixos dentro do java', 'o construtor cria o objeto e inicializa seus atributos']]
respostas = []
opcao = 0
while opcao != 5:
    opcao = menu()
    if opcao == 1:
        cadastra_pergunta(lista)
    elif opcao == 2:
        print(lista)
    elif opcao == 3:
        print("apaga pergunta")
    elif opcao == 4:
        aplica_enquete(lista, respostas)
    elif opcao == 5:
        print("saindo do sistema")
    else:
        print("opcao invalida")

