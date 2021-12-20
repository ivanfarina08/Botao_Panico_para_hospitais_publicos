import mysql.connector

from DAOServidor import DAOServidor

con = mysql.connector.connect(host='192.168.0.1', database='panico', user='server', password='F@rin@08')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    sql = ("select * from servidores")
    cursor.execute(sql)
    if cursor:
        DAOServidor.excluir_tudo()
        for (ip, descricao) in cursor:
            DAOServidor.insere_servidor(ip, descricao)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")
