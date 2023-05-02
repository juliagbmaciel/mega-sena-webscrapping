import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='localhost',
        database='loteria',
        user='root',
        password=''
    )
except:
    print("Erro ao conectar")



