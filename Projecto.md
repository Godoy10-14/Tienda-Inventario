# Proyecto: Sistema de Gestión de Inventario con SQLite

## Objetivo
Construir una aplicación de consola que administre el inventario de una tienda, usando una **base de datos SQLite** en lugar de estructuras en memoria (listas/diccionarios). Esto obliga a combinar fundamentos de Python con conocimientos de bases de datos.

## Contexto
Eres el desarrollador encargado de digitalizar el inventario de una tienda. El requisito clave es que los datos **persistan** entre ejecuciones del programa: cerrar y volver a abrir no debe perder información, porque todo vive en un archivo `.db`.

---

## Requisitos funcionales

A través de un **menú interactivo**, el programa debe permitir:

1. **Agregar un producto nuevo**
   - Nombre, precio, cantidad y categoría.
   - No permitir nombres duplicados (forzarlo tanto en la lógica de Python como con una restricción `UNIQUE` en la tabla).

2. **Listar todos los productos**
   - Traer todos los registros de la tabla y mostrarlos con su subtotal (precio × cantidad).
   - Si la tabla está vacía, indicarlo claramente.

3. **Buscar un producto por nombre**
   - Consultar en la base de datos filtrando por nombre.
   - Manejar el caso de que no exista.

4. **Actualizar stock**
   - Sumar o restar unidades directamente en la base de datos.
   - No permitir que quede en negativo (validar antes de hacer el `UPDATE`).

5. **Eliminar un producto**
   - Pedir confirmación antes de borrar el registro.
   - Manejar el caso de que el producto no exista.

6. **Calcular el valor total del inventario**
   - Se puede resolver trayendo todos los registros y sumando en Python, o con una consulta SQL que calcule la suma directamente. Pensar cuál es más apropiado y por qué.

7. **Filtrar por categoría**
   - Aprovechar la base de datos real para hacer consultas con condiciones (`WHERE categoría = ...`).

8. **Salir del programa**
   - Cerrar la conexión a la base de datos correctamente antes de terminar.

---

## Requisitos técnicos

- **Base de datos:** una tabla `productos` con columnas como id (clave primaria autoincremental), nombre, precio, cantidad, categoría.
- **Conexión:** decidir cómo manejar la conexión — ¿se abre una vez al iniciar el programa y se mantiene abierta, o se abre/cierra en cada operación? Investigar ventajas y desventajas de cada enfoque y elegir con criterio.
- **Separación de responsabilidades (módulos):** al menos tres archivos:
  - `main.py`: menú y flujo del programa.
  - `db.py` (o `inventario.py`): todas las funciones que hablan con la base de datos (crear tabla, insertar, consultar, actualizar, eliminar).
  - Opcional: un archivo o función separada para la creación/inicialización de la base de datos (crear la tabla si no existe).
- **Funciones:** cada operación debe ser su propia función, que reciba parámetros y devuelva resultados — nada de SQL disperso dentro del menú.
- **Manejo de errores:** contemplar tanto errores de entrada del usuario (texto donde va un número) como errores propios de la base de datos (por ejemplo, intentar insertar un nombre duplicado si se usó `UNIQUE`).
- **Parámetros seguros en las consultas:** investigar por qué no se deben construir consultas SQL concatenando strings directamente con los datos del usuario, y qué mecanismo ofrece la librería de SQLite en Python para hacerlo de forma segura.

---

## Casos borde que debes contemplar

- ¿Qué pasa si la base de datos o la tabla no existen todavía la primera vez que se ejecuta el programa?
- ¿Qué pasa si dos productos "casi" iguales se agregan (mismo nombre con mayúsculas distintas, por ejemplo "Mouse" vs "mouse")? ¿Se van a tratar como el mismo producto o no? Definir el criterio y ser consistente.
- ¿Qué pasa si se cae la conexión a mitad de una operación?
- ¿Qué pasa si el usuario intenta filtrar por una categoría que no existe?

---

## Preguntas de diseño (responder antes de programar)

1. ¿Qué tipos de dato se le van a asignar a cada columna de la tabla y por qué?
2. ¿En qué momento del programa se va a crear la tabla si no existe — cada vez que arranca, o solo la primera vez?
3. ¿La función de "agregar producto" debe verificar duplicados en Python antes de insertar, o se debe dejar que la base de datos lo rechace con la restricción `UNIQUE` y capturar ese error?
4. ¿Cómo se va a estructurar el valor de retorno de las funciones de consulta, para que `main.py` pueda usarlas sin saber nada de SQL?

---

## Extra (opcional)

- Agregar una tabla de "movimientos" o "historial" que registre cada entrada/salida de stock con fecha, para llevar trazabilidad.
- Generar un reporte de productos con stock bajo directamente con una consulta SQL (`WHERE cantidad < 5`), en vez de filtrar en Python.
