import networkx as nx

# Crear un grafo (representa el sistema de transporte)
G = nx.Graph()

# Añadir nodos (paradas o estaciones)
G.add_nodes_from(["A", "B", "C", "D", "E"])

# Añadir aristas (conexiones entre las estaciones con pesos, que representan distancias o tiempo)
G.add_edge("A", "B", weight=2)
G.add_edge("A", "C", weight=5)
G.add_edge("B", "D", weight=1)
G.add_edge("C", "D", weight=3)
G.add_edge("D", "E", weight=4)

# Calcular la ruta más corta entre A y E
shortest_path = nx.shortest_path(G, source="A", target="E", weight="weight")

# Mostrar la mejor ruta
print("La mejor ruta de A a E es:", shortest_path)
