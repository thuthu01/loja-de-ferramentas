import psycopg2
from backend.Ferramenta import Ferramenta
class ferramentabanco:
    def __init__(self):
        pass 
    def tabela_ferramenta(self):
        conexao=psycopg2.connect(dbname="20221214010007",
                            user="postgres",
                            password="pabd",
                            host="localhost",
                            port=5432)
        cursor=conexao.cursor()
        codigosql="SELECT * FROM ferramentas"
        cursor.execute(codigosql)
        conexao.commit()
        lista=[]
        result=cursor.fetchall()
        for ferramenta in result:
            if result != None:
                nome=ferramenta[0]
                preco=ferramenta[1]
                codigo=ferramenta[2]
                fer=Ferramenta(nome,preco,codigo)

                lista.append(fer)

            else :
                lista=None
        return lista
    
    def addferramenta(self,nome,preco):
        conexao=psycopg2.connect(dbname="20221214010007",
                            user="postgres",
                            password="pabd",
                            host="localhost",
                            port=5432)
        cursor=conexao.cursor()
        codigosql=f"INSERT INTO ferramentas(nome,preco ) values('{nome}',{preco})" 
        cursor.execute(codigosql)
        conexao.commit()

    def removerferramenta(self,codigo):
        conexao=psycopg2.connect(dbname="20221214010007",
                            user="postgres",
                            password="pabd",
                            host="localhost",
                            port=5432)
        cursor=conexao.cursor()
        codigosql=f"DELETE FROM ferramentas WHERE codigo={codigo};" 
        cursor.execute(codigosql)
        conexao.commit()

    def atualizarferramenta(self,codigo,nome,preco):
        conexao=psycopg2.connect(dbname="20221214010007",
                            user="postgres",
                            password="pabd",
                            host="localhost",
                            port=5432)
        cursor=conexao.cursor()
        codigosql=f"UPDATE ferramentas SET nome='{nome}',preco={preco} WHERE codigo={codigo}" 
        cursor.execute(codigosql)
        conexao.commit()