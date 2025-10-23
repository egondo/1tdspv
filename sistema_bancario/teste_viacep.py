import requests

cep = "01311000"

url = f"https://viacep.com.br/ws/{cep}/json"
resposta = requests.get(url)
print(resposta)
dado = resposta.json()
print(dado)



