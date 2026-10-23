from collections import deque 
import networkx as nx 
import matplotlib as plt 


def dfs(dict_adj, source, target):
    pilha = [(source, [])]
    visitados = set()

    while pilha:
        atual, caminho_arestas = pilha.pop()

        if atual == target:
            return caminho_arestas
        
        if atual not in visitados: 
            visitados.add(atual)

        for vizinhos in reversed(dict_adj[atual]):
            if vizinhos not in visitados:
                nova_aresta = (atual, vizinhos)
                pilha.append((vizinhos, caminho_arestas + [nova_aresta]))


def bfs(dict_adj, source, target): 
    fila = deque([source])

    visitados = {source} 

    pais = {source: None}


    while fila:

        atual = fila.popleft()
        print(f"Visitando o vertice {atual} ")

        if atual == target:
            print(f"Vertice {target} encontrado")
            return True

        for vizinhos in dict_adj[atual]:
            if vizinhos not in visitados:
                visitados.add(vizinhos)
                pais[vizinhos] = atual
                fila.append(vizinhos)

    print(f"Alvo {target} nao encontrado no grafo")
    return False
        
dict_adj = {
    "A": ["B"],
    "B": ["C", "D", "E"],
    "C": ["E", "F"],
    "D": ["I", "J"],
    "E": ["C", "F", "G", "H"], 
    "F": ["C", "E", "G"],
    "G": ["E", "F", "H"],
    "H": ["E", "G"],
    "I": ["D"],
    "J": ["D"],
}


dfs(dict_adj, "A", "J")



