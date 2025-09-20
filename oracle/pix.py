import oracledb

def get_conexao(usuario="pf0313", senha="professor#23") -> oracledb.Connection:
    servidor = "oracle.fiap.com.br/orcl"
    return oracledb.connect(user=usuario, password=senha, dsn=servidor)


def insere_pix(obj: dict):
    with get_conexao("pf0313", "professor#23") as con:
        with con.cursor() as cur:
            sql = "INSERT INTO t_pix(chave, nome, banco, agencia, conta) VALUES(:chave, :nome, :banco, :agencia, :conta)"
            cur.execute(sql, obj)
        con.commit()

def recupera_pix() -> list:
    resp = []
    with get_conexao("pf0313", "professor#23") as con:
        with con.cursor() as cur:
            sql = "SELECT id_pix, chave, nome, banco, agencia, conta FROM t_pix ORDER BY chave"
            cur.execute(sql)
            regs = cur.fetchall()
            for info in regs:
                obj = {"id": info[0], "chave": info[1], "nome": info[2], "banco": info[3], "agencia": info[4], "conta": info[5]}
                resp.append(obj)
    return resp

def apaga_pix(id: str):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "DELETE FROM t_pix WHERE id_pix = :id"
            cur.execute(sql, {"id": id})

        con.commit()

def atualiza_pix(obj: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "UPDATE t_pix SET chave=:chave, nome=:nome, banco=:banco, agencia=:agencia, conta=:conta WHERE id_pix=:id"

            cur.execute(sql, obj)
        con.commit()



if __name__ == "__main__":
    #conexao = get_conexao("pf0313", "professor#23")
    #print(conexao.version)
    #conexao.close()

    #dado = {"chave": "(11) 832423", "nome": "Alexandre Matias", "banco": "Bradesco", "agencia": "234-9", "conta": "02873-8"}

    #dado = {"chave": "028.874.829-03", "nome": "Maria da Graça", "banco": "Itaú", "agencia": "82343-9", "conta": "8243-2"}

    #dado = {"chave": "fefe@gmail.com", "nome": "Fernanda Ferreira", "banco": "Inter", "agencia": "0001-0", "conta": "6372-9"}

    #insere_pix(dado)

    #apaga_pix(11)
    #apaga_pix(12)

    dado = {"id": 15, "chave": "fernanda_fer@gmail.com", "nome": "Fernanda Ferreira Guimaraes", "banco": "Inter", "agencia": "0001-0", "conta": "2834209-9"}

    atualiza_pix(dado)

    lista = recupera_pix()
    for info in lista:
        print(info)