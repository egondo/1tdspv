import oracledb
import traceback

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")


def insere_cliente(cliente):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "insert into cliente(nome, telefone, documento) values(:nome, :telefone, :documento) returning id into :id"

            new_var = cur.var(oracledb.NUMBER)
            cliente['id'] = new_var

            cur.execute(sql, cliente)
            cliente['id'] = new_var.getvalue()[0]
        con.commit()

def insere_endereco(endereco, id_cliente):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "insert into endereco(logradouro, bairro, cep, cidade, pessoa_id) values(:logradouro, :bairro, :cep, :cidade, :pessoa_id)"

            endereco['pessoa_id'] = id_cliente
            cur.execute(sql, endereco)
        con.commit()

def insere_conta(cliente: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = 'select sq_numero.nextval from dual'
            cur.execute(sql)
            registro = cur.fetchone()
            id_conta = registro[0]
            print(f"Conta: {id_conta}")

            sql = "insert into conta(tipo, numero, senha, saldo, cliente_id) values('corrente', :id_conta, 'admin', 0, :cliente_id)"

            info = {"id_conta": id_conta, "cliente_id": cliente['id']}
            cur.execute(sql, info)
        con.commit()


def insere_transacao(transacao: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO TRANSACAO(valor, data_hora, contraparte, tipo, conta_id) VALUES(:valor, current_timestamp, :contraparte, :tipo, :conta_id)"
            cur.execute(sql, transacao)
        con.commit()

def atualiza_saldo(info: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "UPDATE conta SET saldo = saldo + :valor WHERE id = :id"
            cur.execute(sql, info)
        con.commit()

def consulta_conta(id: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "SELECT c.nome, c.telefone, cont.numero, cont.saldo, cont.tipo FROM conta cont join cliente c on cont.cliente_id = c.id WHERE c.id = :id"        
            cur.execute(sql)
            return cur.fetchone()
        

def recupera_clientes():
    clientes = []
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "SELECT c.nome, c.telefone, c.documento FROM cliente c WHERE c.ativo = true"
            cur.execute(sql)
            dados = cur.fetchall()
            for reg in dados:
                info = {
                        "nome": dados[1],
                        "telefone": dados[2],
                        "documento": dados[3]
                    }
                clientes.append(info)
        return clientes