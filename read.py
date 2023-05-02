from conexao_banco import conexao
from prettytable import PrettyTable

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()
print(f'Banco => {linha[0]}')


def retorna_banco():
    sql = 'SELECT * from resultados'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas


def listar_resultados():
    sql = 'SELECT * from resultados'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    tabela = PrettyTable()
    tabela.field_names = ["ano", "sorteio", "num1", "num2", "num3", "num4", "num5", "num6"]

    for linha in linhas:
        tabela.add_row(linha)
    print(tabela)


def procurar_usuario(idUser):
    sql = f"SELECT * from usuario WHERE idUsuario = '{idUser}'"
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas


