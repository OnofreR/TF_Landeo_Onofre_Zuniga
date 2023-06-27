import csv

class CSVReader:
    def __init__(self, archivo):
        self.archivo = archivo
        self.columna1 = []

    def leer_csv(self, provincia, distrito):
        with open(self.archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if fila[3] == provincia:
                    if fila[4] == distrito:
                        self.columna1.append(fila[0])

    def obtener_columna1(self):
        return self.columna1