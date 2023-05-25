import matplotlib.pyplot as plt
import networkx as nx
import math

# Método para obtener la distancia entre dos nodos
def getDistancia(lat1, long1, lat2, long2):
    # Coordenadas de la Ciudad 1 en radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(long1)

    # Coordenadas de la Ciudad 2 en radianes
    lat2 = math.radians(lat2)
    lon2 = math.radians(long2)

    # Radio de la Tierra en kilómetros
    rrr = 6378.388

    # Cálculo de las diferencias de latitud y longitud
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Cálculo de la fórmula de la haversine
    a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dij = rrr * c
    dij = round(dij,4)
    return dij

# Método para mostrar la gráfica de un grafo
def mostrarGrafo(grafo):
    # Visualizar el grafo
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray', width=1.5)
    edge_labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    plt.show()


if __name__ == '__main__':
    # Grafo dirigido vacío
    grafo = nx.DiGraph()

    # Matriz de adyacencia  
    matriz = [
   # Ciudades     
   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]]

    # Agregar ciudades 1-16 al grafo
    for valor in range(1,17):
        var = f"Ciudad {valor}"
        grafo.add_node(var)

    # Lectura del archivo tsp y creación de lista vacía
    archivo = 'ulysses16.tsp'
    ciudades = [[],[]]

    # Bucle para ingresar coordenadas en lista
    with open(archivo, 'r') as tsp:
        inicio = False
        # Leer las lineas del archivo
        for linea in tsp:
            # Procesar las líneas de la sección NODE_COORD_SECTION
            if inicio:
                if linea.strip() == 'EOF':
                    break  # Salir del bucle cuando se encuentra 'EOF'
                lat, long = map(float, linea.split()[1:])
                ciudades[0].append(lat)
                ciudades[1].append(long)
            elif linea.startswith('NODE_COORD_SECTION'):
                inicio = True

    # Bucle para agregar conexiones y distancias
    # Lectura de ciudades
    for indiceA, adyacencia in enumerate(matriz):
        # Lectura de nodos dentro de la ciudad
        for indiceN, nodo in enumerate(adyacencia):
            # Verificar si existe adyacencia
            if nodo == 1:
                ciudadInicio = f"Ciudad {indiceA+1}"
                ciudadDestino = f"Ciudad {indiceN+1}"
                distancia = getDistancia(ciudades[0][indiceA], ciudades[1][indiceA], ciudades[0][indiceN], ciudades[1][indiceN])
                grafo.add_edge(ciudadInicio, ciudadDestino, weight=distancia)


    # Aplicar el algoritmo de Dijkstra para encontrar el camino más corto y su distancia

    # Bucle para obtener el camino y la distancia más corta
    print('------------------------------------------------------')
    for i in range(1,17):
        destino = f'Ciudad {i}'
        # Aplicación de Dijkstra
        camino_mas_corto = nx.dijkstra_path(grafo, "Ciudad 1", destino, weight="weight")
        distancia_mas_corta = nx.dijkstra_path_length(grafo, "Ciudad 1", destino, weight="weight")
        distancia_mas_corta = round(distancia_mas_corta,4)
        # Impresión de la tabla
        print(f'Ruta hacia {i}: {camino_mas_corto}')
        print(f'Costo: {distancia_mas_corta}Km')
        print('------------------------------------------------------')
    mostrarGrafo(grafo)