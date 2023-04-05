# Componentes-Conexas
 Trabalho de implementação 1 da disciplina de Algoritmos em Grafos

Escreva um programa que receba um grafo não-direcionado e que escreva as suas componentes conexas. Uma componente conexa é um conjunto maximal de vértices ligados por caminhos no grafo.

A entrada, recebida através da entrada padrão, estará no formato UCINET DL, lista de arestas ("edgelist1"), sem rótulos para os vértices e sem pesos para as arestas.

A saída, fornecida através da saída padrão, tem que estar no seguinte formato:

    1- Deve ser impressa uma componente conexa por linha.

    2- Em cada linha, os vértices devem aparecer em ordem crescente, separados por um espaço em branco, mas sem um espaço em branco após o último vértice.

    3- A primeira linha deve ser a da componente conexa do vértice 1. A segunda linha deve ser a da componente conexa do vértice 2, exceto se ele já tiver aparecido na componente conexa do vértice 1, e assim sucessivamente, ou seja: cada uma das outras linhas contém os vértices da componente conexa do vértice de menor rótulo que não tenha aparecido nas componentes listadas em linhas anteriores.

Importante:
    A saída não precisa ser escrita toda de uma vez, ou seja, você pode gerar a saída em partes. O que importa é que a saída gerada pela execução do seu programa, se considerada como um todo, esteja no formato indicado acima.