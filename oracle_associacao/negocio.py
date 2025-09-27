import banco

def cadastra_empresa(empresa: dict):
    veiculos = empresa['veiculos']
    banco.salva_pessoa(empresa)
    for veiculo in veiculos:
        veiculo['proprietario_id'] = empresa['id']
        banco.salva_veiculo(veiculo)


if __name__ == "__main__":
    dado = {
        "nome": "MOVIDA",
        "telefone": "(11) 9823-9202",
        "documento": "52.797.382/0001-82",
        "url": "www.movida.com.br",
        "veiculos": [
            {"placa": "GWR-2I38", "montadora": "Volks", "modelo": "Golf", "ano": 2020},
            {"placa": "KJR-0E65", "montadora": "Ford", "modelo": "Fiesta", "ano": 2019},
            {"placa": "EHK-5F90", "montadora": "Toyota", "modelo": "Yaris", "ano": 2022}  
        ]
    }

    cadastra_empresa(dado)
        