import networkx as nx
import matplotlib.pyplot as plt
import csv
import heapq
import itertools

class Graph():
    def __init__(self):
        self.G = nx.Graph()
        self.G2 = nx.Graph()

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

    #def insert(self, nodo_inicial, nodo_final, peso):
    #    self.G.add_edge(nodo_inicial, nodo_final, weight=peso)

    #def insert2(self, nodo_inicial, nodo_final):
    #    self.G2.add_edge(nodo_inicial, nodo_final)

    def return_kw(self, nodo):
        for a, b in self.G.nodes(data=True):
            if a == nodo:
                return b['KW']
            
    def returnweight(self, nodo_inicial, nodo_final):
        for a, b, d in self.G.edges(data=True):
            if a == nodo_inicial and b == nodo_final:
                return float(d['weight'])

    def dijkstra_shortest_path(self, source, target):
        distances = {node: float('inf') for node in self.G}
        distances[source] = 0
        previous = {node: None for node in self.G}

        queue = [(0, source)]
        heapq.heapify(queue)

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == target:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.G[current_node].items():
                distance = current_distance + weight['weight']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        current_node = target
        while current_node is not None:
            path.insert(0, current_node)
            current_node = previous[current_node]

        return path
                
    def returnhighestkw(self, min_path):
        aux = list()
        for ide in min_path:
            aux.append(self.return_kw(ide))
        return max(aux)
    
    def returnsumkw(self, min_path):
        aux = list()
        for ide in min_path:
            aux.append(self.return_kw(ide))
        return sum(aux)
    
    def showgraph(self):
       pos = nx.spring_layout(self.G, k=1, iterations=2)
       nx.draw(self.G, pos, with_labels=True)
       labels = nx.get_edge_attributes(self.G, 'weight')
       nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, font_size=2, alpha=0.7)
       nx.draw_networkx_edges(self.G,pos,width=0.5,alpha=0.5)
       plt.show()
    
    def connection_exists(self, nodo_a, nodo_b): return True

    def showgraphdijkstra(self, min_path):
        self.G2.add_nodes_from(min_path)

        combinaciones = list(itertools.combinations(min_path, 2))
        if len(combinaciones) > 1:
            combinaciones.remove((min_path[0], min_path[len(min_path) - 1]))
            
        for combinacion in combinaciones:
            nodo_a, nodo_b = combinacion
            if self.connection_exists(nodo_a, nodo_b):
                peso = self.returnweight(nodo_a, nodo_b)
                self.G2.add_edge(nodo_a, nodo_b, weight=peso)

        subgrafo = self.G.subgraph(min_path)
        edges = subgrafo.edges()
        weights = [subgrafo[u][v]['weight'] for u, v in edges]
        labels = nx.get_edge_attributes(subgrafo, 'weight')

        pos = nx.spring_layout(self.G2, k=1, iterations=2)
        nx.draw_networkx_nodes(subgrafo, pos, node_size=10)
        nx.draw_networkx_labels(subgrafo, pos, labels={nodo: str(nodo) for nodo in subgrafo.nodes()}, font_size=10, font_color='black', alpha=0.7)
        nx.draw_networkx_edges(subgrafo, pos, width=2.0, alpha=0.8, edge_color='red')
        nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels, font_size=10, alpha=0.7)
        plt.axis('off')
        plt.show()