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


#Função que contabiliza o total de componentes
def qtdeComp(todasCompConexas,numvertices):
    cont=0
    for i in range(numvertices):
        if todasCompConexas[i]!=None:
            cont=cont+1
        else:
            break
    return cont


#Função que atribui rótulos para os vértices que estejam na mesma componente conexa. Retorna UMA componente conexa.depois que a funçao é executada dentro do laço, faz o append da componente no vetor componentes
def criaComponente(adjList,vertice,rotlist,vetorCC):
   rotlist[vertice]=True
   vetorCC.append(vertice) 
   if adjList[vertice]==[]:
       return vetorCC
   else:
       for i in range(len(adjList[vertice])):
        if rotlist[adjList[vertice][i]]==True:
            continue 
        else:
            criaComponente(adjList,adjList[vertice][i],rotlist,vetorCC)
        return vetorCC
   
#Função que ordena as componentes 
def ordenaComp(formatComponentes):
    for i in range(len(formatComponentes)):
        formatComponentes[i].sort()
    return formatComponentes
    
#Função que printa as linhas da saída do programa
def printLines(formatComponentes):
    for i in range(len(formatComponentes)):
        #tratamento de strings
        line1=str(formatComponentes[i])
        line2=line1[1:]
        line3=line2[:-1]
        line4=line3.replace(",","")
        print(line4)

        

