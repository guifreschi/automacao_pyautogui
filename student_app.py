import tkinter as tk
from tkinter import ttk

def executer():
  """
  Inicia uma interface gráfica para o cadastro de alunos.

  Esta função cria uma janela Tkinter com campos para nome e email,
  uma tabela TreeView para exibir os alunos cadastrados, e um botão para
  adicionar alunos à tabela.

  A janela é posicionada em uma localização fixa na tela.
  """
  
  # Define a posição fixa da janela
  root = tk.Tk()
  root.title('Cadastro de Alunos')
  root.geometry("700x700+500+100")
   
  # Cria a tabela TreeView
  tree = ttk.Treeview(root, columns=('Name', 'Email'))
  tree.heading('Name', text='Name')
  tree.heading('Email', text='Email')
  tree.pack()

