# Abrindo os dados do arquivo.Agora precisamos extrair dados dele
meuArquivo= open('0.in')

#print(meuArquivo.read())
listaNomes= meuArquivo.readlines()

#Printando o número de vértices
vertices=listaNomes[2].split('=',0)
print(vertices)
#print(listaNomes[2])

#Printando as arestas
for i in range(4, len(listaNomes)):
    print(listaNomes[i])

#

