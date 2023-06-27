from guizero import App, Text, PushButton, ButtonGroup, Combo, Picture
from algoritmo import Graph
from filtro import CSVReader
from bfs import BFS

app = App(title="Electro Ucayali S.A.")

combo_inicio = None
combo_final = None

def dijkstra():
    metodo = Graph()
    
    result = metodo.dijkstra_shortest_path(combo_inicio.value, combo_final.value)
    texto = " ".join(result)
    
    Text(app, text=texto, font="Times New Roman")
    metodo.showgraphdijkstra(result)
    #metodo.showgraphdijkstra(result)
    print(metodo.returnsumkw(result))

def bfs():
    metodobfs = BFS()
    camino, peso = metodobfs.BFS_path(combo_inicio.value, combo_final.value)
    metodobfs.showBFS(camino)
    
def filtro1():
    global combo_inicio
    global combo_final

    lector_inicio = CSVReader('Nodo.csv')
    lector_inicio.leer_csv(provincia1.value, distrito1.value)
    nodos1 = lector_inicio.obtener_columna1()
    
    for elemento in nodos1:
        print(elemento)
        print("Entra al nodo1")
    
    lector_final = CSVReader('Nodo.csv')
    lector_final.leer_csv(provincia2.value, distrito2.value)
    nodos2 = lector_final.obtener_columna1()

    for elemento1 in nodos2:
        print(elemento1)
        print("Entra al nodo2")
    
    if nodos1 and nodos2:
        nodoinicio = Text(app, text="Nodo Inicial")
        combo_inicio = Combo(app, options=nodos1, selected=nodos1[0])
  
        nodofinal = Text(app, text="Nodo Final")
        combo_final = Combo(app, options=nodos2, selected=nodos2[0])
    else:
        falla = Text(app, text="Al menos uno de los nodos está vacío.")

# -----------------------------------------------INICIO----------------------------------------------
Text(app, text="")
logo = Picture(app, image="ucayali.png", width=400, height=80)
Text(app, text="")

# Opciones para filtrar los nodos
# Nodo 1
Text(app, text="Nodo Inicial")
provincia1 = ButtonGroup(app, options=['ATALAYA', 'CORONEL PORTILLO', 'PADRE ABAD', 'PURUS'], horizontal=True)
distrito1 = ButtonGroup(app, options=['RAYMONDI', 'CALLERIA', 'CAMPOVERDE', 'MANANTAY', 'MASISEA', 'NUEVA REQUENA', 'YARINACOCHA', 'ALEXANDER VON HUMBOLT', 'CURIMANA', 'IRAZOLA', 'NESHUYA', 'PADRE ABAD', 'PURUS'], horizontal=True)
# Nodo 2
Text(app, text="Nodo Final")
provincia2 = ButtonGroup(app, options=['ATALAYA', 'CORONEL PORTILLO', 'PADRE ABAD', 'PURUS'], horizontal=True)
distrito2 = ButtonGroup(app, options=['RAYMONDI', 'CALLERIA', 'CAMPOVERDE', 'MANANTAY', 'MASISEA', 'NUEVA REQUENA', 'YARINACOCHA', 'ALEXANDER VON HUMBOLT', 'CURIMANA', 'IRAZOLA', 'NESHUYA', 'PADRE ABAD', 'PURUS'], horizontal=True)

PushButton(app, command=filtro1, text="Confirmar")
Text(app, text="")
PushButton(app, command=dijkstra, text="Solucion Dijkstra")
Text(app, text="")
PushButton(app, command=bfs, text="Solucion BFS")
app.display()