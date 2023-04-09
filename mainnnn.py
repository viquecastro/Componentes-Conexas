import funcoes as fun

#Criando variáveis importantes

listArq=fun.acessaArquivo('0.in')
listaArestas=fun.listaArestas(listArq)
numvertices=fun.numVertices(listArq)
vizinhosde4=fun.listaVizinhos(listaArestas,4)

#Temos a lista de arestas, agora precisamos percorrer essa lista caçando os vertices pra colocar na lista de adj

#procura pelo vertice 1. funçao verificaaresta

#print(listaArestas)
#print(listaArestas[1][2])

print(listaArestas)

listaAdjacencias=fun.listaAdj(listaArestas,numvertices)
print(listaAdjacencias)