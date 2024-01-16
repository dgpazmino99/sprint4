#%%

# logica.py
import csv
import os

def notas_promedio(lecciones, tareas, examen):
    return (lecciones + tareas + examen) / 3

def escribir_nota_final(nombre_archivo_entrada, nombre_archivo_salida):
    if not os.path.exists(nombre_archivo_entrada):
        print(f"Error: El archivo seleccionado {nombre_archivo_entrada} no existe.")
        return

    with open(nombre_archivo_entrada, 'r') as archivo_entrada:
        lector_csv = csv.DictReader(archivo_entrada)

        with open(nombre_archivo_salida, 'w', newline='') as archivo_salida:
            campos = ['estudiante', 'notaFinal']
            escritor_csv = csv.DictWriter(archivo_salida, fieldnames=campos)
            escritor_csv.writeheader()

            for fila in lector_csv:
                estudiante = fila['estudiante']
                lecciones = float(fila['lecciones'])
                tareas = float(fila['tareas'])
                examen = float(fila['examen'])

                nota_final = notas_promedio(lecciones, tareas, examen)

                escritor_csv.writerow({'estudiante': estudiante, 'notaFinal': round(nota_final, 2)})
