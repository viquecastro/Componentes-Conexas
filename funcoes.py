#Essas são as funções que usaremos durante a execução do programa

#Função que acessa o arquivo de instâncias e retorna uma lista com as linhas do arquivo "cruas"
def acessaArquivo(arq):
    meuArquivo= open(arq)
    listaInicial= meuArquivo.readlines()
    return listaInicial

#Função que cria a lista de arestas do arquivo formatadas
def listaArestas(listaInicial):
    novaLista=[]
    for i in range(4, len(listaInicial)):
        aux1=listaInicial[i]
        size=len(aux1)
        aux2=aux1[:size -1]
        novaLista.append(aux2)
    return novaLista

#Função que retorna o número de vértices totais do grafo
def numVertices(listaInicial):
    vertices=listaInicial[2].split('=')
    numeroVerices=int(vertices[1])
    return numeroVerices


#Função que retorna a lista de vértices vizinhos de um vértice X
def listaVizinhos(novaLista,x):
    arestasDeX=[]
    for i in novaLista:
        listaAux=i.split()
        if x==int(listaAux[0]):
            arestasDeX.append(int(listaAux[1]))
        elif x==int(listaAux[1]):
            arestasDeX.append(int(listaAux[0]))
    arestasDeX.sort()
    return arestasDeX

#Função que cria lista de adjacências usando dicionário
def listaAdj(novaLista,numVertices):
    adjList= {}
    adjList[0]=[0]
    for i in range (1,numVertices+1):
        adjList[i]=listaVizinhos(novaLista,i)
    return adjList
