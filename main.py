import funcoes as fun

#Criando variáveis importantes

listArq=fun.acessaArquivo('0.in')
listaArestas=fun.listaArestas(listArq)
numvertices=fun.numVertices(listArq)
vizinhosde8=fun.listaVizinhos(listaArestas,8)
listaAdjacencias=fun.listaAdj(listaArestas,numvertices)
listaRotulos=fun.listaRotulos(numvertices+1)
vetorCC=[]

#Lógica pra armazenar as componentes conexas

todasCompConexas=[]
for i in range(1,numvertices):
    componente=fun.criaComponente(listaAdjacencias,i,listaRotulos,vetorCC)
    #componente.sort()
    todasCompConexas.append(componente)
    vetorCC=[]


#Criar variável que só pode ser criada após o bloco de código acima
numComponentes=fun.qtdeComp(todasCompConexas,numvertices)

#Formatando a lista com todas as componentes conexas(tirar os 'none')
formatComponentes=todasCompConexas[0:numComponentes]

#Ordenando a lista com todas as componentes conexas
todasCompConexas=fun.ordenaComp(formatComponentes)





#Prints importantes
print(numComponentes)
print(listArq)
print(listaArestas)
print(numvertices)
print(vizinhosde8)
print(type(vizinhosde8[1]))
print(listaAdjacencias)
print(listaAdjacencias[9][1])
print(listaRotulos)
#print(vetorComp)
print(todasCompConexas)
print(type(todasCompConexas[0][0]))
print(todasCompConexas[1][0])
print(len(todasCompConexas))
print(formatComponentes)


fun.printLines(formatComponentes)