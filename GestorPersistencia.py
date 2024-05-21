import csv 
import os
DIRECTORIO_BASE = os.getcwd()
DIRECTORIO_BASE_CSV = os.path.join(DIRECTORIO_BASE, "baseDeDatos.csv")
def cargarDiccionarios(diccionario):
    try:
        with open(DIRECTORIO_BASE_CSV) as bd:
            lector = csv.reader(bd,delimiter=';')

            next(lector)

            for i in lector:
                palabra = i[0]

                if i[1] != '':
                    silabas = eval(i[1])
                else:
                    silabas = ''

                if i[2] != '':
                    silabaTonica = eval(i[2])
                else :
                    silabaTonica = '' 
                
                diccionario[palabra] = {
                    'silabas': silabas,
                    'silabaTonica': silabaTonica
                }
    except FileNotFoundError:
        print ("Error: El fichero de la base de datos fue ilocalizable.")
        print ("Creando una nueva base de datos.")
        with open (DIRECTORIO_BASE_CSV, mode='w', newline='') as baseDeDatos:
            escritor = csv.writer(baseDeDatos, delimiter=';')
            escritor.writerow(['Palabra', 'Silabas', 'SilabaTonica'])
    except PermissionError:
        print("Error: NO se disponen de los permisos necesarios.")
def actualizar(diccionario):
    try:
        with open(DIRECTORIO_BASE_CSV, 'w', newline='') as baseDeDatos:
            escritor = csv.writer(baseDeDatos, delimiter=';')
            escritor.writerow(['Palabra', 'Silabas', 'SilabaTonica'])

            for palabra, valores in diccionario.items():
                silabas = valores ['silabas']
                silabaTonica = valores['silabaTonica']
                escritor.writerow([palabra, silabas, silabaTonica])

            print("La base de datos ha sido actualizada")
    except PermissionError:
        print("Error: NO se disponen de los permisos necesarios.")
