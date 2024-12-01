import json  # Importar la librería para manejar archivos JSON

# Datos del grafo (estaciones y conexiones)
graph_data = {
    "nodes": ["A", "B", "C", "D", "E"],  # Estaciones
    "edges": [  # Conexiones con pesos
        {"source": "A", "target": "B", "weight": 2},
        {"source": "A", "target": "C", "weight": 5},
        {"source": "B", "target": "D", "weight": 1},
        {"source": "C", "target": "D", "weight": 4},
        {"source": "D", "target": "E", "weight": 3}
    ]
}

# Guardar los datos en un archivo llamado "grafo.json"
with open("grafo.json", "w") as archivo_json:
    json.dump(graph_data, archivo_json, indent=4)  # Guardar en formato JSON

print("El archivo grafo.json se creó correctamente.")