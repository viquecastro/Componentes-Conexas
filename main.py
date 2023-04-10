import funcoes as fun

#Criando variáveis importantes

listArq=fun.acessaArquivo('0.in')
listaArestas=fun.listaArestas(listArq)
numvertices=fun.numVertices(listArq)
vizinhosde2=fun.listaVizinhos(listaArestas,2)

#Temos a lista de arestas, agora precisamos percorrer essa lista caçando os vertices pra colocar na lista de adj

#procura pelo vertice 1. funçao verificaaresta

print(listArq)
print(listaArestas)
print(numvertices)
print(vizinhosde2)


listaAdjacencias=fun.listaAdj(listaArestas,numvertices)
print(listaAdjacencias)

