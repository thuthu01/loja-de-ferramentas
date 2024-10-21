import tkinter as tk
from tkinter import messagebox 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.usuariobanco import usuariobanco
from frontend.telahome import run

def verificar_login():
    nome = entry_usuario.get()
    senha = entry_senha.get()
    
    ub=usuariobanco()
    usuarioitem=ub.pegar_usuario_pelo_nome(nome)
    if usuarioitem != None and usuarioitem.senha == senha:
        run()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry('400x300')
# Criando os componentes da interface
label_usuario = tk.Label(janela, text="nome:")
label_usuario.pack(pady=5)

entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)

entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)

# Iniciando o loop da interface
janela.mainloop()
