import oracledb

conn = oracledb.connect(user="pf0313", dsn="oracle.fiap.com.br/orcl", password="professor#23")

cursor = conn.cursor()

ins = "INSERT INTO t_pix(chave, nome, banco, agencia, conta) VALUES(:chave, :nome, :banco, :agencia, :conta)"
info = {"chave": "airton@gmail.com", "nome": "Airton Custodio", "banco": "NuBank", "agencia": "2439", "conta": "634289-8"}

cursor.execute(ins, info)
conn.commit()

chave = input("Informe a chave pix que deseja apagar: ")
#PASSIVEL DE ATAQUES DE sql INJECTION
#sql = f"DELETE FROM t_pix WHERE chave='{chave}'"
#cursor.execute(sql)

sql = "delete from t_pix where chave = :valor"
info = {"valor": chave}
cursor.execute(sql, info)

conn.commit()

cursor.close()
conn.close()