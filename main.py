import re 

import ProcesadorPalabras as procesador
import GestorPersistencia as bd

titulo = r"""
            Automatas y Lenguajes Formales
                  Curso 2023/2024
                Convocatoria Junio
        Profesor Juan Antonio Sánchez Laguna
"""

def cerrar(diccionario):
    bd.actualizar(diccionario)
    print ("El programa cerro con exito")
    exit()

def interpreteComandos(Comando,PalabrasAnalizadas):
    if Comando == "3":
        cerrar(PalabrasAnalizadas)
    else: 
        if Comando == "1":
            palabra = input("palabra> ")
            print(palabra)
            if palabra not in PalabrasAnalizadas:
                silabeo = procesador.silabear(palabra)

                PalabrasAnalizadas[palabra] = {'silabas': silabeo, 'silabaTonica': ''}
                print (f"\nSe añadio la palabra: {palabra} a la base de datos.\n ")
                print (f"{palabra}: {silabeo}\n")
            elif PalabrasAnalizadas[palabra].get('silabas') == '' :
                silabeo = procesador.silabear(palabra)
                PalabrasAnalizadas[palabra] = {'silabas': silabeo, 'silabaTonica': PalabrasAnalizadas[palabra].get('silabaTonica')}
                print (f"\nSe añadio la separacion silabica de {palabra}\n")
                print (f"{palabra}: {silabeo}\n")
            elif PalabrasAnalizadas[palabra].get('silabas') != '':
                print(f"\nSe encontro la separacion silabica de {palabra}\n")
                silabeo = PalabrasAnalizadas[palabra].get("silabas")
                print (f"{palabra}:{silabeo}")
        elif Comando == "2":
            palabra = input("palabra> ")
            if palabra not in PalabrasAnalizadas:
                # Se introdujo una llamada a silabear para garantizar la independencia entre funciones. 
                tonica = procesador.entonar(palabra)  

                PalabrasAnalizadas[palabra] = {'silabas':'', 'silabaTonica': tonica}

                print(f"\n[+] Se añadió la silaba tónica de {palabra} a la base de datos.")
                print (f"{palabra}:{tonica}\n")
            elif PalabrasAnalizadas[palabra].get('silabaTonica') == '':
                tonica = procesador.entonar(palabra)
                PalabrasAnalizadas[palabra]={'silabas':PalabrasAnalizadas[palabra].get('silabas'),'silabaTonica': tonica}
                print(f"\n Se añadió la silaba tónica de {palabra} a la base de datos.")
                print (f"{palabra}:{tonica}\n")
            elif PalabrasAnalizadas[palabra].get('silabaTonica') != '':
                print(f"\n Se encontró la silaba tónica de {palabra} en la base de datos.")
                tonica = PalabrasAnalizadas[palabra].get("silabaTonica")
                print(f"{palabra}:{tonica}")


def main():
    try:
        print (titulo)
        palabrasAnalizadas = {}
        bd.cargarDiccionarios(palabrasAnalizadas)
        while True:
            print("Opciones disponibles:\n")
            print(" 1) Separador de silabas.\n")
            print(" 2) Buscar vocal tónica.\n")
            print(" 3) Salir\n")
            funcion = input("Opción> ")
            interpreteComandos(funcion, palabrasAnalizadas)
    except KeyboardInterrupt:
        cerrar(palabrasAnalizadas)

if __name__ == "__main__":
    main() 