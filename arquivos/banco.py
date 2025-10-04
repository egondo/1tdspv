import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password='professor#23',
    dsn='oracle.fiap.com.br/orcl')

def recupera_pelo_nome(nome: str) -> dict:
    '''se o time nao existir no banco, você deverá retornar None
    caso contrário, retorne um dicionário contendo todas as colunas presentes na tabela time'''

def insere_time(time: dict):
    '''realiza a insercao do time na tabela do banco de dados
    nao esqueca de pegar o id gerado pelo banco de dados e coloque no time.'''

def atualiza_time(time: dict):
    '''atualiza os times que participaram da partida.'''

def insere_partida(partida: dict):
    #grava o dicionario na tabela partida