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

def registra_transacao(transacao: dict):
    try:
        insere_transacao(transacao)
        info = {"id": transacao['conta_id'], "valor": transacao['valor']}
        atualiza_saldo(info)
    except Exception as erro:
        traceback.print_exc()
        msg = f"Erro no registro da transacao"
        raise Exception(msg)


cli = {
    "nome": "Luis Fernando",
    "telefone": "(11) 9483-0484",
    "documento": "324239344"
}
#abertura_conta(cli, '01311000')

tran = {
    "valor": 580,
    "contraparte": "Eduardo",
    "tipo": 'BOLETO',
    "conta_id": 21
}
registra_transacao(tran)