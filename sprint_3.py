#Tenemos una veterinaria donde es necesario clasificar animales por habitat
#Tenemos un archivo con el siguiente formato:

#Tipo, sonido, tipoanimal, color, habitat
#Gato,maulla,mamifero,negro,domestico
#Leon,ruge,mamifero,amarillo,salvaje

#Clase Animal con los atributos Tipo, sonido, tipoanimal,color, habitat
#Crear la clase AnimalDomestico que herede de Animal
#Crear la clase AnimalSalvaje que herede de Animal

#Se debe leer el archivo animales.csv, clasificar los animales y generar un nuevo archivo con el tipo de clasificación que el usuario escoja por consola:

# %%
import csv

class Animal:

    def _init_ (self,tipo,sonido,tipoanimal,color,habitat):
        self.tipo= tipo
        self.sonido= tipo
        self.tipoanimal= tipoanimal
        self.color= color
        self.habitat= tipo

    def __str__(self):
        return f'{{tipo: "{self.tipo}", tipoanimal: "{self.tipoanimal}", color: "{self.color}", habitat: "{self.habitat}"}}'
    
    def get_tipo(self):
        return self.tipo

    def set_tipo(self,tipo):
        self.tipo = tipo
    
    def get_sonido(self):
        return self.sonido

    def set_sonido(self,sonido):
        self.sonido = sonido

    def get_tipoanimal(self):
        return self.tipoanimal

    def set_tipoanimal(self,tipoanimal):
        self.tipo = tipoanimal
    
    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color
    
    def get_habitat(self):
        return self.habitat

    def set_habitat(self,habitat):
        self.habitat = habitat
   
class AnimalDomestico(Animal):
    pass

class AnimalSalvaje(Animal):
    pass
        
def clasificar_animales():
    animales = []

    with open('animales.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            animal = Animal(**row)
            animales.append(animal)

    return animales

def escribir_a_archivo(animales, output_path):
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['tipo', 'tipoanimal', 'color', 'habitat'])
        for animal in animales:
            writer.writerow([animal.tipo, animal.tipoanimal, animal.color, animal.habitat])

def obtener_ruta_salida():
    ruta_salida = input("Ingrese la ruta de salida para el archivo clasificado (por ejemplo, 'C:/ruta/salida/resultados'): ")
    return ruta_salida

def clasificar_animal(animal):
    clasificacion = input(f"Clasificar animal:\n{animal}\nSeleccione la clasificación (1 para Salvajes, 2 para Domésticos): ")
    return clasificacion

def main():
    animales = clasificar_animales()

    salvajes = []
    domesticos = []

    for animal in animales:
        opcion_clasificacion = clasificar_animal(animal)
        while opcion_clasificacion not in ['1', '2']:
            print("Opción incorrecta. Por favor, elija 1 para Salvajes o 2 para Domésticos.")
            opcion_clasificacion = clasificar_animal(animal)

        if opcion_clasificacion == '1':
            salvajes.append(animal)
        else:
            domesticos.append(animal)

    ruta_salida = obtener_ruta_salida()

    ruta_salvajes = f"{ruta_salida}/salvajes.csv"
    ruta_domesticos = f"{ruta_salida}/domesticos.csv"

    escribir_a_archivo(salvajes, ruta_salvajes)
    escribir_a_archivo(domesticos, ruta_domesticos)

    print(f"Se han creado los archivos de clasificación en {ruta_salvajes} y {ruta_domesticos}")

if __name__ == "__main__":
    main()
    