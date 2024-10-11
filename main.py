import subprocess
import pyautogui
from time import sleep

# Executa student_app.py como um subprocesso
subprocess.Popen(['python', 'student_app.py'])
sleep(1)

with open('alunos.txt', 'r', encoding='utf-8') as  file:
  for line in file:
    aluno = line.split(',')[0]
    email = line.split(',')[1]
    
    # Coordenadas dos campos na janela
    # Campo "Aluno": 1260, 580
    # Campo "Email": 1260, 645
    # Botão "Add": 1300, 675
    
    # Clicando em "Aluno" e escrevendo o nome do aluno
    pyautogui.click(1260, 580, duration=1)
    sleep(1)
    pyautogui.write(aluno)
    
    # Clicando em "Email" e escrevendo o email
    pyautogui.click(1260, 645, duration=1)
    sleep(1)
    pyautogui.write(email)
    
    # Clicando em "Add"
    pyautogui.click(1300, 675, duration=0.5)
    sleep(1)
