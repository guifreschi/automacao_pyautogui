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

  # Criando campo name e email
  label_name = tk.Label(root, text='Name')
  label_name.pack()
  entry_name = tk.Entry(root)
  entry_name.pack()

  label_email = tk.Label(root, text='Email')
  label_email.pack()
  entry_email = tk.Entry(root)
  entry_email.pack()
  
  # Botão para adicionar aluno
  button_add = tk.Button(root, text='Add') 
  button_add.pack()
  
  root.mainloop()
