
# Imports
import sys
import io

# Configurar salida UTF-8 en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Creacion del archivo
archivo = open('reservas.txt', 'w', encoding='utf-8')

reservas = [
    "12A, Juan Pérez, Economy",
    "14B, María López, Business",
    "21C, Carlos García, Economy"
]

for reserva in reservas:
    archivo.write(reserva + '\n')

archivo.close()
print("Archivo 'reservas.txt' creado correctamente\n")

archivo = open('reservas.txt', 'r', encoding='utf-8')

lineas = archivo.readlines()

archivo.close()

total_reservas = 0
pasajeros_business = 0

print("RESERVAS REGISTRADAS:")
print("-" * 50)

for linea in lineas:
    linea = linea.strip()
    
    if linea:
        datos = linea.split(',')
        
        asiento = datos[0].strip()
        nombre = datos[1].strip()
        clase = datos[2].strip()
        
        print(f"Asiento: {asiento}")
        print(f"Pasajero: {nombre}")
        print(f"Clase: {clase}")
        print("-" * 50)
        
        total_reservas += 1
        
        if clase == "Business":
            pasajeros_business += 1

print(f"Total de reservas: {total_reservas}")
print(f"Pasajeros en Business: {pasajeros_business}")