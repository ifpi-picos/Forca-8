import opções_menu

def organizar():
  lista_nomes = opções_menu.ver_participantes()
  lista_pontos = opções_menu.ver_pontuacao()

  for i in range(len(lista_pontos)):
    for j in range(len(lista_pontos)):
      if(lista_pontos[i] > lista_pontos[j]):

        aux_pontos = lista_pontos[i]
        lista_pontos[i] = lista_pontos[j]
        lista_pontos[j] = aux_pontos

        aux_nomes = lista_nomes[i]
        lista_nomes[i] = lista_nomes[j]
        lista_nomes[j] = aux_nomes

  if(len(lista_nomes) != 0):
    for l in range(len(lista_pontos)):
      print("{} - {} {}".format(l+1, lista_nomes[l], lista_pontos[l]))
  else:
    print()
    print("***Histórico de partidas inexistente***")