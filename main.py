import funcoes as fun

#Criando variáveis importantes

listArq=fun.acessaArquivo('0.in')
listaArestas=fun.listaArestas(listArq)
numvertices=fun.numVertices(listArq)
vizinhosde8=fun.listaVizinhos(listaArestas,8)
listaAdjacencias=fun.listaAdj(listaArestas,numvertices)
listaRotulos=fun.listaRotulos(numvertices+1)
vetorCC=[]
vetorComp=fun.rotuloAtribui(listaAdjacencias,1,listaRotulos,vetorCC)

#Temos a lista de arestas, agora precisamos percorrer essa lista caçando os vertices pra colocar na lista de adj

#procura pelo vertice 1. funçao verificaaresta

print(listArq)
print(listaArestas)
print(numvertices)
print(vizinhosde8)
print(type(vizinhosde8[1]))
print(listaAdjacencias)
print(listaAdjacencias[9][1])
print(listaRotulos)
print(vetorCC)