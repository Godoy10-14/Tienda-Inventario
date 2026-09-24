import sqlite3 as sql


DB_NAME = "/home/cristofer/Documents/Inventario System/Inventario.db"

def get_connetion():
    return sql.connect(DB_NAME)

def exists_value_from_products(user_product):
    search_value = f"%{user_product}%"
    querry = """
    SELECT id_producto,nombre_producto, unidades, precio_unitario
    FROM Productos
    WHERE nombre_producto LIKE ?
    """
    with get_connetion() as conexion:
        cursor = conexion.cursor()
        cursor.execute(querry, (search_value,))
        registros = cursor.fetchall()
    conexion.close()
    if not registros:
        return []

    for index,registro in enumerate(registros):
        print(f"{index+1} | Nombre: {registro[1]} | Unidades: {registro[2]} | Precio: {registro[3]}")

    return registros

def actualizar_productos():
    querry = """
    SELECT id_producto,nombre_producto, unidades, precio_unitario
    FROM Productos
    """
    with get_connetion() as conexion:
        cursor = conexion.cursor()
        cursor.execute(querry)
        registros = cursor.fetchall()
    conexion.close()
    return registros

def modificar_unidades_from_productos(user_id_producto,user_unidad):
    querry = """
    SELECT id_producto,nombre_producto, unidades, precio_unitario 
    FROM Productos 
    WHERE unidades > 0 and id_producto = ?
    """
    with get_connetion() as conexion:
        cursor = conexion.cursor()
        cursor.execute(querry,(user_id_producto,))
        registro = cursor.fetchall()
        unidad_table = registro[0][2]
        if unidad_table < user_unidad:
          print()
        unidad_total = unidad_table - user_unidad
        resgistros = cursor.execute("""UPDATE Productos 
        SET unidades = ?
        WHERE id_producto = ? """, (unidad_total, user_id_producto))
        return "Listo tu venta ha sido completada"
