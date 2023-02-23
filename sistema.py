from funcionalidades import cadastrar_aluno, pegar_chave, devolver_chave
from time import sleep

while True:
  print("="*36)
  print("|  SISTEMA DE ACESSO A LABORATÓRIOS |")
  print("="*36)
  print("              MENU ")
  print("-"*36)
  print("1- Lista de Alunos Cadastrados\n2- Cadastrar Novo Aluno\n3- Pegar Chave\n4- Devolver Chave\n5- Sair do Sistema")

  opc = input("Opçao: ")
  if opc.isdigit():
    opc = int(opc)
  #opc = int(input("Opção: "))

  if opc == 1:
    #ver_lista()
    sleep(3) 
    #funçao pra limpar a tela
  elif opc == 2:
    cadastrar_aluno()
  elif opc == 3:
    pegar_chave()
  elif opc == 4:
    devolver_chave()
  elif opc == 5:
    print("Saindo do Sistema, até logo!")
    sleep(3) 
    break
  else:
    print("\033[31mErro. Digite uma opçao válida.\033[m")
  sleep(3)