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
    vizinhos= {}
    vizinhos[0]=[0]
    for i in range (1,numVertices+1):
        vizinhos[i]=listaVizinhos(novaLista,i)
    return vizinhos

#Função que cria uma lista de rótulos inicializados com falso
def listaRotulos(numVertices):
    rotulos={}
    for i in range(numVertices):
        rotulos[i]=False
    return rotulos

#Função que cria uma lista que guarda a componente atual que está sendo visitada
#def componente(verticeOrigem):
#   recebe um vertice e retorna a lista de componentes na qual ele esta inserido

#Função que armazena as componentes de um grafo
#def componentesConexas():
#    uyhy



#Função que atribui rótulos para os vértices que estejam na mesma componente conexa. Retorna UMA componente conexa.depois que a funçao é executada dentro do laço, faz o append da componente no vetor componentes
def rotuloAtribui(adjList,vertice,rotlist,vetorCC):
   #Selecionar a origem e marcá-la como descoberta
   rotlist[vertice]=True
   vetorCC.append(vertice) 
   if adjList[vertice]==[]:
       return vetorCC
   else:
       for i in range(len(adjList[vertice])):
        if rotlist[adjList[vertice][i]]==True:
            continue 
        else:
            rotuloAtribui(adjList,adjList[vertice][i],rotlist,vetorCC)
        return vetorCC
            
    

