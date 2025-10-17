from banco import *
import traceback

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
    "nome": "Edu",
    "telefone": "(11) 73432423",
    "documento": "123"
}

abertura_conta(cli, '010293000')