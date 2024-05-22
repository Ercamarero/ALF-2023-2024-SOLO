import os
import csv
DIRECTORIO_BASE = os.getcwd()
DIRECTORIO_BASE_CSV = os.path.join(DIRECTORIO_BASE, "baseDeDatos.csv")

print (DIRECTORIO_BASE)
with open (DIRECTORIO_BASE_CSV, mode='w', newline='') as baseDeDatos:
    escritor = csv.writer(baseDeDatos, delimiter=';')
    escritor.writerow(['Palabra', 'Silabas', 'SilabaTonica'])