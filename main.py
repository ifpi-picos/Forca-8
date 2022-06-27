import random
import opções_menu
import ranking

print("*********************************")
print("***Bem vindo ao jogo da forca!***")
print("*********************************")
print()
print("||===== ")
print("||    | ")
print("||    O ")
print("||   /|\ ")
print("||    | ")
print("||   / \ ")
print("||__ __ __ __ __")
print()
print()

print("**************MENU***************")
print()

cont = 0
opcao_tema = 0
opcao = int(input("Escolha uma opção:\n [ 1 ] Jogar\n [ 2 ] Temas\n [ 3 ] Ranking\n [ 4 ] Sair\n"))

somatoria = 0

while(opcao != 4):
  
  if(opcao_tema == 5):
    opcao = int(input("Escolha uma opção:\n [ 1 ] Jogar\n [ 2 ] Temas\n [ 3 ] Ranking\n [ 4 ] Sair\n"))

  if(opcao == 1):

    while(True):
      if(cont == 1):
        break
      nivel = int(input("Escolha a dificuldade:\n [ 1 ]Fácil\n [ 2 ]Médio\n [ 3 ]Difícil\n"))
      if(nivel == 1):
        dificuldade = 10
        valor_pontuacao = 10
      elif(nivel == 2):
        dificuldade = 7
        valor_pontuacao = 30
      elif(nivel == 3):
        dificuldade = 4
        valor_pontuacao = 60

      while(nivel < 1 or nivel > 3):
        print("OPÇÃO INVALIDA")
        nivel = int(input("Escolha a dificuldade:\n [ 1 ]Fácil\n [ 2 ]Médio\n [ 3 ]Difícil\n"))
        if(nivel == 1):
          dificuldade = 10
          valor_pontuacao = 10
        elif(nivel == 2):
          dificuldade = 7
          valor_pontuacao = 20
        elif(nivel == 3):
          dificuldade = 4
          valor_pontuacao = 30
      cont = 1
    print("----> VOCÊ PODE ERRAR {} VEZES <----".format(dificuldade))
    
    palavra_secreta_lista = ["Python 3", "Java", "Ruby", "Cobol", "JavaScript", "Assembly", "PHP", "c++"]
    palavra_secreta = random.choice(palavra_secreta_lista)
    letras_acertadas = []

    for i in palavra_secreta:
      if(i != " "):
        letras_acertadas.append("_")
      else:
        letras_acertadas.append(" ")

    enforcou  = 0
    acertou = False

    print(" ".join(letras_acertadas))


    while(enforcou != dificuldade and not acertou):

      chute = input("Número de erros -> {} -- Qual letra? ".format(enforcou))
      chute = chute.strip()

      if(chute.upper() not in palavra_secreta.upper()):
        enforcou+=1

      index = 0
      for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
          letras_acertadas[index] = letra
        index += 1

      print(" ".join(letras_acertadas))

      if("_" not in letras_acertadas):
        acertou = True
        somatoria+=valor_pontuacao

    if(enforcou == dificuldade):
      print("Você errou {} vezes!".format(dificuldade))
      print("Sua pontuação foi: {}".format(somatoria))
      break

    continuar = input("Você deseja continuar jogando? [S/N]\n")
    if(continuar.upper() == "N"):
      opcao = 4
  elif(opcao == 2):
    print("[ 1 ] Listar temas\n[ 2 ] Adicionar temas\n[ 3 ] Remover tema\n[ 4 ] Remover palavra de tema\n[ 5 ] Voltar")
    opcao_tema = int(input())
    if(opcao_tema == 1):
      print()
      ver = opções_menu.ver_tema()
      for i in ver:
        print(i)
      print()
      print("Deseja retornar ao menu inicial? [S]")
      variavel = input().upper()
      while(variavel != "S"):
        print("Valor inválido, digite novamente: ")
        variavel = input().upper()
      opcao_tema = 5
    elif(opcao_tema == 2):
      opções_menu.adicionar()
      opcao_tema = 5
  elif(opcao == 3):
    ranking.organizar()
    print()
    print("Deseja retornar ao menu inicial? [S]")
    variavel = input().upper()
    while(variavel != "S"):
      print("Valor inválido, digite novamente: ")
      variavel = input().upper()
    opcao_tema = 5

opções_menu.pontuacao(somatoria)
if(somatoria != 0):
  cadastro = input("Como deseja ser chamado? \n").upper()
  opções_menu.participantes(cadastro)
  print("Sua pontuação foi: {}".format(somatoria))
print("Fim do jogo!")
print()
print()