import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.ferramentabanco import ferramentabanco
def tela_tabela():


    root = tk.Tk()
    root.title("Tabela de Produtos")

    # Criação da tabela
    columns = ("nome", "preco", "codigo")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("nome", text="nome")
    tree.heading("preco", text="Preço")
    tree.heading("codigo", text="Codigo")

    # Ajuste das larguras das colunas
    tree.column("nome", width=100)
    tree.column("preco", width=100)
    tree.column("codigo", width=100)

    # Inserindo valores pré-definidos na tabela
    fb=ferramentabanco()
    dados=fb.tabela_ferramenta()

    for item in dados:
        tree.insert("", tk.END, values=(item.nome,item.preco,item.codigo))

    tree.pack(pady=10)

    # Iniciar a aplicação
    root.mainloop()

def criarferramenta():
    global entry_nome
    global entry_preco
    janela=tk.Tk()
    janela.geometry('400x300' )
    label_nome=tk.Label(janela,text='Nome')
    label_nome.pack()

    entry_nome=tk.Entry(janela)
    entry_nome.pack()

    label_preco=tk.Label(janela, text='preço')
    label_preco.pack()
    entry_preco=tk.Entry(janela)
    entry_preco.pack()

    adicionar=tk.Button(janela, text='adicionar ferramenta',command=add)
    adicionar.pack(pady=10)

    janela.mainloop()
def add():
    global entry_nome
    global entry_preco

    nome=entry_nome.get()
    preco=entry_preco.get()

    fb=ferramentabanco()
    try:
        fb.addferramenta(nome,preco)
        messagebox.showinfo('certo','ferramenta adicionada')
    except:
        messagebox.showerror('erro','impossivel adicionar')

def removerferramenta():
    global entry_remove
    janela = tk.Tk()
    janela.geometry('400x300')
    label = tk.Label(janela, text= 'digite o codigo da ferramenta que voce quer excluir')
    label.pack()
    entry_remove=tk.Entry(janela)
    entry_remove.pack()
    botao=tk.Button(janela, text='remover ferramenta',command=remover)
    botao.pack()
    janela.mainloop()
def remover():
    global entry_remove
    codigo=entry_remove.get()
    fb=ferramentabanco()
    try:
        fb.removerferramenta(codigo)
        messagebox.showinfo('certo','ferramenta removida')
    except: 
        messagebox.showerror('erro','impossivel remover ferramenta')

def atualizarferramenta():
    global entry_nome
    global entry_preco
    global entry_codigo
    janela=tk.Tk()
    janela.geometry('400x300' )

    label_codigo=tk.Label(janela, text='digite o codigo da ferramenta que voce quer atualizar')
    label_codigo.pack()

    entry_codigo=tk.Entry(janela)
    entry_codigo.pack()

    label_nome=tk.Label(janela,text='Nome')
    label_nome.pack()

    entry_nome=tk.Entry(janela)
    entry_nome.pack()

    label_preco=tk.Label(janela, text='preço')
    label_preco.pack()
    entry_preco=tk.Entry(janela)
    entry_preco.pack()

    atualizar=tk.Button(janela, text='atualizar ferramenta',command=update)
    atualizar.pack(pady=10)

def update():
    global entry_nome
    global entry_preco
    global entry_codigo
    nome=entry_nome.get()
    preco=entry_preco.get()
    codigo=entry_codigo.get()
    fb=ferramentabanco()
    try:
        fb.atualizarferramenta(codigo, nome, preco)

        messagebox.showinfo('certo','ferramenta atualizada')
    except:
        messagebox.showerror('erro','impossivel atualizada')
    
def run():
    janela = tk.Tk()
    janela.geometry('400x300')

    label = tk.Label(janela, text='Loja de Ferramentas CN')
    label.pack(pady=5)

    tabela = tk.Button(janela, text='Tabela de Ferramentas', command=tela_tabela)
    tabela.pack(pady=10)

    adicionar=tk.Button(janela, text='adicionar ferramenta',command=criarferramenta)
    adicionar.pack(pady=10)

    remover=tk.Button(janela, text='remover ferramenta',command=removerferramenta)
    remover.pack(pady=10)

    atualizar=tk.Button(janela,text='atulizar ferramenta',command=atualizarferramenta)
    atualizar.pack()
    janela.mainloop()

