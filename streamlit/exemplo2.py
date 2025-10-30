import streamlit as st
import requests

def recupera_clientes():
    url = "https://onetdspv-banco.onrender.com/banco/cliente"
    requisicao = requests.get(url)
    if requisicao.status_code >= 200 and requisicao.status_code < 300:
        clientes = requisicao.json()
        return clientes
    else:
        raise Exception(f"ERRO HTTP {requisicao.status_code}")


def envia_transacao(nome_cliente: str, registro: dict, clientes: list):
    for c in clientes:
        if c.get('nome') == nome_cliente:
            registro['conta_id'] = c.get('id')
            break
    url = "https://onetdspv-banco.onrender.com/banco/transacao"
    requisicao = requests.post(url, json=registro)
    if requisicao.status_code == 201:
        return True
    else:
        return False



st.set_page_config(layout="wide")    
st.header("Cadastro de transacao")
clientes = recupera_clientes()
nomes = [""]

for cli in clientes:
    nomes.append(cli['nome'])

nome_selecionado = st.selectbox("Cliente", nomes)
tipo = st.selectbox("Tipo: ", ["", "PIX", "saque", "depósito", "boleto", "cheque"])
valor = st.number_input("Valor: ")
obs = st.text_area("Observacao: ")
if st.button("envia"):
    '''coleta as informacoes do formulario, procura o cliente de acordo com o nome e envia a transacao para a API no render usando o requests'''
    info = {
        "valor": valor,
        "tipo": tipo,
        "contraparte": obs
    }
    resp = envia_transacao(nome_selecionado, info, clientes)
    if resp == True:
        st.subheader("Sucesso!")
    else:
        st.subheader("Falha")