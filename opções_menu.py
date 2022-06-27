def adicionar():
  while True:
    nome_categoria = input("qual o nome da nova categoria?\n").upper()
    todos_temas = open("todos_os_temas.txt", 'a')
    todos_temas.write(nome_categoria + '\n')
    todos_temas.close()
    print("digite abaixo os elementos que deseja adicionar:")
    elementos = open(nome_categoria + '.txt', 'w')
    while True:
      palavra = input()
      elementos.write(palavra + '\n')
      esc1 = input("deseja adicionar mais um elemento?[S/N]").upper()
      if esc1 == "N":
        elementos.close()
        print("sua Categoria foi criada com sucesso!!")
        break;
    esc2 = str(input("deseja criar mais uma categoria?[S/N]")).upper()
    if esc2 == "N":
      break;


def ver_tema():
  doc = open('todos_os_temas.txt', 'r')
  lista= []
  for tema in doc:
    tema= tema.strip()
    lista.append(tema)
  doc.close()
  return lista


def ver_elementos(tema):
  elemento= (tema+'.txt','r')
  lista=[]
  for c in tema:
    lista.append(c)
  elemento.close()
  return lista

def participantes(nome_participante):
  todos_os_participantes = open("nomes.txt", "a")
  todos_os_participantes.write(nome_participante + '\n')
  todos_os_participantes.close()

def pontuacao(somatoria):
  todos_os_pontos = open("pontos.txt", "a")
  todos_os_pontos.write(str(somatoria) + "\n")
  todos_os_pontos.close()

def ver_participantes():
  pessoa = open('nomes.txt', 'r')
  lista_pessoa = []
  for i in pessoa:
    i = i.strip()
    lista_pessoa.append(i)
  pessoa.close()
  return lista_pessoa

def ver_pontuacao():
  ponto = open('pontos.txt', 'r')
  lista_pontuacao = []
  for i in ponto:
    i = i.strip()
    lista_pontuacao.append(int(i))
  ponto.close()
  return lista_pontuacao