dados = {}
lista = []

matriculasUFAL = {} 
matriculas_keys = []
salas = {}
chaves_pegas = {}

for x in range(1,101): 
  matriculasUFAL[f'{x}'] = f"Aluno{x}"

def cadastrar_aluno():
  while True:
    matricula = input("Matricula: ")
    if matricula not in matriculasUFAL.keys():
      print("Número de matrícula inválido!")
    else:
      if matricula not in matriculas_keys:
        dados['nome'] = matriculasUFAL[matricula]
        dados['matricula'] = matricula
        dados['celular'] = input(f"Olá, {dados['nome']}!\nInforme um número para contato: ")
        #ddd - 9 - 8digitos

        matriculas_keys.append(matricula)
        lista.append(dados.copy()) #
        #dados.clear()
        
        print(f"{matriculasUFAL[matricula]} agora faz parte do sistema.")
      else:
        print(f"Olá, {matriculasUFAL[matricula]} voce já está cadastrado no nosso sistema de controle das chaves.")
        print("--------------------------------")
      break
  print(matriculas_keys)#del
 
def chaves():
  print("\nCHAVES DISPONIVEIS:")
  for k,v in salas.items():
    if k not in chaves_pegas.keys():
      print(f"[{k}] {v}")

  if len(chaves_pegas) != 0:
    print("\nCHAVES RESERVADAS: ")
    for k,v in chaves_pegas.items():
        print(f"[{k}] {v}")

def pegar_chave():  
  #Lista com as salas (MANUALMENTE)
  lista = ["CID", "LICA", "LACCAN", "PET", "GTI", "LEC1"]

  #Atribuindo valores as chaves (automatico)
  for c,x in enumerate(lista):
      salas[c+1] = x
  chaves()
  print("------------------------------------------------")

  while True:
    matricula = input("Matricula: ")
    if matricula not in matriculas_keys:
      print("Aluno nao matriculado no sistema.")
    else:
      while True:
        cod = int(input("Código da Sala: "))
        if cod not in salas.keys():
          print("Digite um código válido")
        else: #ver s
          for k, v in salas.items():
            if cod == k:
              print(f"Liberado a chave:   \033[31m{v}\033[m")   
              chaves_pegas[k] = v
          break
    break

  chaves()

def devolver_chave():
  while True:
    cod = int(input("Código da sala: "))
    if cod not in chaves_pegas.keys():
      print("Didite um código válido")
    else:
      print(f"Devolvendo chave do \033[31m{salas[cod]}\033[m")
      chaves_pegas.pop(cod)
      break
  chaves()
      

