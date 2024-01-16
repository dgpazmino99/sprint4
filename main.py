# %%
# main.py
import argparse
from logica import escribir_nota_final, notas_promedio

def main(nombre_archivo, nombre_archivo_final):
    escribir_nota_final(nombre_archivo, nombre_archivo_final)

# Obtener argumentos de kernel de IPython
nombre_archivo = "calificaciones.csv"
nombre_archivo_final = "notaFinal.csv"

main(nombre_archivo, nombre_archivo_final)

# %%
