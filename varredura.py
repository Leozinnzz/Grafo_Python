import networkx as nx
import matplotlib.pyplot as plt

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

G = nx.from_dict_of_lists(dict_adj)

pos = nx.spring_layout(G, k=1.2)

def bfs_edges_path(G, source, target):
    predecessores = {source: None}
    fila = [source]
    alvo_encontrado = False

    while fila:
        atual = fila.pop(0)

        if atual == target:
            alvo_encontrado = True
            break

        for vizinho in G.neighbors(atual):
            if vizinho not in predecessores:
                predecessores[vizinho] = atual
                fila.append(vizinho)

    if not alvo_encontrado and target not in predecessores:
        return []

    arestas_caminho = []
    passo_atual = target

    while predecessores[passo_atual] is not None:
        pai = predecessores[passo_atual]
        arestas_caminho.insert(0, (pai, passo_atual))
        passo_atual = pai

    return arestas_caminho

bfs = bfs_edges_path(G, source="A", target="H")

n_colors_dict = {n: "lightblue" for n in G.nodes()}
e_colors_dict = {e: "gray" for e in G.edges()}


for i,(u, v) in enumerate (bfs):
    n_colors_dict[u] = "lightgreen"
    n_colors_dict[v] = "lightgreen"
    e_colors_dict[(u, v)] = "lightgreen"

    plt.clf()
    nx.draw(G, pos, edge_color=e_colors_dict.values(), node_color=n_colors_dict.values(), with_labels=True)
    plt.savefig(f"bfs_passo{i}.png", dpi=400)

def dfs_edges_path(G, source, target):
    pilha = [(source, [])]
    visitados = set()

    while pilha:
        atual, caminho_arestas = pilha.pop()

        if atual == target:
            return caminho_arestas

        if atual not in visitados:
            visitados.add(atual)

            for vizinho in reversed(list(G.neighbors(atual))):
                if vizinho not in visitados:
                    nova_aresta = (atual, vizinho)
                    pilha.append((vizinho, caminho_arestas + [nova_aresta]))
    return []


dfs = dfs_edges_path(G, source="A", target="H")

n_colors_dict = {n: "lightblue" for n in G.nodes()}
e_colors_dict = {e: "gray" for e in G.edges()}

for i, (u, v) in enumerate(dfs):
    n_colors_dict[u] = "purple"
    n_colors_dict[v] = "purple"
    e_colors_dict[(u, v)] = "purple"

    plt.clf()
    nx.draw(G, pos, edge_color=e_colors_dict.values(), node_color=n_colors_dict.values(), with_labels=True)
    plt.savefig(f"dfs_passo_{i}.png", dpi=400)

plt.clf()
nx.draw(G, pos, edge_color=list(e_colors_dict.values()), node_color=list(n_colors_dict.values()), with_labels=True)
plt.savefig("dfs_final.png", dpi=400)

plt.clf()
nx.draw(G, pos, edge_color="gray", node_color="green", with_labels=True)
plt.savefig("grafo.png", dpi=400)

