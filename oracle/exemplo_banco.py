import oracledb

#conectando ao oracle
conn = oracledb.connect(user="pf0313", password="professor#23",       dsn="oracle.fiap.com.br/orcl")
print(conn.version)

#abrir um cursor para efetuar as operacoes (Statement/PreparedStatement)
cursor = conn.cursor()
sql = "SELECT * FROM TB_PERGUNTA"
#executando uma consulta
cursor.execute(sql)

#recuperando dados da consulta e imprimindo na tela
registros = cursor.fetchall()
for info in registros:
    print(info)

#fechando os recursos abertos
cursor.close()
conn.close()


