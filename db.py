import sqlite3 as sql

DB_NAME = "/home/cristofer/Documents/Inventario System/Inventario.db"

def get_connetion():
    return sql.connect(DB_NAME)

def exists_value_from_products(user_product):
    search_value = f"%{user_product}%"
    querry = """
    SELECT id_producto,nombre_producto, unidades, precio_unitario
    FROM Productos
    WHERE nombre_producto LIKE ? AND unidades > 0
    """
    with get_connetion() as conexion:
        cursor = conexion.cursor()
        cursor.execute(querry, (search_value,))
        registros = cursor.fetchall()
    conexion.close()
    if not registros:
        return []
    return registros

def actualizar_productos(user_id_producto):
    querry = """
    SELECT id_producto,nombre_producto, unidades, precio_unitario
    FROM Productos
    WHERE id_producto = ?
    """
    with get_connetion() as conexion:
        cursor = conexion.cursor()
        cursor.execute(querry,(user_id_producto,))
        registros = cursor.fetchall()
    conexion.close()
    return registros

def modificar_unidades_from_productos(user_id_producto,user_unidad):
    querry = """
        UPDATE Productos
        SET unidades = ?
        WHERE id_producto = ?
    """
    with get_connetion() as conexion:
        cursor = conexion.cursor()
        cursor.execute(querry,(user_unidad,user_id_producto))
        return "Tu venta se sido exitosa..."
        

        