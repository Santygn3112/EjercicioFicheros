# Sistema de Gestión de Reservas de Vuelos

## Descripción del Proyecto

Este proyecto simula un sistema de gestión de reservas de vuelos para una aerolínea. Se ha desarrollado en Python y está dividido en tres partes que incrementan progresivamente en complejidad, abarcando desde operaciones básicas de archivos hasta manejo avanzado de errores y registro de incidencias.

## Requisitos del Sistema

- Python 3.x
- Sistema operativo: Windows, Linux o macOS
- No se requieren librerías externas adicionales

## Resolución de las Partes

### Parte 1: Gestión Básica de Reservas

**Objetivo:** Crear, escribir y leer un archivo de reservas básico.

**Implementación:**

1. **Creación del archivo:** Se utiliza la función `open()` con modo escritura (`'w'`) para crear el archivo `reservas.txt`.

2. **Escritura de datos:** Se define una lista con las reservas en formato `[Asiento], [Nombre], [Clase]` y se escriben línea por línea en el archivo utilizando el método `write()`.

3. **Lectura y procesamiento:** 
   - Se abre el archivo en modo lectura (`'r'`)
   - Se utiliza `readlines()` para obtener todas las líneas
   - Se procesan los datos utilizando `split(',')` para separar los campos
   - Se utiliza `strip()` para eliminar espacios en blanco y saltos de línea

4. **Análisis de datos:**
   - Contador de reservas totales
   - Contador específico de pasajeros en clase Business
   - Impresión formateada de cada reserva

**Conceptos aplicados:**
- Operaciones básicas de archivos (open, write, read, close)
- Manipulación de strings (split, strip)
- Estructuras de control (for, if)
- Codificación UTF-8 para soportar caracteres especiales

### Parte 2: Clasificación por Destinos

**Objetivo:** Clasificar reservas en diferentes archivos según el destino del vuelo.

**Implementación:**

1. **Archivo maestro:** Se crea `reservas_maestro.txt` con un campo adicional: el destino del vuelo.

2. **Lectura y clasificación:**
   - Se lee el archivo maestro línea por línea
   - Se extrae el campo `destino` de cada reserva
   - Se genera dinámicamente el nombre del archivo destino usando f-strings: `f"reservas_{destino.lower()}.txt"`

3. **Escritura en archivos múltiples:**
   - Se utiliza el modo `'a'` (append) para añadir datos sin sobrescribir
   - Esto permite que múltiples reservas del mismo destino se acumulen en el mismo archivo

4. **Contador de destinos:**
   - Se implementa un diccionario para llevar el conteo de reservas por destino
   - Se imprime un resumen al finalizar el procesamiento

**Conceptos aplicados:**
- Modo append para archivos
- Diccionarios para conteo y agrupación
- Generación dinámica de nombres de archivo
- Formateo de strings con lower() para normalización

### Parte 3: Manejo de Errores y Registro

**Objetivo:** Implementar validación de datos y registro automático de errores con marca temporal.

**Implementación:**

1. **Archivo con errores intencionales:** Se crea `reservas_maestro_con_errores.txt` que incluye:
   - Líneas con campos faltantes
   - Líneas vacías
   - Líneas con formato incorrecto

2. **Sistema de validación:**
   - Verificación de líneas vacías o con solo espacios en blanco
   - Validación del número exacto de campos (debe ser 4)
   - Verificación de que ningún campo esté vacío

3. **Registro de errores:**
   - Uso del módulo `datetime` para obtener fecha y hora actual
   - Formato de registro: `[Fecha Hora], [Línea errónea], [Descripción del error]`
   - Creación del archivo `registro_errores.log`

4. **Procesamiento diferenciado:**
   - Reservas válidas: se clasifican y guardan por destino
   - Reservas inválidas: se registran en el log de errores
   - Contador separado para reservas válidas y errores

5. **Informe final:**
   - Resumen de archivos creados con cantidad de reservas válidas
   - Visualización completa del contenido del archivo de errores

**Conceptos aplicados:**
- Módulo datetime para marcas temporales
- Validación de datos con múltiples condiciones
- Manejo de excepciones y casos especiales
- Logging de errores
- Formato strftime para fechas: `"%Y-%m-%d %H:%M:%S"`

## Configuración de Encoding (UTF-8)

Durante el desarrollo se identificó un problema con la visualización de caracteres especiales (tildes, eñes) en la terminal de Windows, que utiliza por defecto la codificación cp1252.

**Solución implementada con ayuda de IA:**

Esta solución fue consultada mediante IA para resolver específicamente el problema de encoding en terminales Windows. Se añadieron las siguientes líneas al inicio de cada archivo Python:

```python
import sys
import io

# Configurar salida UTF-8 en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

Esta configuración permite:
- Visualización correcta de acentos (á, é, í, ó, ú)
- Soporte para la letra ñ
- Compatibilidad con caracteres especiales en español


## Instrucciones de Ejecución

### Ejecución Individual por Partes

Cada parte es independiente y debe ejecutarse en orden:

#### Parte 1:
```bash
python parte1_reservas.py
```

**Resultado esperado:**
- Se crea el archivo `reservas.txt`
- Se muestra en consola: información de cada reserva, total de reservas y cantidad de pasajeros en Business

#### Parte 2:
```bash
python parte2_destinos.py
```

**Resultado esperado:**
- Se crea el archivo `reservas_maestro.txt`
- Se generan archivos individuales por destino: `reservas_madrid.txt`, `reservas_paris.txt`, `reservas_londres.txt`
- Se muestra en consola: confirmación de cada reserva procesada y resumen por destino

#### Parte 3:
```bash
python parte3_errores.py
```

**Resultado esperado:**
- Se crea el archivo `reservas_maestro_con_errores.txt`
- Se generan archivos por destino con solo las reservas válidas
- Se crea el archivo `registro_errores.log` con los errores encontrados
- Se muestra en consola: procesamiento línea por línea, resumen de archivos creados y contenido del log de errores

### Verificación de Archivos Generados

Después de ejecutar cada parte, verifica que se hayan creado los archivos correspondientes en el directorio del proyecto:

- **Parte 1:** `reservas.txt`
- **Parte 2:** `reservas_maestro.txt`, `reservas_madrid.txt`, `reservas_paris.txt`, `reservas_londres.txt`
- **Parte 3:** `reservas_maestro_con_errores.txt`, archivos por destino actualizados, `registro_errores.log`