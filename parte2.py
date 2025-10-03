# Imports
import sys
import io

# Configurar salida UTF-8 en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Creacion del archivo maestro
archivo = open('reservas_maestro.txt', 'w', encoding='utf-8')

reservas_maestro = [
    "12A, Juan Pérez, Economy, Madrid",
    "14B, María López, Business, París",
    "21C, Carlos García, Economy, Madrid",
    "05D, Ana Sánchez, Business, Londres",
    "19E, Luis Gómez, Economy, París",
    "08F, Sofía Vargas, Economy, Londres"
]

for reserva in reservas_maestro:
    archivo.write(reserva + '\n')

archivo.close()
print("Archivo 'reservas_maestro.txt' creado correctamente\n")

archivo = open('reservas_maestro.txt', 'r', encoding='utf-8')
lineas = archivo.readlines()
archivo.close()

# Diccionario para contar reservas por destino
contador_destinos = {}

for linea in lineas:
    linea = linea.strip()
    
    if linea:
        datos = linea.split(',')
        
        asiento = datos[0].strip()
        nombre = datos[1].strip()
        clase = datos[2].strip()
        destino = datos[3].strip()
        
        # Creacion del nombre del archivo para este destino
        nombre_archivo = f"reservas_{destino.lower()}.txt"
        
        archivo_destino = open(nombre_archivo, 'a', encoding='utf-8')
        
        archivo_destino.write(linea + '\n')
        
        archivo_destino.close()
        
        if destino in contador_destinos:
            contador_destinos[destino] += 1
        else:
            contador_destinos[destino] = 1
        
        print(f"Reserva de {nombre} añadida a {nombre_archivo}")


for destino, cantidad in contador_destinos.items():
    nombre_archivo = f"reservas_{destino.lower()}.txt"
    print(f"Archivo: {nombre_archivo}")
    print(f"Reservas totales: {cantidad}")
    print("-" * 50)

print(f"\nTotal de archivos creados: {len(contador_destinos)}")