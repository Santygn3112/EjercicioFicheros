# Imports
import sys
import io

# Configurar salida UTF-8 en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from datetime import datetime

# Crear un archivo maestro con algunas líneas erróneas para pruebas
archivo = open('reservas_maestro_con_errores.txt', 'w', encoding='utf-8')

datos_con_errores = [
    "12A, Juan Pérez, Economy, Madrid",
    "14B, María López, Business",  # Falta destino
    "21C, Carlos García, Economy, Madrid",
    "",  # Línea vacía
    "05D, Ana Sánchez, Business, Londres",
    "19E, Luis Gómez",  # Faltan clase y destino
    "08F, Sofía Vargas, Economy, París",
    "10G, Pedro Ruiz, Business, Londres",
    "15H, Elena Martín, Economy",  # Falta destino
    "   ",  # Línea solo con espacios
    "22I, Laura Torres, Economy, Madrid"
]

for linea in datos_con_errores:
    archivo.write(linea + '\n')

archivo.close()
print("Archivo 'reservas_maestro_con_errores.txt' creado\n")


archivo = open('reservas_maestro_con_errores.txt', 'r', encoding='utf-8')
lineas = archivo.readlines()
archivo.close()

archivo_errores = open('registro_errores.log', 'w', encoding='utf-8')

# Diccionario para contar reservas válidas por destino
contador_destinos = {}
total_errores = 0

# Procesamos cada línea
for numero_linea, linea in enumerate(lineas, 1):
    linea_original = linea
    linea = linea.strip()
    
    # Obtener la fecha y hora actual
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Verificar si la línea está vacía
    if not linea:
        error_msg = f"[{fecha_hora}], Línea {numero_linea} vacía, Error: Línea vacía\n"
        archivo_errores.write(error_msg)
        total_errores += 1
        print(f"Error en línea {numero_linea}: Línea vacía")
        continue
    
    datos = linea.split(',')
    
    # Verificar que tenga exactamente 4 campos
    if len(datos) != 4:
        # Determinar qué campo falta
        if len(datos) == 1:
            descripcion = "Faltan todos los campos excepto uno"
        elif len(datos) == 2:
            descripcion = "Faltan los campos 'clase' y 'destino'"
        elif len(datos) == 3:
            descripcion = "Falta el campo 'destino'"
        else:
            descripcion = f"Número incorrecto de campos ({len(datos)} en lugar de 4)"
        
        error_msg = f"[{fecha_hora}], {linea}, {descripcion}\n"
        archivo_errores.write(error_msg)
        total_errores += 1
        print(f"Error en línea {numero_linea}: {descripcion}")
        continue
    
    asiento = datos[0].strip()
    nombre = datos[1].strip()
    clase = datos[2].strip()
    destino = datos[3].strip()
    
    if not asiento or not nombre or not clase or not destino:
        error_msg = f"[{fecha_hora}], {linea}, Error: Uno o más campos están vacíos\n"
        archivo_errores.write(error_msg)
        total_errores += 1
        print(f"Error en línea {numero_linea}: Campo vacío")
        continue
    
    nombre_archivo = f"reservas_{destino.lower()}.txt"
    
    archivo_destino = open(nombre_archivo, 'a', encoding='utf-8')
    archivo_destino.write(linea + '\n')
    archivo_destino.close()
    
    if destino in contador_destinos:
        contador_destinos[destino] += 1
    else:
        contador_destinos[destino] = 1
    
    print(f"Reserva de {nombre} añadida a {nombre_archivo}")

archivo_errores.close()


print("ARCHIVOS DE DESTINO CREADOS:")
print("-" * 60)
for destino, cantidad in contador_destinos.items():
    nombre_archivo = f"reservas_{destino.lower()}.txt"
    print(f"• {nombre_archivo}: {cantidad} reservas válidas")

print(f"\nTotal de errores encontrados: {total_errores}")

# Mostramos el contenido del archivo de errores
archivo_errores = open('registro_errores.log', 'r', encoding='utf-8')
contenido_errores = archivo_errores.read()
archivo_errores.close()

if contenido_errores:
    print(contenido_errores)
else:
    print("No se encontraron errores en el procesamiento.")