import csv
import networkx as nx
import matplotlib.pyplot as plt

class BFS():
    def __init__(self):
        self.nodos = {}
        self.G = nx.Graph()

        with open("Nodo.csv", 'r') as archivo:
            lector_csv = csv.reader(archivo)
            cabeceras = next(lector_csv)
            for fila in lector_csv:
                nodo = fila[0]
                parametros = {'KW': float(fila[1])}
                self.G.add_node(nodo, **parametros)
               
        with open("Aristas.csv", 'r') as archivo:
            lector_csv = csv.reader(archivo)
            cabeceras = next(lector_csv)
            for fila in lector_csv:
                nodo_inicial = fila[0]
                nodo_final = fila[1]
                peso = float(fila[2])
                self.G.add_edge(nodo_inicial, nodo_final, weight=peso)

    def BFS_path(self, inicio, final):
        visitados = set()
        camino_actual = [inicio]
        peso_actual = 0
        mejor_camino, mejor_peso = self.max_path(inicio, final, camino_actual, peso_actual, visitados)
        return mejor_camino, mejor_peso
    
    def max_path(self, nodo_actual, nodo_final, camino_actual, peso_actual, visitados):
        visitados.add(nodo_actual)

        caminos = []

        for vecino in self.G.neighbors(nodo_actual):
            if vecino not in visitados:
                peso_arista = self.G[nodo_actual][vecino]['weight']
                nuevo_peso = peso_actual + peso_arista
                nuevo_camino = camino_actual + [vecino]
                caminos.append((nuevo_camino, nuevo_peso))

        if not caminos or nodo_actual == nodo_final:
            return camino_actual, peso_actual

        caminos.sort(key=lambda x: x[1], reverse=True)
        mejor_camino, mejor_peso = caminos[0]

        if mejor_peso > peso_actual:
            return self.max_path(mejor_camino[-1], nodo_final, mejor_camino, mejor_peso, visitados.copy())

        return camino_actual, peso_actual

    
    def showBFS(self, camino):
        subgrafo = self.G.subgraph(camino)
        edges = subgrafo.edges()
        weights = [subgrafo[u][v]['weight'] for u, v in edges]
        labels = nx.get_edge_attributes(subgrafo, 'weight')
        pos = nx.spring_layout(self.G, k=1, iterations=2)
        nx.draw_networkx_nodes(subgrafo, pos, node_size=10)
        nx.draw_networkx_labels(subgrafo, pos, labels={nodo: str(nodo) for nodo in subgrafo.nodes()}, font_size=10, font_color='black', alpha=0.7)
        nx.draw_networkx_edges(subgrafo, pos, width=2.0, alpha=0.8, edge_color='red')
        nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels, font_size=10, alpha=0.7)
        plt.axis('off')
        plt.show()