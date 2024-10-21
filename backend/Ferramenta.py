class Ferramenta:
    def __init__(self,nome,preco,codigo):
         self.nome=nome 
         self.preco=preco
         self.codigo=codigo

    def __str__(self):
         return f'nome:{self.nome}\npreço:{self.preco}\ncodigo:{self.codigo}'