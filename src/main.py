import matplotlib.pyplot as plt
import networkx as nx


def path_image_generator(G, pos, path_name, graph_path):
    n_colors_dict = {n: "lightblue" for n in G.nodes()}
    e_colors_dict = {e: "gray" for e in G.edges()}

    for edge in graph_path:
        n_colors_dict[edge[0]] = "lightgreen"
        n_colors_dict[edge[1]] = "lightgreen"
        e_colors_dict[edge] = "lightgreen"

    plt.clf()
    nx.draw(
        G,
        pos,
        edge_color=e_colors_dict.values(),
        node_color=n_colors_dict.values(),
        with_labels=True,
        labels=labels,
        node_size=1200,
    )
    plt.savefig(f"{path_name}.png", dpi=400)


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
    "J": ["D"]
}

labels = {
    "A": "Entrada",
    "B": "Gabinete",
    "C": "Biblioteca",
    "D": "Médio",
    "E": "Superior",
    "F": "Agro Industria",
    "G": "Médio porte",
    "H": "Grande porte",
    "I": "Refeitório",
    "J": "Posto de vendas",
}

G = nx.from_dict_of_lists(dict_adj)

pos = nx.spring_layout(G, k=1, seed=70294)

dfs = dfs_edges_path(G, source="A", target="H")
bfs = bfs_edges_path(G, source="A", target="H")

path_image_generator(G, pos, "dfs_path", dfs)
path_image_generator(G, pos, "bfs_path", bfs)

path_image_generator(G, pos, "dfs", nx.dfs_edges(G))
path_image_generator(G, pos, "bfs", nx.bfs_edges(G, source="A"))

plt.clf()
nx.draw(G, pos, edge_color="gray", node_color="lightblue", with_labels=True, labels=labels, node_size=1200)
plt.savefig("grafo.png", dpi=400)
