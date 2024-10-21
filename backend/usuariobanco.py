import psycopg2
from backend.Usuario import Usuario
class usuariobanco:
    def __init__(self):
        pass 
    def pegar_usuario_pelo_nome(self,nome):
        conexao=psycopg2.connect(dbname="20221214010007",
                                user="postgres",
                                password="pabd",
                                host="localhost",
                                port=5432)
        cursor=conexao.cursor()
        codigosql="SELECT * FROM usuario WHERE nome='"+nome+"';"
        cursor.execute(codigosql)
        linha=cursor.fetchone()
        if linha != None:
            nome=linha[0]
            senha=linha[1]
            codigo=linha[2]
            usuario=Usuario(nome,senha,codigo)
        else: 
            usuario=None
        return usuario