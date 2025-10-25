from flask import Flask, jsonify, request
from flask_cors import CORS
import negocio as neg

app = Flask(__name__)

CORS(app, origins="*")

@app.route("/banco/cliente", methods=['POST'])
@cors_origins()
def cadastra_cliente():
    cli = request.json
    cep = cli['cep']
    cli.pop('cep')
    try:
        neg.abertura_conta(cli, cep)
        return cli, 201
    except Exception as erro:
        return {"erro": "Erro no cadastro do cliente"}, 400

@app.route("/banco/transacao", methods=['POST'])
@cors_origins()
def cadastra_transacao():
    transacao = request.json
    try:
        neg.registra_transacao(transacao)
        return transacao, 201
    except Exception as erro:
        return {"erro": "Erro no cadatro da transacao"}, 400


app.run(debug=True)