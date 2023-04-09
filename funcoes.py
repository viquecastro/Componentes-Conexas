#Essas são as funções que usaremos durante a execução do programa

#Função que acessa o arquivo de instâncias e retorna uma lista com as linhas do arquivo
def acessaArquivo(arq):
    meuArquivo= open(arq)
    listaInicial= meuArquivo.readlines()
    return listaInicial

#Função que cria a lista de arestas do arquivo
def listaArestas(listaInicial):
    novaLista=[]
    for i in range(4, len(listaInicial)):
        aux1=listaInicial[i]
        aux2=aux1[0:3]
        novaLista.append(aux2)
        #novaLista.append(listaInicial[i])
    return novaLista

#Função que retorna o número de vértices
def numVertices(listaInicial):
    vertices=listaInicial[2].split('=')
    numeroVerices=int(vertices[1])
    return numeroVerices


#Função que retorna a lista de vértices vizinhos de um vértice X
def listaVizinhos(novaLista,x):
    arestasDeX=[]
    for i in novaLista:
        if x==int(i[0]):
            arestasDeX.append(int(i[2]))
        elif x==int(i[2]):
            arestasDeX.append(int(i[0]))
    arestasDeX.sort()
    return arestasDeX

#criando a lista de adjacências

def listaAdj(novaLista,numVertices):
    adjList= {}
    adjList[0]=['avulso']
    for i in range (1,numVertices):
        adjList[i]=listaVizinhos(novaLista,i)
    return adjList
