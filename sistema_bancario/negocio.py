from banco import *
import traceback
import requests

def consulta_viacep(cep: str) -> dict:
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    dado = resposta.json()
    info = {
        "logradouro": dado['logradouro'],
        "bairro": dado['bairro'],
        "cep": dado['cep'],
        'cidade': dado['localidade']
    }
    return info


def abertura_conta(cliente: dict, cep: str):
    try:
        #pego o cep do cliente e faço uma consulta no viacep
        endereco = consulta_viacep(cep)
        insere_cliente(cliente)
        insere_endereco(endereco, cliente['id'])
        insere_conta(cliente)
    except Exception as erro:
        traceback.print_exc()
        msg = f'Erro na abertura do cliente {cliente["nome"]}'
        raise Exception(msg)


cli = {
    "nome": "Viviane",
    "telefone": "(11) 9483-9029",
    "documento": "364.948.802-99"
}

abertura_conta(cli, '01211000')