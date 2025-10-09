from flask import Flask, request, jsonify
import db

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "Olá turma 1tdspv!", 200



@app.route("/carros", methods=['GET'])
def recupera_carros():
    return db.carros, 200

@app.route("/carros", methods=['POST'])
def insere_carro():
    info = request.json
    db.carros.append(info)
    return info, 201

app.run(debug=True)